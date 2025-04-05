from dataclasses import dataclass
from typing import Optional
from uuid import UUID
from blacksheep import Response
from blacksheep.server.controllers import Controller, post, get, patch
from application.category_service import CategoryService
from domain.value_objects.attribute_type import AttributeType


@dataclass
class CreateAttribute:
    name: str
    type: AttributeType

    def __post_init__(self):
        if isinstance(self.type, str):
            self.type = AttributeType(self.type)


class CategoryAttributes(Controller):
    def __init__(self, service: CategoryService):
        self.service = service
        super().__init__()

    @classmethod
    def route(cls) -> Optional[str]:
        return "/api/categories/:category_id/attributes"

    @classmethod
    def class_name(cls) -> str:
        return "CategoryAttributes"

    @get()
    async def get_all(self, category_id: UUID) -> Response:
        pass

    @post()
    async def post(self, category_id: UUID, attribute: CreateAttribute) -> Response:
        pass

    @patch(":id")
    async def patch(
        self,
        id: UUID,
        name: Optional[str] = None,
        attribute_type: Optional[AttributeType] = None,
    ) -> Response:
        result = self.service.update_attribute(id=id, name=name, type=attribute_type)
        if result is None:
            return self.not_found()

        return self.ok(result.to_dict())
