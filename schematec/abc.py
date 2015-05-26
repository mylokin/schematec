from __future__ import absolute_import


class IDescriptor(object):
    def has_sugar_descriptors(self):
        return hasattr(self, '_sugar_descriptors')

    def get_sugar_descriptors(self):
        return self._sugar_descriptors

    def __and__(self, other):
        if not self.has_sugar_descriptors():
            self._sugar_descriptors = [other]

        self._sugar_descriptors.append(other)
        return self


class Schema(IDescriptor):
    pass


class Converter(IDescriptor):
    pass


class Validator(IDescriptor):
    BINDING = None
