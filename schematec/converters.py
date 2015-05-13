'''
Convertaion rules
=================

Can be converted into:

integer
-------

#. Any int or long value
#. Any suitable string/unicode
#. Boolean value

number
-------

#. Any float or int or long value
#. Any suitable string/unicode
#. Boolean value

string
------

#. Any suitable string/unicode
#. Any int or long value

boolean
-------

#. Boolean value
#. 0 or 1
#. '0' or '1'
#. u'0' or u'1'

array
-----

#. Any iterable value(collections.Iterable)

dictionary
----------

#. Any mapping value(collections.Mapping)


'''
from __future__ import absolute_import

import collections

import schematec.exc as exc


class Converter(object):
    pass


class Integer(Converter):
    def __call__(self, value):
        if value is None:
            raise exc.ConvertationError(value)

        if isinstance(value, bool):
            return int(value)

        if isinstance(value, (int, long)):
            return int(value)

        if isinstance(value, basestring):
            try:
                return int(value)
            except ValueError:
                raise exc.ConvertationError(value)

        raise exc.ConvertationError(value)

integer = Integer()


class Number(Converter):
    def __call__(self, value):
        if value is None:
            raise exc.ConvertationError(value)

        if isinstance(value, bool):
            return float(value)

        if isinstance(value, (float, int, long)):
            return float(value)

        if isinstance(value, basestring):
            try:
                return float(value)
            except ValueError:
                raise exc.ConvertationError(value)

        raise exc.ConvertationError(value)

number = Number()


class String(Converter):
    def __call__(self, value):
        if value is None:
            raise exc.ConvertationError(value)

        if isinstance(value, unicode):
            return value

        if isinstance(value, bool):
            raise exc.ConvertationError(value)

        if isinstance(value, (int, long)):
            return unicode(value)

        if isinstance(value, str):
            try:
                return unicode(value)
            except UnicodeDecodeError:
                raise exc.ConvertationError(value)

        raise exc.ConvertationError(value)

string = String()


class Boolean(Converter):
    def __call__(self, value):
        if value is None:
            raise exc.ConvertationError(value)

        if isinstance(value, bool):
            return value

        if isinstance(value, (int, long)) and value in (0, 1):
            return bool(value)

        if isinstance(value, basestring) and value in (u'0', u'1'):
            return bool(int(value))

        raise exc.ConvertationError(value)

boolean = Boolean()


class Array(Converter):
    TYPE = collections.Iterable

    def __call__(self, value):
        if isinstance(value, self.TYPE):
            return list(value)

        raise exc.ConvertationError(value)

array = Array()


class Dictionary(Converter):
    TYPE = collections.Mapping

    def __call__(self, value):
        if isinstance(value, self.TYPE):
            return dict(value)

        raise exc.ConvertationError(value)

dictionary = Dictionary()
