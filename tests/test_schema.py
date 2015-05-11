from __future__ import absolute_import

# import pytest

import schematec.schema
# import schematec.converters as converters
# import schematec.validators as validators
# import schematec.exc as exc


def test_empty_schema_with_empty_value():
    schema = schematec.schema.Schema()
    assert schema({}) == {}
