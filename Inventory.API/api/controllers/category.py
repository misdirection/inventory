from typing import Optional
from blacksheep import Response
from blacksheep.server.controllers import Controller, get, post, patch
from application.category_service import CategoryService


class InventoryCategory(Controller):
    def __init__(self, service: CategoryService):
        self.service = service
        super().__init__()

    @classmethod
    def route(cls) -> Optional[str]:
        return "/api/inventory_category"

    @classmethod
    def class_name(cls) -> str:
        return "InventoryCategory"

    @get()
    async def get_all(self) -> Response:
        results = self.service.get_all_categories()
        return self.ok([result for result in results])

    @get(":id")
    async def get_by_id(self, id: int) -> Response:
        result = self.service.get_category_by_id(id)
        if result is None:
            return self.not_found()
        return self.ok(result)

    @post()
    async def post(self, name: str, description: str) -> Response:
        result = self.service.create_category(
            {"name": name, "description": description}
        )
        return self.created(result)

    @patch(":id")
    async def patch(
        self, id: int, name: Optional[str] = None, description: Optional[str] = None
    ) -> Response:
        updated_data = {}
        if name is not None:
            updated_data["name"] = name
        if description is not None:
            updated_data["description"] = description

        if not updated_data:
            return self.bad_request("No data provided to update")

        result = self.service.update_category(id, updated_data)
        if result is None:
            return self.not_found()
        return self.ok(result)
