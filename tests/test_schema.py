from __future__ import absolute_import

import pytest

import schematec.schema
import schematec.converters as converters
import schematec.validators as validators
import schematec.exc as exc


def test_empty_schema_with_empty_value():
    schema = schematec.schema.Schema()
    assert schema({}) == {}


def test_empty_schema_with_non_empty_value():
    schema = schematec.schema.Schema()
    assert schema({'a': 1}) == {}


def test_numeric_to_string_converter():
    schema = schematec.schema.Schema(
        a=[converters.string]
    )
    assert schema({'a': 1}) == {'a': '1'}


def test_numeric_to_numeric_converter():
    schema = schematec.schema.Schema(
        a=[converters.numeric]
    )
    assert schema({'a': 1}) == {'a': 1}


def test_unbound_validator_required():
    schema = schematec.schema.Schema(
        a=[validators.required, converters.numeric]
    )
    assert schema({'a': '1'}) == {'a': 1}


def test_unbound_validator_required_for_missed_value():
    schema = schematec.schema.Schema(
        a=[validators.required, converters.numeric]
    )
    with pytest.raises(exc.ValidationError):
        schema({})


def test_unbound_validator_required_without_converter():
    schema = schematec.schema.Schema(
        a=[validators.required]
    )
    assert schema({'a': 1}) == {'a': 1}


def test_unbound_validator_required_for_missed_without_converter():
    schema = schematec.schema.Schema(
        a=[validators.required]
    )
    with pytest.raises(exc.ValidationError):
        schema({})
