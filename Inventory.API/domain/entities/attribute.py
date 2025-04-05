from typing import Optional
from uuid import UUID
from domain.value_objects.attribute_type import AttributeType
from domain.entities.entity import Entity


class Attribute(Entity):
    name: str
    type: AttributeType

    def __init__(self, id: Optional[UUID], name: str, type: AttributeType):
        super().__init__(id)
        self.name = name
        self.type = type

    @classmethod
    def create(cls, name: str, type: AttributeType) -> "Attribute":
        return cls(id=None, name=name, type=type)

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update(
            {
                "name": self.name,
                "type": self.type.value,
            }
        )
        return base
