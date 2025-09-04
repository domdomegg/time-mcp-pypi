# Time MCP Server

A minimal Model Context Protocol (MCP) server built with Python.

The server provides one simple tool:
- `get_current_utc_time` - Gets the current UTC date and time in RFC 3339 format

## Quick start

Prerequisites:
- Python 3.8 or later
- Claude Desktop or another MCP-compatible client

Install and run with:

```bash
pip install time-mcp-pypi  # or from a local clone: pip install -e .
time-mcp-pypi
```

## Configuration

To use this server with Claude Desktop, add the following to your MCP configuration file:

### Windows
Add to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "time-server": {
      "command": "time-mcp-pypi"
    }
  }
}
```

### macOS
Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "time-server": {
      "command": "time-mcp-pypi"
    }
  }
}
```

## Usage

Once configured, you can use the time tool in Claude Desktop:
- "What's the current UTC time?"
- "Give me an RFC 3339 timestamp"

## Publishing New Versions

To publish a new version of the package:

1. **Tag the release** with a version number prefixed with 'v':
   ```bash
   git tag v1.0.1
   ```

2. **Push the tag** to trigger the publishing pipeline:
   ```bash
   git push --tags
   ```

Then the CI/CD pipeline will automatically publish the package.

### CI/CD
The project includes GitHub Actions workflows for:
- **Build & Test** - Builds and tests the Python package
- **Publish** - Automatically publishes to PyPI and creates GitHub releases on version tags

<!-- mcp-name: io.github.domdomegg/time-mcp-pypi -->
