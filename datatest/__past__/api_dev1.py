# -*- coding: utf-8 -*-
"""Backwards compatibility for version 0.6.0.dev1 API."""
from __future__ import absolute_import
from datatest import DataTestCase


DataTestCase.subjectData = DataTestCase.subject
DataTestCase.referenceData = DataTestCase.reference