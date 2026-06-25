from quant.config import load_paper_library
from quant.paper_search import search_arxiv_papers


def search_strategy_papers(query: str, strategy_type: str, use_online: bool = True) -> list[dict]:
    if use_online:
        try:
            online_papers = search_arxiv_papers(query, strategy_type)
            if online_papers:
                return online_papers
        except Exception:
            pass

    papers = load_paper_library()
    matches = [paper for paper in papers if paper.get("strategy") == strategy_type]
    return matches or [paper for paper in papers if paper.get("strategy") == "momentum"]
