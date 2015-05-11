'''
Schematec
=========

Schematec is a set of tools that brings some static typing into Python and
makes input data validation easier. The purpose of this code is attempt to
bring simplicity to applications logics using separation of data validation
and actual data processing.

Concepts
--------

Schematec separates concept of validation and concept of types casting.

Object deconstruction seems reasonable useful for input data filtering.

Workflow
--------

Schematec determine validity of data using following criterias:

# Existence (schema validator)
# Type (converter)
# Suitability (validator)

Example::

   a = string and email and required

   ### Cases

   {'a': 'mylokin@me.com'}  # valid
   {'a': 'mylokin'}  # invalid by suitability
   {'a': ''}  # invalid by suitability
   {'a': 1}  # invalid by suitability
   {'a': None}  # invalid by type
   {'a': []}  # invalid by type
   {}  # invalid by existence

   a = string and email

   ### Cases

   {'a': 'mylokin@me.com'}  # valid
   {'a': 'mylokin'}  # invalid by suitability
   {'a': ''}  # invalid by suitability
   {'a': 1}  # invalid by suitability
   {'a': None}  # invalid by type
   {'a': []}  # invalid by type
   {}  # valid

   a = string

   ### Cases

   {'a': 'mylokin@me.com'}  # valid
   {'a': 'mylokin'}  # valid
   {'a': ''}  # valid
   {'a': 1}  # valid
   {'a': None}  # invalid by type
   {'a': []}  # invalid by type
   {}  # valid


Glossary
========

Validator

   Configurable object that checks object for predefined conditions.

Converter

   Converter casts input object to required type if possible.

Schema

   Set of validators

Validation

   Checking process where every value validated through set of validators.

Validators
==========

Required -- any

   Required value, (everything is optional by default).

Regex (URL, Email, IPAddress) -- string

    String contains expected value.

Range -- integer

    Integer within range

Length -- string, array, dictionary

    Length of iteratable is appropriate.

Supported Data Types
====================

Schematec supports subset of JSON data types:

Basic types:
- numeric(int)
- string(str)
- boolean(bool)

Containers:
- array(list)
- dictionary(dict)

Extended Data Types
===================

- datetime - based on str
- regexp str - based on str

Order of schema check
=====================

#. Unbound Validators
#. Converters
#. Bound Validators

Current Developments
====================

WTForms
-------
::

   class MyForm(Form):
       name    = StringField(u'Full Name', [validators.required(), validators.length(max=10)])
       address = TextAreaField(u'Mailing Address', [validators.optional(), validators.length(max=200)])

WTForms uses lists of validators. That approach helps to separate validators
from converters. `Source code <https://github.com/wtforms/wtforms/blob/master/wtforms/validators.py>`_.

::

   def __init__(self, fieldname, message=None):
       self.fieldname = fieldname
       self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)

Validators are simple objects. ``__init__`` method provides a way to configure validator.
``__call__`` method provides a way to process validation.

Validation is bound to forms objects. This has been made to provide ``EqualTo``
functionality. Reflects connections between form fields.

WTForms users ``ValidationError`` and ``StopValidation`` exceptions.
``ValidationError`` is used for errors forwarding.
``StopValidation`` is used to skip steps. Thus some validation steps could be optional.


scheme
------

Scheme `provides <https://github.com/arterial-io/scheme/tree/master/scheme/fields>`_
wide range of different types validators. It extracts types conversion into
serializers/deserializers.

django-data-schema
------------------

Module `implements <https://github.com/ambitioninc/django-data-schema/blob/develop/data_schema/convert_value.py>`_
data converters.


API Examples
============

::



'''

__version__ = '0.1.0'
