Schematec
=========

.. image:: https://travis-ci.org/mylokin/redisext.svg?branch=master
   :target: https://travis-ci.org/mylokin/redisext

Schematec is a set of tools that makes input data validation easier.
The purpose of this code is attempt to bring simplicity to applications
logics using separation of data validation and actual data processing.

Quickstart
----------

.. code:: python

   import schematec as s

   schema = s.dictionary(
      id=[s.integer, s.required],
      name=s.string,
      tags=s.array(s.string),
   )

.. code:: python

   >>> data = {
   ...     'id': '1',
   ...     'name': 'Red Hot Chili Peppers',
   ...     'tags': ['funk', 'rock'],
   ...     'rank': '1',
   ... }
   >>> schema(data)
   {'id': 1, 'name': u'Red Hot Chili Peppers', 'tags': [u'funk', u'rock']}


Concepts
--------

Schematec module is based on three basic concepts:

* Schema
* Validator
* Converter

Schema
^^^^^^

Term "schema" is used to describe complex data struct such as dictionary(hashmap)
or array(list). Schemas has two different types of validation (it is not related to
array schemas):

* Strict - requires all values
* Non-strict - tolerate to missed values

`schematec.exc.SchemaError` is raised in case provided data is incorrect.

Order of schema validations:

#. Unbound Validators
#. Schemas(inner)
#. Converters
#. Bound Validators

Validator
^^^^^^^^^

Term "validator" describes callable objects that perform different types of checks.
There are two types of validators in schematec:

* Bound - type related, for example "max length" validator is bound to sized type.
* Unbound - universal, for example "required" validator.

Converter
^^^^^^^^^

Term "converter" is used to describe cast functions. Schematec supports subset of JSON
data types.

Basic types:

- integer(int)
- string(str)
- boolean(bool)

Containers:

- array(list)
- dictionary(dict)
