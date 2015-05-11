from __future__ import absolute_import

import pytest

import schematec.validators as validators
import schematec.exc as exc


def test_empty_dict():
    with pytest.raises(exc.ValidationError):
        validators.required('a', {})


def test_list():
    validators.required('a', {'a': []})


def test_none():
    validators.required('a', {'a': None})


def test_int():
    validators.required('a', {'a': 1})


def test_empty_str():
    validators.required('a', {'a': ''})


def test_str():
    validators.required('a', {'a': 'aaa'})
