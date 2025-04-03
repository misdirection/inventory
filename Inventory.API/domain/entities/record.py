from dataclasses import dataclass, field
from typing import List, Optional
from value import Value


@dataclass
class Record:
    id: Optional[int] = None
    category_id: int = 0
    values: List[Value] = field(default_factory=list)
