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


def test_positive_number_string():
    assert converters.numeric('1') == 1


def test_negative_number_string():
    assert converters.numeric('-1') == -1


def test_positive_number_unicode_string():
    assert converters.numeric(u'1') == 1


def test_negative_number_unicode_string():
    assert converters.numeric(u'-1') == -1


def test_none():
    with pytest.raises(exc.ConvertationError):
        converters.numeric(None)


def test_true():
    assert converters.numeric(True) == 1


def test_false():
    assert converters.numeric(False) == 0
