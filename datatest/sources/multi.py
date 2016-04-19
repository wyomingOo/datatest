# -*- coding: utf-8 -*-
from ..utils.builtins import *
from ..utils import collections
from ..utils import itertools
from ..utils import functools

from ..compare import CompareDict
from ..compare import CompareSet

from .base import BaseSource
from .adapter import AdapterSource


class MultiSource(BaseSource):
    """
    MultiSource(*sources, missing='')

    A wrapper class that allows multiple data sources to be treated
    as a single, composite data source::

        subjectData = datatest.MultiSource(
            datatest.CsvSource('file1.csv'),
            datatest.CsvSource('file2.csv'),
            datatest.CsvSource('file3.csv')
        )

    The original sources are stored in the ``__wrapped__`` attribute.
    """
    def __init__(self, *sources, **kwd):
        """
        __init__(self, *sources, missing='')

        Initialize self.
        """
        # Accept `missing` as a keyword-only argument.
        try:
            missing = kwd.pop('missing')
        except KeyError:
            missing = ''

        if kwd:                     # Enforce keyword-only argument
            key, _ = kwd.popitem()  # behavior that works in Python 2.x.
            msg = "__init__() got an unexpected keyword argument " + repr(key)
            raise TypeError(msg)

        msg = 'Sources must be derived from BaseSource'
        assert all(isinstance(s, BaseSource) for s in sources), msg

        all_columns = []
        for s in sources:
            for c in s.columns():
                if c not in all_columns:
                    all_columns.append(c)

        normalized_sources = []
        for s in sources:
            if set(s.columns()) < set(all_columns):
                columns = s.columns()
                fn = lambda x: x if x in columns else None
                old = [fn(x) for x in all_columns]
                interface = list(zip(all_columns, old))
                s = AdapterSource(s, interface, missing)
            normalized_sources.append(s)

        self._columns = all_columns
        self._sources = normalized_sources
        self.__wrapped__ = sources  # <- Original sources.

    def __repr__(self):
        """Return a string representation of the data source."""
        cls_name = self.__class__.__name__
        src_names = [repr(src) for src in self.__wrapped__]  # Get reprs.
        src_names = ['    ' + src for src in src_names]      # Prefix with 4 spaces.
        src_names = ',\n'.join(src_names)                    # Join w/ comma & new-line.
        return '{0}(\n{1}\n)'.format(cls_name, src_names)

    def columns(self):
        """Return list of column names."""
        return self._columns

    def __iter__(self):
        """Return iterable of dictionary rows (like csv.DictReader)."""
        #columns = self.columns()
        for source in self._sources:
            for row in source.__iter__():
                yield row

    def filter_rows(self, **kwds):
        for source in self._sources:
            for row in source.filter_rows(**kwds):
                yield row

    def distinct(self, columns, **kwds_filter):
        """Return iterable of tuples containing distinct *column*
        values.
        """
        fn = lambda source: source.distinct(columns, **kwds_filter)
        results = (fn(source) for source in self._sources)
        results = itertools.chain(*results)
        return CompareSet(results)

    def sum(self, column, keys=None, **kwds_filter):
        """Return sum of values in *column* grouped by *keys*."""
        fn = lambda source: source.sum(column, keys, **kwds_filter)
        results = (fn(source) for source in self._sources)

        if not keys:
            return sum(results)  # <- EXIT!

        sum_total = collections.defaultdict(lambda: 0)
        for result in results:
            for key, val in result.items():
                sum_total[key] += val
        return CompareDict(sum_total, keys)

    #def count(self, column, keys=None, **kwds_filter):
    #    pass

    def mapreduce(self, mapper, reducer, columns, keys=None, **kwds_filter):
        fn = lambda source: source.mapreduce(mapper, reducer, columns, keys, **kwds_filter)
        results = (fn(source) for source in self._sources)

        if not keys:
            return functools.reduce(reducer, results)  # <- EXIT!

        final_result = {}
        results = (result.items() for result in results)
        for key, y in itertools.chain(*results):
            if key in final_result:
                x = final_result[key]
                final_result[key] = reducer(x, y)
            else:
                final_result[key] = y
        return CompareDict(final_result, keys)