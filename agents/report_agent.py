from mcp_server.tools import generate_research_report
from agents.llm import call_llm


def write_report(payload: dict) -> str:
    fallback = generate_research_report(payload)
    metrics = payload["metrics"]
    paper_titles = ", ".join(paper["title"] for paper in payload["papers"])
    return call_llm(
        "You are a quant research report writing agent. Write concise markdown reports with sections for thesis, literature, data, methodology, results, risks, and next steps.",
        f"""
Write a markdown quant research report.

Query: {payload["query"]}
Strategy type: {payload.get("strategy_label", "Momentum")}
Config reason: {payload.get("config_reason", "")}
Papers: {paper_titles}
Data notes: {payload["data_notes"]}
Metrics: total return {metrics["total_return"]:.2%}, annual return {metrics["annualized_return"]:.2%}, volatility {metrics["volatility"]:.2%}, Sharpe {metrics["sharpe_ratio"]:.2f}, max drawdown {metrics["max_drawdown"]:.2%}
""".strip(),
        fallback,
    )
