from __future__ import absolute_import

import schematec.abc as abc


class Dictionary(object):
    '''
    Unbound validators is appliyed first.
    Converters is appliyed second in orderder they defined
    Bound validators is appliyed third.
    '''

    def __init__(self, **descriptors):
        self.descriptors = descriptors

    def __call__(self, data):
        result = {}
        for name, descriptors in self.descriptors.items():
            unbound_validators = [v for v in descriptors if
                                  isinstance(v, abc.Validator) and not v.BINDING]
            for validator in unbound_validators:
                validator(name, data)
            try:
                value = data[name]
            except KeyError:
                continue
            converters = [c for c in descriptors if isinstance(c, abc.Converter)]
            for converter in converters:
                value = converter(value)
            bound_validators = [v for v in descriptors if isinstance(v, abc.Validator) and v.BINDING]
            for validator in bound_validators:
                if isinstance(value, validator.BINDING):
                    validator(value)
            result[name] = value
        return result


dictionary = Dictionary
