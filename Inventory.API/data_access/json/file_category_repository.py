import os
import json
from typing import List, Optional
from uuid import UUID

from application.interfaces.category_repository import CategoryRepository
from domain.entities.category import Category
from domain.entities.attribute import Attribute
from domain.value_objects.attribute_type import get_attribute_type


class FileCategoryRepository(CategoryRepository):
    def __init__(self):
        self.file_path = "categories.json"
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)
        self.categories = self._load_categories()

    def _load_categories(self) -> List[Category]:
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [self._dict_to_category(cat_dict) for cat_dict in data]

    def _save_categories(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([category.to_dict() for category in self.categories], f, indent=4)

    def _dict_to_category(self, data: dict) -> Category:
        attributes = []
        for attr in data.get("attributes", []):
            attribute = Attribute(
                id=UUID(attr.get("id")),
                name=attr.get("name"),
                type=get_attribute_type(attr.get("type")),
            )
            attributes.append(attribute)
        return Category(
            id=UUID(data.get("id")),
            name=data.get("name", ""),
            description=data.get("description"),
            attributes=attributes,
        )

    def get_all(self) -> List[Category]:
        return self.categories

    def get(self, category_id: UUID) -> Optional[Category]:
        for category in self.categories:
            if category.id == category_id:
                return category
        return None

    def add(self, category: Category) -> Category:
        self.categories.append(category)
        self._save_categories()
        return category

    def update(self, category: Category) -> Optional[Category]:
        for idx, cat in enumerate(self.categories):
            if cat.id == category.id:
                self.categories[idx] = category
                self._save_categories()
                return category
        return None

    def delete(self, category: Category) -> Optional[Category]:
        for idx, cat in enumerate(self.categories):
            if cat.id == category.id:
                removed_category = self.categories.pop(idx)
                self._save_categories()
                return removed_category
        return None
