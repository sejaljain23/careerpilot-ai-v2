import asyncio
import traceback
from fastmcp import Client


SERVER_PATH = r"C:\Users\jains\OneDrive\Documents\CareerPilot-AI\careerpilot_mcp\server.py"

async def _call(tool_name: str, args: dict):
    try:
        async with Client(SERVER_PATH) as client:
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