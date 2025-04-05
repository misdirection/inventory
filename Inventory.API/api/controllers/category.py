from typing import Optional
from uuid import UUID
from blacksheep import Response
from blacksheep.server.controllers import Controller, get, post, patch, delete
from application.category_service import CategoryService


class InventoryCategory(Controller):
    def __init__(self, service: CategoryService):
        self.service = service
        super().__init__()

    @classmethod
    def route(cls) -> Optional[str]:
        return "/api/categories"

    @classmethod
    def class_name(cls) -> str:
        return "Categories"

    @get()
    async def get_all(self) -> Response:
        results = self.service.get_all()

        return self.ok([result.to_dict() for result in results])

    @get(":id")
    async def get_by_id(self, id: UUID) -> Response:
        result = self.service.get(id)

        if result is None:
            return self.not_found()

        return self.ok(result.to_dict())

    @post()
    async def post(self, name: str, description: str) -> Response:
        print(name, description, flush=True)
        result = self.service.create(name=name, description=description)

        return self.created(result.to_dict())

    @patch(":id")
    async def patch(
        self, id: UUID, name: Optional[str] = None, description: Optional[str] = None
    ) -> Response:
        result = self.service.update(id=id, name=name, description=description)
        if result is None:
            return self.not_found()

        return self.ok(result.to_dict())

    @delete(":id")
    async def delete(self, id: UUID) -> Response:
        result = self.service.delete(id)
        if result is None:
            return self.not_found()

        return self.ok(result.to_dict())
