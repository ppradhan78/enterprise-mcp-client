from app.mcp.tool_executor import ToolExecutor


class WeatherService:

    def __init__(self, executor: ToolExecutor):

        self.executor = executor

    async def get_weather(
        self,
        city: str,
        country_code: str
    ):

        return await self.executor.execute(
            "get_weather",
            {
                "city": city,
                "country_code": country_code
            }
        )