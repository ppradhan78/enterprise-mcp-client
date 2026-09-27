# import asyncio

# from app.mcp.client import MCPClient
# from app.mcp.tool_executor import ToolExecutor

# from app.services.weather_service import WeatherService
# from app.services.order_service import OrderService
# from app.services.product_service import ProductService


# async def main():

#     client = MCPClient()

#     try:

#         print("Connecting to MCP Server...")

#         await client.connect()

#         print("Connected.")

#         # --------------------------------
#         # List Tools
#         # --------------------------------

#         tools = await client.list_tools()

#         print("\nAvailable MCP Tools:")

#         for tool in tools:

#             print(
#                 f"- {tool.name}"
#             )

#         # --------------------------------
#         # Tool Executor
#         # --------------------------------

#         executor = ToolExecutor(client)

#         # --------------------------------
#         # Weather
#         # --------------------------------

#         weather_service = WeatherService(executor)

#         weather = await weather_service.get_weather(
#             city="Hyderabad",
#             country_code="IN"
#         )

#         print("\nWeather Result:")
#         print(weather)

#         # --------------------------------
#         # Order
#         # --------------------------------

#         order_service = OrderService(executor)

#         order = await order_service.get_order(
#             order_id=1
#         )

#         print("\nOrder Result:")
#         print(order)

#         # --------------------------------
#         # Product
#         # --------------------------------

#         product_service = ProductService(executor)

#         product = await product_service.get_product(
#             product_id=1
#         )

#         print("\nProduct Result:")
#         print(product)

#     except Exception as ex:

#         print(
#             f"MCP Client Error: {ex}"
#         )

#     finally:

#         await client.disconnect()

#         print("\nDisconnected.")


# if __name__ == "__main__":

#     asyncio.run(main())

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router
from app.api import routes


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting Enterprise MCP Client...")

    await routes.mcp_client.connect()

    print("Connected to MCP Server.")

    yield

    print("Stopping Enterprise MCP Client...")

    await routes.mcp_client.disconnect()

    print("Disconnected from MCP Server.")


app = FastAPI(
    title="Enterprise MCP Client",
    description="REST API over MCP Client",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(
    router
)


@app.get("/health")
async def health():

    return {
        "status": "UP",
        "service": "enterprise-mcp-client"
    }