#!/usr/bin/env python3
"""Time MCP Server main entry point."""

import asyncio
import logging
from datetime import datetime, timezone

from mcp.server.stdio import stdio_server
from mcp.server import Server
from mcp.types import Tool, TextContent


logger = logging.getLogger(__name__)

server = Server("time-mcp-server")


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="get_current_utc_time",
            description="Gets the current UTC date and time in RFC 3339 format",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name == "get_current_utc_time":
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        return [TextContent(type="text", text=current_time)]
    else:
        raise ValueError(f"Unknown tool: {name}")


async def async_main():
    """Async main entry point for the server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


def main():
    """Sync main entry point for the server."""
    asyncio.run(async_main())


if __name__ == "__main__":
    main()