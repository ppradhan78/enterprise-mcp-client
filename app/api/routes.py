from fastapi import APIRouter, HTTPException

from app.mcp.client import MCPClient
from app.mcp.tool_executor import ToolExecutor

from app.services.weather_service import WeatherService
from app.services.order_service import OrderService
from app.services.product_service import ProductService


router = APIRouter()


# --------------------------------------------------
# MCP Client
# --------------------------------------------------

mcp_client = MCPClient()

tool_executor = ToolExecutor(
    mcp_client
)


# --------------------------------------------------
# Services
# --------------------------------------------------

weather_service = WeatherService(
    tool_executor
)

order_service = OrderService(
    tool_executor
)

product_service = ProductService(
    tool_executor
)


# ==================================================
# Weather
# ==================================================

@router.get("/weather")
async def get_weather(
    city: str,
    country_code: str
):

    try:

        result = await weather_service.get_weather(
            city=city,
            country_code=country_code
        )

        return result

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ==================================================
# Order
# ==================================================

@router.get("/orders/{order_id}")
async def get_order(
    order_id: int
):

    try:

        result = await order_service.get_order(
            order_id=order_id
        )

        return result

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ==================================================
# Product
# ==================================================

@router.get("/products/{product_id}")
async def get_product(
    product_id: int
):

    try:

        result = await product_service.get_product(
            product_id=product_id
        )

        return result

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )