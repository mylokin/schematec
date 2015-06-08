from __future__ import absolute_import

import pytest

import schematec.schema
import schematec.abc as abc
import schematec.exc as exc
import schematec.converters as converters
import schematec.validators as validators


def test_empty_dict():
    schema = schematec.schema.expand({})
    assert isinstance(schema, schematec.schema.Dictionary)


def test_empty_list():
    schema = schematec.schema.expand([])
    assert isinstance(schema, schematec.schema.Array)


def test_tuple():
    with pytest.raises(exc.SchemaError):
        schematec.schema.expand(())


def test_integer():
    with pytest.raises(exc.SchemaError):
        schematec.schema.expand(1)


def test_flat_dict_descriptor():
    schema = {
        'a': converters.integer,
    }
    schema = schematec.schema.expand(schema)
    assert isinstance(schema.descriptors['a'], abc.Converter)


def test_flat_dict_complex_descriptor():
    schema = {
        'a': converters.integer & validators.required,
    }
    schema = schematec.schema.expand(schema)
    assert len(schema.descriptors['a'].descriptors) == 2


def test_traversal():
    schema = {
        'a': [{
            'b': converters.integer,
        }]
    }
    schema = schematec.schema.expand(schema)
    assert isinstance(schema.descriptors['a'].descriptors[0].descriptors['b'], abc.Converter)
