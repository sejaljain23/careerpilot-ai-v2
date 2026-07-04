import asyncio
import os
import traceback

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

SERVER_PATH = os.path.join(
    os.path.dirname(__file__),
    "server.py"
)

transport = StdioTransport(
    command="python",
    args=[SERVER_PATH],
)

async def _call(tool_name: str, args: dict):
    try:
        async with Client(transport) as client:
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