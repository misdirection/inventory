"""
Use this module to register required services.
Services registered inside a `rodi.Container` are automatically injected into request
handlers.

For more information and documentation, see `rodi` Wiki and examples:
    https://github.com/Neoteroi/rodi/wiki
    https://github.com/Neoteroi/rodi/tree/main/examples
"""

from typing import Tuple

from rodi import Container

from api.settings import Settings, load_settings
from application.interfaces.category_repository import CategoryRepository
from data_access.json.file_category_repository import FileCategoryRepository
from application.category_service import CategoryService


def configure_services() -> Tuple[Container, Settings]:
    container = Container()
    settings = load_settings()

    container.add_instance(settings)
    container.add_scoped(CategoryRepository, FileCategoryRepository)

    container.add_scoped(CategoryService)
    return container, settings
