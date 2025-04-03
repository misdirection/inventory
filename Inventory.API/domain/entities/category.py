from dataclasses import dataclass, field
from typing import List, Optional
from .attribute_definition import AttributeDefinition


@dataclass
class Category:
    id: Optional[int] = None
    name: str = ""
    description: Optional[str] = None
    attributes: List[AttributeDefinition] = field(default_factory=list)
