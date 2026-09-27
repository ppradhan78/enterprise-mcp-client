# from app.mcp.connection import MCPConnection


# class MCPClient:

#     def __init__(self):

#         self.connection = MCPConnection()
#         self.session = None

#     async def connect(self):

#         self.session = await self.connection.connect()

#     async def disconnect(self):

#         await self.connection.disconnect()

#     async def list_tools(self):

#         result = await self.session.list_tools()

#         return result.tools

#     async def call_tool(
#         self,
#         tool_name: str,
#         arguments: dict
#     ):

#         return await self.session.call_tool(
#             tool_name,
#             arguments
#         )

#     async def list_resources(self):

#         result = await self.session.list_resources()

#         return result.resources

#     async def list_prompts(self):

#         result = await self.session.list_prompts()

#         return result.prompts


from app.mcp.connection import MCPConnection


class MCPClient:

    def __init__(self):

        self.connection = MCPConnection()
        self.session = None

    async def connect(self):

        self.session = await self.connection.connect()

    async def disconnect(self):

        if self.session is not None:

            await self.connection.disconnect()

            self.session = None

    async def list_tools(self):

        result = await self.session.list_tools()

        return result.tools

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict
    ):

        return await self.session.call_tool(
            tool_name,
            arguments
        )