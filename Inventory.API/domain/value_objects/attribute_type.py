from enum import Enum


class AttributeType(Enum):
    """
    Enum representing the type of an attribute.
    """

    STRING = "string"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    FLOAT = "float"
    DATE = "date"
    TIME = "time"
    DATETIME = "datetime"
    LIST = "list"
    DICT = "dict"
    REFERENCE = "reference"
