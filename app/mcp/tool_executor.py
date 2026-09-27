from app.mcp.client import MCPClient


class ToolExecutor:

    def __init__(self, client: MCPClient):

        self.client = client

    async def execute(
        self,
        tool_name: str,
        arguments: dict
    ):

        return await self.client.call_tool(
            tool_name,
            arguments
        )