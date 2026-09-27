from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

from app.config.settings import settings


class MCPConnection:

    def __init__(self):
        self.session = None
        self.exit_stack = AsyncExitStack()

    async def connect(self):

        read_stream, write_stream = await self.exit_stack.enter_async_context(
            streamable_http_client(
                settings.MCP_SERVER_URL
            )
        )

        self.session = await self.exit_stack.enter_async_context(
            ClientSession(
                read_stream,
                write_stream
            )
        )

        await self.session.initialize()

        return self.session

    async def disconnect(self):

        await self.exit_stack.aclose()