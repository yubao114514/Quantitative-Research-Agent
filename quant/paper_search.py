import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


ARXIV_API_URL = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def build_literature_query(query: str, strategy_type: str) -> str:
    if strategy_type == "mean_reversion":
        return f"{query} short term reversal stock returns finance"
    return f"{query} momentum investing stock returns finance"


def search_arxiv_papers(query: str, strategy_type: str, max_results: int = 5) -> list[dict]:
    search_query = build_literature_query(query, strategy_type)
    params = urllib.parse.urlencode(
        {
            "search_query": f"all:{search_query}",
            "start": 0,
            "max_results": max_results,
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
    )
    request = urllib.request.Request(
        f"{ARXIV_API_URL}?{params}",
        headers={"User-Agent": "quantitative-research-assistant/0.1"},
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        root = ET.fromstring(response.read())

    papers = []
    for entry in root.findall("atom:entry", ATOM_NS):
        title = clean_text(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
        summary = clean_text(entry.findtext("atom:summary", default="", namespaces=ATOM_NS))
        authors = [
            clean_text(author.findtext("atom:name", default="", namespaces=ATOM_NS))
            for author in entry.findall("atom:author", ATOM_NS)
        ]
        published = entry.findtext("atom:published", default="", namespaces=ATOM_NS)[:4]
        url = entry.findtext("atom:id", default="", namespaces=ATOM_NS)
        citation = format_citation(authors, published)
        if title and summary:
            papers.append(
                {
                    "title": title,
                    "citation": citation,
                    "summary": summary,
                    "url": url,
                    "source": "arXiv",
                }
            )
    return papers


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def format_citation(authors: list[str], year: str) -> str:
    if not authors:
        return f"arXiv ({year or 'n.d.'})"
    if len(authors) == 1:
        author_text = authors[0]
    elif len(authors) == 2:
        author_text = f"{authors[0]} and {authors[1]}"
    else:
        author_text = f"{authors[0]} et al."
    return f"{author_text} ({year or 'n.d.'})"
