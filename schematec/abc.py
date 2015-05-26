from __future__ import absolute_import


class AbstractDescriptor(object):
    def has_sugar_descriptors(self):
        return hasattr(self, '_sugar_descriptors')

    def get_sugar_descriptors(self):
        return self._sugar_descriptors

    def __and__(self, other):
        if not self.has_sugar_descriptors():
            self._sugar_descriptors = [other]

        self._sugar_descriptors.append(other)
        return self


class Schema(AbstractDescriptor):
    pass


class Converter(AbstractDescriptor):
    pass


class Validator(AbstractDescriptor):
    BINDING = None
