from __future__ import absolute_import

import pytest

import schematec.converters as converters
import schematec.exc as exc


def test_zero():
    assert converters.string(0) == u'0'


def test_long():
    assert converters.string(1L) == u'1'


def test_long_type():
    assert isinstance(converters.string(1L), unicode)


def test_positive_number_string():
    assert converters.string('1') == u'1'


def test_positive_number_string_type():
    assert isinstance(converters.string('1'), unicode)


def test_positive_number_unicode_string():
    assert converters.string(u'1') == u'1'


def test_positive_number_unicode_string_type():
    assert isinstance(converters.string(u'1'), unicode)


def test_none():
    with pytest.raises(exc.ConvertationError):
        converters.string(None)


def test_boolean_true():
    with pytest.raises(exc.ConvertationError):
        converters.string(True)


def test_boolean_false():
    with pytest.raises(exc.ConvertationError):
        converters.string(False)
