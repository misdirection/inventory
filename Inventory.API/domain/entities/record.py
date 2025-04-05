from dataclasses import field
from typing import List, Optional
from domain.entities.value import Value


class Record:
    id: Optional[int] = None
    category_id: int = 0
    values: List[Value] = field(default_factory=list)
