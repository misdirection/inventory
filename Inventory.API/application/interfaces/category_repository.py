from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.category import Category
from typing import Optional


class CategoryRepository(ABC):
    """
    Abstract base class for the Category repository.
    This class defines the interface for interacting with category data.
    """

    @abstractmethod
    def get_all(self) -> list[Category]:
        """
        Retrieve all categories.

        Returns:
            list: A list of all categories.
        """
        pass

    @abstractmethod
    def get(self, category_id: UUID) -> Optional[Category]:
        """
        Retrieve a category by its ID.

        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            dict: The category with the specified ID.
        """
        pass

    @abstractmethod
    def add(self, category: Category) -> Category:
        """
        Create a new category.
        Args:
            category (Category): The category object to create.
            Returns:
                Category: The created category.
        """
        pass

    @abstractmethod
    def update(self, category: Category) -> Optional[Category]:
        """
        Update an existing category.

        Args:
            category_id (int): The ID of the category to update.
            updated_data (dict): The data to update the category with.

        Returns:
            Optional[Category]: The updated category, or None if not found.
        """
        pass

    @abstractmethod
    def delete(self, category: Category) -> Optional[Category]:
        """
        Delete a category.

        Args:
            category (Category): The category object to delete.

        Returns:
            Optional[Category]: The deleted category, or None if not found.
        """
        pass
