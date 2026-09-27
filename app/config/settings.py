import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    MCP_SERVER_URL: str = os.getenv(
        "MCP_SERVER_URL",
        "http://127.0.0.1:8000/mcp"
    )


settings = Settings()