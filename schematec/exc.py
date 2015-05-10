class SchematecError(Exception):
    pass


class SchemaError(SchematecError):
    pass


class ConvertationError(SchematecError):
    pass


class ValidationError(SchematecError):
    pass
