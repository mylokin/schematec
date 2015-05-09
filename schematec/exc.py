class SchematecError(Exception):
    pass


class SchemaError(SchematecError):
    pass


class ConvertationError(SchematecError):
    pass
