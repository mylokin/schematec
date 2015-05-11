from __future__ import absolute_import

import schematec.converters as converters
import schematec.validators as validators


class Schema(object):
    '''
    Converters is appliyed first in orderder they defined
    Validators is appliyed second.
    '''

    def __init__(self, **descriptors):
        self.descriptors = descriptors

    def __call__(self, data):
        result = {}
        for name, descriptors in self.descriptors.items():
            unbound_validators = [v for v in descriptors if isinstance(v, validators.Validator) and not v.BINDING]
            for validator in unbound_validators:
                validator(name, data)
            try:
                value = data[name]
            except KeyError:
                continue
            converters = [c for c in descriptors if isinstance(c, converters.Converter)]
            for converter in converters:
                value = converter(value)
            bound_validators = [v for v in descriptors if isinstance(v, Validators.validators) and v.BINDING]
            for validator in bound_validators:
                validator(value)
            result[name] = value
        return name
