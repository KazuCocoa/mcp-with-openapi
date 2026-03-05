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

Use a custom OpenAPI endpoint via `OPENAPI_URL`:

```bash
OPENAPI_URL="https://jsonplaceholder.typicode.com/openapi.json" uv run python main.py
```

## Open the MCP Inspector

```bash
uv run fastmcp dev inspector mcp_server.py:mcp
```

Optional: choose a fixed inspector UI port:

```bash
uv run fastmcp dev inspector mcp_server.py:mcp --ui-port 5173
```

After launch, open the local URL printed in your terminal.

## Debug with MCP Inspector

Use this flow to debug tools and schemas step-by-step.

1. Start inspector:

```bash
uv run fastmcp dev inspector mcp_server.py:mcp --ui-port 5173
```

2. Open `http://localhost:5173`.
3. List tools and confirm you can see:
	- `greet`
	- `openapi_getPostById`
4. Run a tool call in the UI:
	- Tool: `openapi_getPostById`
	- Input: `{"id": 1}`
5. Check result payload and validation errors in the inspector output pane.

### Helpful debug commands

Inspect generated tool metadata (name, description, input schema, output schema):

```bash
uv run fastmcp inspect mcp_server.py --format fastmcp
```

Call a tool directly from CLI (useful to compare CLI vs Inspector behavior):

```bash
uv run fastmcp call mcp_server.py openapi_getPostById '{"id": 1}'
```

### Common issues

- `No server named 'mcp' found`: use file-only form with CLI commands when needed (`mcp_server.py`), or keep `mcp_server.py:mcp` for `dev inspector`.
- Port already in use: change port with `--ui-port 5174` (and optionally `--server-port`).
- Tool missing in Inspector: restart inspector, then verify with `uv run fastmcp inspect mcp_server.py --format fastmcp`.
- OpenAPI call fails: verify `servers.url`, `path`, `operationId`, and required parameters in the spec.

### Faster edit/debug loop

`fastmcp dev inspector` enables reload by default, so changes in `mcp_server.py` should refresh automatically. If behavior seems stale, stop and restart the inspector process.


# references
- https://fastmcp.wiki/en/integrations/openapi
