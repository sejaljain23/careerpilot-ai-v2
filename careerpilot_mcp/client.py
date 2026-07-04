import asyncio
import traceback
import os
from fastmcp import Client

# Path to the MCP server inside the project
SERVER_PATH = os.path.join(
    os.path.dirname(__file__),
    "server.py"
)

async def _call(tool_name: str, args: dict):
    try:
        # Explicitly run the server over stdio
        async with Client(f"python {SERVER_PATH}") as client:
            result = await client.call_tool(tool_name, args)

            if hasattr(result, "data"):
                return result.data

            if hasattr(result, "content"):
                return result.content

            return str(result)

    except Exception:
        traceback.print_exc()
        raise


def call_tool(tool_name: str, args: dict):
    return asyncio.run(_call(tool_name, args))