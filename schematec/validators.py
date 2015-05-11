from __future__ import absolute_import

import schematec.exc as exc


class Validator(object):
    BINDING = None


class Required(Validator):
    def __call__(self, name, data):
        if name not in data:
            raise exc.ValidationError(name)

required = Required()
