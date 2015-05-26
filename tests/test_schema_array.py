from __future__ import absolute_import

import pytest

import schematec.schema
import schematec.converters as converters
import schematec.validators as validators
import schematec.exc as exc


def test_empty_schema_with_empty_value():
    schema = schematec.schema.array()
    assert schema([]) == []


def test_empty_schema_with_non_empty_value():
    schema = schematec.schema.array()
    assert schema([1]) == [1]


def test_schema_with_missed_keys():
    schema = schematec.schema.array(converters.string)
    assert schema([1]) == ['1']


def test_integer_to_string_converter():
    schema = schematec.schema.array(converters.string)
    assert schema([1]) == ['1']


def test_integer_to_integer_converter():
    schema = schematec.schema.array(converters.integer)
    assert schema([1]) == [1]


def test_bound_validator_skipped():
    schema = schematec.schema.array(validators.length(3))
    assert schema([1]) == [1]


def test_bound_validator():
    schema = schematec.schema.array(validators.length(3))
    assert schema(['1']) == ['1']


def test_bound_validator_error():
    schema = schematec.schema.array(validators.length(3))
    with pytest.raises(exc.ValidationError):
        schema(['1234'])


def test_schema_with_converters_and_validators():
    schema = schematec.schema.array(converters.string & validators.length(3))

    assert schema([123]) == ['123']


def test_schema_with_converters_and_validators_fail_on_convertation():
    schema = schematec.schema.array(converters.string & validators.length(3))

    with pytest.raises(exc.ConvertationError):
        schema([None])


def test_schema_with_converters_and_validators_fail_on_length():
    schema = schematec.schema.array(converters.string & validators.length(3))

    with pytest.raises(exc.ValidationError):
        schema(['1234'])


def test_schema_with_converters_and_validators_fail_on_length_for_various_values():
    schema = schematec.schema.array(converters.string & validators.length(3))

    with pytest.raises(exc.ValidationError):
        schema(['123', '1234'])
