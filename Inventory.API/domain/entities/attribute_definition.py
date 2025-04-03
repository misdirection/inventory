from dataclasses import dataclass
from typing import Optional, Any


from ..value_objects.attribute_type import AttributeType


@dataclass
class AttributeDefinition:
    id: Optional[int] = None
    name: str = ""
    type: AttributeType = AttributeType.STRING
    options: Optional[Any] = None
