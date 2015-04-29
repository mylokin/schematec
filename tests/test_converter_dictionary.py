from __future__ import absolute_import

import pytest

import schematec.converters as converters
import schematec.exc as exc


def test_none():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary(None)


def test_empty_list():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary([])


def test_empty_tuple():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary(())


def test_empty_dict():
    assert converters.dictionary({}) == {}


def test_empty_str():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary('')


def test_empty_unicode():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary(u'')


def test_full_list():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary([0, 1, '0', '1', [], {}])


def test_full_tuple():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary((0, 1, '0', '1', [], {}))


def test_full_dict():
    assert converters.dictionary({0: '0', 1: '1'}) == {0: '0', 1: '1'}


def test_full_str():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary('0')


def test_full_unicode():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary(u'0')


def test_int():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary(0)


def test_generator():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary((x for x in xrange(5)))


def test_list_comprehention():
    with pytest.raises(exc.ConvertationError):
        converters.dictionary([x for x in xrange(5)])


def test_object():
    class Object(object):
        pass

    with pytest.raises(exc.ConvertationError):
        converters.dictionary(Object())
