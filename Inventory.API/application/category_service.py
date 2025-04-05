from typing import Optional
from uuid import UUID
from domain.entities.attribute import Attribute
from application.interfaces.category_repository import CategoryRepository
from domain.entities.category import Category
from domain.value_objects.attribute_type import get_attribute_type


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def get_all(self) -> list[Category]:
        return self.category_repository.get_all()

    def get(self, category_id: UUID) -> Optional[Category]:
        return self.category_repository.get(category_id)

    def create(self, name: str, description: str) -> Category:
        new_category = Category.create(name=name, description=description)

        return self.category_repository.add(new_category)

    def update(
        self, id: UUID, name: Optional[str], description: Optional[str]
    ) -> Optional[Category]:
        category = self.category_repository.get(id)

        if category is None:
            return None

        if name is not None:
            category.name = name
        if description is not None:
            category.description = description

        return self.category_repository.update(category)

    def delete(self, id: UUID) -> Optional[Category]:
        category = self.category_repository.get(id)

        if category is None:
            return None

        return self.category_repository.delete(category)

    def add_attribute(
        self, category_id: UUID, name: str, attribute_type: str
    ) -> Optional[Category]:
        category = self.category_repository.get(category_id)
        if category is None:
            return None

        new_attribute = Attribute.create(
            name=name, type=get_attribute_type(attribute_type)
        )

        category.add_attribute(new_attribute)
        self.category_repository.update(category)

        return new_attribute
