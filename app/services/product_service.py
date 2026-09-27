from app.mcp.tool_executor import ToolExecutor


class ProductService:

    def __init__(self, executor: ToolExecutor):

        self.executor = executor

    async def get_product(
        self,
        product_id: int
    ):

        return await self.executor.execute(
            "get_product",
            {
                "productId": product_id
            }
        )