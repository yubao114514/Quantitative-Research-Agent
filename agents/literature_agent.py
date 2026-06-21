from mcp_server.tools import search_papers


def summarize_literature(query: str) -> list[dict]:
    return search_papers(query)
