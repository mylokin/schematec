from __future__ import absolute_import

import pytest

import schematec.schema
import schematec.converters as converters
import schematec.validators as validators
import schematec.exc as exc


def test_empty_schema_with_empty_value():
    schema = schematec.schema.dictionary()
    assert schema({}) == {}


def test_empty_schema_with_non_empty_value():
    schema = schematec.schema.dictionary()
    assert schema({'a': 1}) == {'a': 1}


def test_schema_with_missed_keys():
    schema = schematec.schema.dictionary(
        a=[converters.string]
    )
    assert schema({'b': 1}) == {}


def test_integer_to_string_converter():
    schema = schematec.schema.dictionary(
        a=[converters.string]
    )
    assert schema({'a': 1}) == {'a': '1'}


def test_integer_to_integer_converter():
    schema = schematec.schema.dictionary(
        a=[converters.integer]
    )
    assert schema({'a': 1}) == {'a': 1}


def test_unbound_validator_required():
    schema = schematec.schema.dictionary(
        a=[validators.required, converters.integer]
    )
    assert schema({'a': '1'}) == {'a': 1}


def test_unbound_validator_required_for_missed_value():
    schema = schematec.schema.dictionary(
        a=[validators.required, converters.integer]
    )
    with pytest.raises(exc.ValidationError):
        schema({})


def test_unbound_validator_required_without_converter():
    schema = schematec.schema.dictionary(
        a=[validators.required]
    )
    assert schema({'a': 1}) == {'a': 1}


def test_unbound_validator_required_for_missed_without_converter():
    schema = schematec.schema.dictionary(
        a=[validators.required]
    )
    with pytest.raises(exc.ValidationError):
        schema({})


def test_bound_validator_skipped():
    schema = schematec.schema.dictionary(
        a=[validators.length(3)]
    )
    assert schema({'a': 1}) == {'a': 1}


def test_bound_validator():
    schema = schematec.schema.dictionary(
        a=[validators.length(3)]
    )
    assert schema({'a': '1'}) == {'a': '1'}


def test_bound_validator_error():
    schema = schematec.schema.dictionary(
        a=[validators.length(3)]
    )
    with pytest.raises(exc.ValidationError):
        schema({'a': '1234'})


def test_schema_with_converters_and_validators():
    schema = schematec.schema.dictionary(
        a=[validators.required, converters.string, validators.length(3)]
    )

    assert schema({'a': 123}) == {'a': '123'}


def test_schema_with_converters_and_validators_fail_on_required():
    schema = schematec.schema.dictionary(
        a=[validators.required, converters.string, validators.length(3)]
    )

    with pytest.raises(exc.ValidationError):
        schema({'b': 123})


def test_schema_with_converters_and_validators_fail_on_convertation():
    schema = schematec.schema.dictionary(
        a=[validators.required, converters.string, validators.length(3)]
    )

    with pytest.raises(exc.ConvertationError):
        schema({'a': None})


def test_schema_with_converters_and_validators_fail_on_length():
    schema = schematec.schema.dictionary(
        a=[validators.required, converters.string, validators.length(3)]
    )

    with pytest.raises(exc.ValidationError):
        schema({'a': '1234'})
