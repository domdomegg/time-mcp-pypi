# Time MCP Server

A minimal Model Context Protocol (MCP) server that provides current UTC time in RFC 3339 format.

## Installation

```bash
pip install time-mcp-pypi
```

(for a local clone, run `pip install -e .` instead)

## Usage

Run the server:

```bash
time-mcp-pypi
```

## Available Tools

### get_current_utc_time

Gets the current UTC date and time in RFC 3339 format.

**Parameters:** None

**Returns:** Current UTC timestamp as a string (e.g., "2024-09-04T13:45:30Z")
