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


def get_attribute_type(attribute_type: str) -> AttributeType:
    """
    Get the AttributeType enum value from a string.

    Args:
        attribute_type (str): The string representation of the attribute type.

    Returns:
        AttributeType: The corresponding AttributeType enum value.
    """
    try:
        return AttributeType[attribute_type.upper()]
    except KeyError:
        raise ValueError(f"Invalid attribute type: {attribute_type}")
