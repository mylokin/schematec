from __future__ import absolute_import

import pytest

import schematec.validators as validators
import schematec.exc as exc


def test_string():
    validators.length(1)('a')


def test_empty_list():
    validators.length(1)([])


def test_list():
    validators.length(1)(['1'])


def test_tuple():
    validators.length(1)(('1',))


def test_too_long_string():
    with pytest.raises(exc.ValidationError):
        validators.length(1)('aa')
