from typing import Optional
from application.interfaces.category_repository import CategoryRepository
from domain.entities.category import Category


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def get_all_categories(self) -> list[Category]:
        return self.category_repository.get_all_categories()

    def get_category_by_id(self, category_id) -> Optional[Category]:
        return self.category_repository.get_category_by_id(category_id)

    def create_category(self, category_data) -> Category:
        new_category = Category(
            name=category_data.get("name"),
            description=category_data.get("description"),
        )
        print(f"Creating category: {new_category}")
        return self.category_repository.create_category(new_category)

    def update_category(self, id: int, updated_data: dict) -> Optional[Category]:
        return self.category_repository.update_category(id, updated_data)
