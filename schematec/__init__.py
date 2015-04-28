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

Glossary
========

Validator

   Object that provides state of processed object. Is it suitable or not.

Converter

   Converter casts input object to required type if possible.

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

'''

__version__ = '0.1.0'
