from dataclasses import dataclass
from typing import Optional


@dataclass
class Value:
    id: Optional[int] = None
    attribute_definition_id: int = 0
    value: str = ""
