from mcp_server.tools import search_papers


def summarize_literature(query: str, strategy_type: str, use_online: bool) -> list[dict]:
    return search_papers(query, strategy_type=strategy_type, use_online=use_online)
