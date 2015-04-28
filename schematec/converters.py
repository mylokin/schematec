from __future__ import absolute_import

import schematec.exc as exc


def numeric(value):
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


def string(value):
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


def boolean(value):
    if value is None:
        raise exc.ConvertationError(value)

    if isinstance(value, bool):
        return value

    if isinstance(value, (int, long)) and value in (0, 1):
        return bool(value)

    if isinstance(value, basestring) and value in (u'0', u'1'):
        return bool(int(value))

    raise exc.ConvertationError(value)


def array(value):
    pass


def dictionary(value):
    pass
