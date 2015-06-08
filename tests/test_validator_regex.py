from __future__ import absolute_import

import re

import pytest

import schematec.validators as validators
import schematec.exc as exc


def test_valid_string():
    regex = re.compile('\w')
    validators.regex(regex)('a')


def test_invalid_string():
    regex = re.compile('\s')
    with pytest.raises(exc.ValidationError):
        validators.regex(regex)('a')
