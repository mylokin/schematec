from __future__ import absolute_import

import schematec.exc as exc


def numeric(value):
    if isinstance(value, bool):
        return int(value)

    if isinstance(value, (int, long)):
        return int(value)

    if isinstance(value, basestring):
        try:
            return int(value)
        except ValueError:
            raise exc.ConvertationError(value)

    if value is None:
        raise exc.ConvertationError(value)

    raise exc.ConvertationError(value)


def string(value):
    pass


def boolean(value):
    pass


def array(value):
    pass


def dictionary(value):
    pass
