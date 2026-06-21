import json
import sys

from mcp_server.tools import call_tool, tool_manifest


def main() -> None:
    """Tiny stdio MCP-style server for demo and code review visibility."""
    print(tool_manifest(), flush=True)
    for line in sys.stdin:
        request = json.loads(line)
        result = call_tool(request["tool"], request.get("arguments", {}))
        print(json.dumps({"result": str(result)}, default=str), flush=True)


if __name__ == "__main__":
    main()
