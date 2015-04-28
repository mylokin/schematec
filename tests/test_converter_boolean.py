from __future__ import absolute_import

import pytest

import schematec.converters as converters
import schematec.exc as exc


def test_zero():
    assert converters.boolean(0) == False


def test_zero_type():
    assert isinstance(converters.boolean(0), bool)


def test_one():
    assert converters.boolean(1) == True


def test_one_type():
    assert isinstance(converters.boolean(1), bool)


def test_positive_number():
    with pytest.raises(exc.ConvertationError):
        converters.boolean(2)


def test_negative_number():
    with pytest.raises(exc.ConvertationError):
        converters.boolean(-1)


def test_one_long():
    assert converters.boolean(1L) == True


def test_one_long_type():
    assert isinstance(converters.boolean(1L), bool)


def test_one_string():
    assert converters.boolean('1') == True


def test_one_string_type():
    assert isinstance(converters.boolean('1'), bool)


def test_one_unicode_string():
    assert converters.boolean(u'1') == True


def test_one_unicode_string_type():
    assert isinstance(converters.boolean(u'1'), bool)


def test_zero_string():
    assert converters.boolean('0') == False


def test_zero_string_type():
    assert isinstance(converters.boolean('0'), bool)


def test_zero_unicode_string():
    assert converters.boolean(u'0') == False


def test_zero_unicode_string_type():
    assert isinstance(converters.boolean(u'0'), bool)


def test_positive_number_string():
    with pytest.raises(exc.ConvertationError):
        converters.boolean('2')


def test_negative_number_string():
    with pytest.raises(exc.ConvertationError):
        converters.boolean('-1')


def test_positive_number_unicode_string():
    with pytest.raises(exc.ConvertationError):
        converters.boolean(u'2')


def test_negative_number_unicode_string():
    with pytest.raises(exc.ConvertationError):
        converters.boolean(u'-1')


def test_not_number_string():
    with pytest.raises(exc.ConvertationError):
        converters.boolean('a')


def test_empty_string():
    with pytest.raises(exc.ConvertationError):
        converters.boolean('')


def test_none():
    with pytest.raises(exc.ConvertationError):
        converters.boolean(None)


def test_boolean_true():
    assert converters.boolean(True) == True


def test_boolean_true_type():
    assert isinstance(converters.boolean(True), bool)


def test_boolean_false():
    assert converters.boolean(False) == False


def test_boolean_false_type():
    assert isinstance(converters.boolean(False), bool)


def test_unknown_type():
    with pytest.raises(exc.ConvertationError):
        converters.boolean(type)
