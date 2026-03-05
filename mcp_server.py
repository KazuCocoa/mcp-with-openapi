import os
import json
from urllib.request import urlopen

from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

jsonplaceholder_spec = {
    "openapi": "3.0.3",
    "info": {
        "title": "JSONPlaceholder API",
        "version": "1.0.0",
    },
    "servers": [{"url": "https://jsonplaceholder.typicode.com"}],
    "paths": {
        "/posts/{id}": {
            "get": {
                "operationId": "getPostById",
                "summary": "Fetch a post by id",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer", "minimum": 1, "maximum": 100},
                        "description": "Post id",
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Post details",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "userId": {"type": "integer"},
                                        "id": {"type": "integer"},
                                        "title": {"type": "string"},
                                        "body": {"type": "string"},
                                    },
                                    "required": ["userId", "id", "title", "body"],
                                }
                            }
                        },
                    }
                },
            }
        }
    },
}

def fetch_openapi_spec(url: str) -> dict:
    with urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))

if os.environ.get("OPENAPI_URL"):
    openapi_url = os.environ.get("OPENAPI_URL")
    jsonplaceholder_spec = fetch_openapi_spec(openapi_url)


openapi_mcp = FastMCP.from_openapi(jsonplaceholder_spec, name="JSONPlaceholder OpenAPI")
mcp.mount(openapi_mcp, namespace="openapi")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"
