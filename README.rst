
*************************************
datatest: Test driven data-wrangling
*************************************
..
    Project badges for quick reference:

|buildstatus| |devstatus| |license| |pyversions|

.. start-inclusion-marker-description

Datatest provides validation tools for test driven data-wrangling.
It extends Python's `unittest
<http://docs.python.org/3/library/unittest.html>`_ package to provide
testing tools for asserting data correctness.

..
    Datatest provides validation tools for test driven data-wrangling.
    It includes tools to quickly load, query, and validate data using
    both unittest- and pytest-style testing.

Datatest can help prepare messy data that needs to be cleaned,
integrated, formatted, and verified. It can provide structure for the
tidying process, automate checklists, log discrepancies, and measure
progress.

.. end-inclusion-marker-description


* Documentation:
    - https://datatest.readthedocs.io/ (stable)
    - https://datatest.readthedocs.io/en/latest/ (latest)
* Official Releases:
   - https://pypi.python.org/pypi/datatest
* Development:
   - https://github.com/shawnbrown/datatest


Installation
============

.. start-inclusion-marker-install

The easiest way to install datatest is to use pip::

  pip install datatest

To upgrade an existing installation, use the "``--upgrade``" option::

  pip install --upgrade datatest


Stuntman Mike
-------------

If you need bug-fixes or features that are not available
in the current stable release, you can "pip install" the
development version directly from GitHub::

  pip install --upgrade https://github.com/shawnbrown/datatest/archive/master.zip

All of the usual caveats for a development install should
apply---only use this version if you can risk some instability
or if you know exactly what you're doing. While care is taken
to never break the build, it can happen.


Safety-first Clyde
------------------

If you need to review and test packages before installing, you can
install datatest manually.

Download the latest **source** distribution from the Python Package
Index (PyPI):

  https://pypi.python.org/pypi/datatest#downloads

Unpack the file (replacing X.Y.Z with the appropriate version number)
and review the source code::

  tar xvfz datatest-X.Y.Z.tar.gz

Change to the unpacked directory and run the tests::

  cd datatest-X.Y.Z
  python setup.py test

Don't worry if some of the tests are skipped. Tests for optional data
sources (like pandas DataFrames or MS Excel files) are skipped when the
related third-party packages are not installed.

If the source code and test results are satisfactory, install the
package::

  python setup.py install

.. end-inclusion-marker-install


Supported Versions
==================

Tested on Python 2.6, 2.7, and 3.1 through 3.6; PyPy and PyPy3.
Datatest is pure Python and is also likely to run on Jython, Stackless,
and other implementations without issue (check using "setup.py test"
before installing).


Backward Compatibility
======================

If you have existing tests that use API features which have
changed since 0.7.0.dev2, you can still run your old code by
adding the following import to the beginning of each file::

  from datatest.__past__ import api07

To maintain existing test code, this project makes a best-effort
attempt to provide backward compatibility support for older
features. The API will be improved in the future but only in
measured and sustainable ways.

All of the data used at the `National Committee for an Effective
Congress <http://ncec.org/about>`_ has been checked with datatest
for more than a year so there is, already, a large and growing
codebase that relies on current features and must be maintained
into the future.


Dependencies
============

There are no hard, third-party dependencies. But if you want to
interface with pandas DataFrames, MS Excel workbooks, or other
optional data sources, you will need to install the relevant
packages (``pandas``, ``xlrd``, etc.).


------------

Freely licensed under the Apache License, Version 2.0

Copyright 2014 - 2017 NCEC Services, LLC and contributing authors


.. |buildstatus| image:: https://api.travis-ci.org/shawnbrown/datatest.png
    :target: https://travis-ci.org/shawnbrown/datatest
    :alt: Current Build Status

.. |devstatus| image:: https://img.shields.io/pypi/status/datatest.svg
    :target: https://pypi.python.org/pypi/datatest
    :alt: Development Status

.. |license| image:: https://img.shields.io/badge/license-Apache%202-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache 2.0 License

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/datatest.svg
    :target: https://pypi.python.org/pypi/datatest#supported-versions
    :alt: Supported Python Versions

.. |githubstars| image:: https://img.shields.io/github/stars/shawnbrown/datatest.svg
    :target: https://github.com/shawnbrown/datatest/stargazers
    :alt: GitHub users who have starred this project

.. |pypiversion| image:: https://img.shields.io/pypi/v/datatest.svg
    :target: https://pypi.python.org/pypi/datatest
    :alt: Current PyPI Version
