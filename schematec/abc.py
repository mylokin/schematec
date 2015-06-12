from __future__ import absolute_import

import collections


class Descriptor(object):
    pass


class ComplexDescriptor(Descriptor, collections.Sequence):
    def __init__(self, *descriptors):
        self.descriptors = list(descriptors)

    def __and__(self, descriptor):
        if not isinstance(descriptor, AbstractDescriptor):
            raise TypeError(descriptor)

        self.descriptors.append(descriptor)
        return self

    def __getitem__(self, index):
        return self.descriptors[index]

    def __len__(self):
        return len(self.descriptors)


class AbstractDescriptor(Descriptor):
    def __init__(self):
        pass

    def __call__(self, *args, **kw):
        raise NotImplementedError

    def __and__(self, descriptor):
        if not isinstance(descriptor, AbstractDescriptor):
            raise TypeError(descriptor)

        return ComplexDescriptor(self, descriptor)


class Schema(AbstractDescriptor):
    pass


class Converter(AbstractDescriptor):
    pass


class Validator(AbstractDescriptor):
    BINDING = None
