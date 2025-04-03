import os
import json
from typing import List, Optional
from dataclasses import asdict

from application.interfaces.category_repository import CategoryRepository
from domain.entities.category import Category
from domain.entities.attribute_definition import AttributeDefinition


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
            json.dump([asdict(category) for category in self.categories], f, indent=4)

    def _dict_to_category(self, data: dict) -> Category:
        attributes = []
        for attr in data.get("attributes", []):
            # Erzeuge ein AttributeDefinition-Objekt aus dem Dictionary
            attribute = AttributeDefinition(**attr)
            attributes.append(attribute)
        return Category(
            id=data.get("id"),
            name=data.get("name", ""),
            description=data.get("description"),
            attributes=attributes,
        )

    def get_all_categories(self) -> List[Category]:
        return self.categories

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        for category in self.categories:
            if category.id == category_id:
                return category
        return None

    def create_category(self, category: Category) -> Category:
        if category.id is None:
            if self.categories:
                max_id = max(cat.id for cat in self.categories if cat.id is not None)
                category.id = max_id + 1
            else:
                category.id = 1
        self.categories.append(category)
        self._save_categories()
        return category

    def update_category(
        self, category_id: int, updated_data: dict
    ) -> Optional[Category]:
        category = self.get_category_by_id(category_id)
        if category is None:
            return None

        for key, value in updated_data.items():
            setattr(category, key, value)

        self._save_categories()
        return category
