from abc import ABC
from uuid import UUID, uuid4
from typing import Optional


class Entity(ABC):
    id: UUID

    def __init__(self, id: Optional[UUID]):
        self.id = id if id is not None else uuid4()

    def to_dict(self) -> dict:
        return {"id": str(self.id)}
