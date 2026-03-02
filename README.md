# mcp-with-openapi

Minimal FastMCP example server.

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## Install dependencies

```bash
uv sync
```

## Run the server

```bash
uv run python main.py
```

This starts the MCP server over HTTP on port `8000`.

## Open the MCP Inspector

```bash
uv run fastmcp dev inspector mcp_server.py:mcp
```

Optional: choose a fixed inspector UI port:

```bash
uv run fastmcp dev inspector mcp_server.py:mcp --ui-port 5173
```

After launch, open the local URL printed in your terminal.
