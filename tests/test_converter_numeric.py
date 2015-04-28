from __future__ import absolute_import

import pytest

import schematec.converters as converters
import schematec.exc as exc


def test_zero():
    assert converters.numeric(0) == 0


def test_positive_number():
    assert converters.numeric(1) == 1


def test_negative_number():
    assert converters.numeric(-1) == -1


def test_long():
    assert converters.numeric(1L) == 1


def test_long_type():
    assert isinstance(converters.numeric(1L), int)


def test_positive_number_string():
    assert converters.numeric('1') == 1


def test_positive_number_string_type():
    assert isinstance(converters.numeric('1'), int)


def test_negative_number_string():
    assert converters.numeric('-1') == -1


def test_positive_number_unicode_string():
    assert converters.numeric(u'1') == 1


def test_positive_number_unicode_string_type():
    assert isinstance(converters.numeric(u'1'), int)


def test_negative_number_unicode_string():
    assert converters.numeric(u'-1') == -1


def test_not_number_string():
    with pytest.raises(exc.ConvertationError):
        converters.numeric('a')


def test_empty_string():
    with pytest.raises(exc.ConvertationError):
        converters.numeric('')


def test_none():
    with pytest.raises(exc.ConvertationError):
        converters.numeric(None)


def test_boolean_true():
    assert converters.numeric(True) == 1


def test_boolean_true_type():
    assert isinstance(converters.numeric(True), int)


def test_boolean_false():
    assert converters.numeric(False) == 0


def test_boolean_false_type():
    assert isinstance(converters.numeric(False), int)


def test_unknown_type():
    with pytest.raises(exc.ConvertationError):
        converters.numeric(type)
