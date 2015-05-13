from __future__ import absolute_import

import pytest

import schematec.converters as converters
import schematec.exc as exc


def test_zero():
    assert converters.number(0.) == 0.


def test_positive_number():
    assert converters.number(1.) == 1.


def test_negative_number():
    assert converters.number(-1.) == -1.


def test_long():
    assert converters.number(1L) == 1.


def test_int():
    assert converters.number(1) == 1.


def test_long_type():
    assert isinstance(converters.number(1L), float)


def test_positive_number_string():
    assert converters.number('1') == 1.


def test_positive_number_string_type():
    assert isinstance(converters.number('1'), float)


def test_negative_number_string():
    assert converters.number('-1') == -1.


def test_positive_number_unicode_string():
    assert converters.number(u'1') == 1.


def test_positive_number_unicode_string_type():
    assert isinstance(converters.number(u'1'), float)


def test_negative_number_unicode_string():
    assert converters.number(u'-1') == -1.


def test_not_number_string():
    with pytest.raises(exc.ConvertationError):
        converters.number('a')


def test_empty_string():
    with pytest.raises(exc.ConvertationError):
        converters.number('')


def test_none():
    with pytest.raises(exc.ConvertationError):
        converters.number(None)


def test_boolean_true():
    assert converters.number(True) == 1.


def test_boolean_true_type():
    assert isinstance(converters.number(True), float)


def test_boolean_false():
    assert converters.number(False) == 0.


def test_boolean_false_type():
    assert isinstance(converters.number(False), float)


def test_unknown_type():
    with pytest.raises(exc.ConvertationError):
        converters.number(type)
