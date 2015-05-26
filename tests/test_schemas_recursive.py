from __future__ import absolute_import

import pytest

import schematec.schema
import schematec.converters as converters
import schematec.validators as validators
import schematec.exc as exc


def test_list_in_list():
    schema = schematec.schema.array(schematec.schema.array(converters.string))
    assert schema([[1, 2], [3, 4]]) == [['1', '2'], ['3', '4']]


def test_list_in_dict():
    schema = schematec.schema.dictionary(
        a=schematec.schema.array(converters.string),
    )
    assert schema({'a': [1, 2]}) == {'a': ['1', '2']}


def test_list_in_dict_required():
    schema = schematec.schema.dictionary(
        a=schematec.schema.array(converters.string) & validators.required,
    )
    with pytest.raises(exc.ValidationError):
        schema({'b': [1, 2]})


def test_dict_in_dict():
    schema = schematec.schema.dictionary(
        a=schematec.schema.dictionary(
            b=converters.string,
        ),
    )
    assert schema({'a': {'b': 1}}) == {'a': {'b': '1'}}


def test_dict_in_dict_required():
    schema = schematec.schema.dictionary(
        a=schematec.schema.dictionary(
            b=converters.string & validators.required,
        ),
    )
    with pytest.raises(exc.ValidationError):
        schema({'a': {'c': 1}})


def test_dict_in_list():
    schema = schematec.schema.array(schematec.schema.dictionary(
        a=converters.string,
    ))
    assert schema([{'a': 1}, {'a': 2}]) == [{'a': '1'}, {'a': '2'}]
