from typing import List, Optional
from uuid import UUID
from domain.entities.attribute import Attribute
from domain.entities.entity import Entity


class Category(Entity):
    name: str
    description: Optional[str]
    attributes: List[Attribute]

    def __init__(
        self,
        id: Optional[UUID],
        name: str,
        description: Optional[str],
        attributes: List[Attribute],
    ):
        super().__init__(id)
        self.name = name
        self.description = description
        self.attributes = attributes

    @classmethod
    def create(cls, name: str, description: Optional[str] = None) -> "Category":
        return cls(id=None, name=name, description=description, attributes=[])

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update(
            {
                "name": self.name,
                "description": self.description,
                "attributes": [attr.to_dict() for attr in self.attributes],
            }
        )
        return base

    def add_attribute(self, attribute: Attribute) -> None:
        self.attributes.append(attribute)
