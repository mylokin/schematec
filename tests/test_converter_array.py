from __future__ import absolute_import

import pytest

import schematec.converters as converters
import schematec.exc as exc


def test_empty_list():
    assert converters.array([]) == []


def test_empty_tuple():
    assert converters.array(()) == []


def test_empty_dict():
    assert converters.array({}) == []


def test_empty_str():
    assert converters.array('') == []


def test_empty_unicode():
    assert converters.array(u'') == []


def test_full_list():
    assert converters.array([0, 1, '0', '1', [], {}]) == [0, 1, '0', '1', [], {}]


def test_full_tuple():
    assert converters.array((0, 1, '0', '1', [], {})) == [0, 1, '0', '1', [], {}]


def test_full_dict():
    assert converters.array({0: '0', 1: '1'}) == [0, 1]


def test_full_str():
    assert converters.array('0') == ['0']


def test_full_unicode():
    assert converters.array(u'0') == [u'0']


def test_int():
    with pytest.raises(exc.ConvertationError):
        converters.array(0)


def test_generator():
    assert converters.array((x for x in xrange(5))) == [0, 1, 2, 3, 4]


def test_list_comprehention():
    assert converters.array([x for x in xrange(5)]) == [0, 1, 2, 3, 4]


def test_object():
    class Object(object):
        pass

    with pytest.raises(exc.ConvertationError):
        converters.array(Object())
