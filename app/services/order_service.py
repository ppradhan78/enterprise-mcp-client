from app.mcp.tool_executor import ToolExecutor


class OrderService:

    def __init__(self, executor: ToolExecutor):

        self.executor = executor

    async def get_order(
        self,
        order_id: int
    ):

        return await self.executor.execute(
            "get_order",
            {
                "orderId": order_id
            }
        )