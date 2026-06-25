from agents.backtest_agent import run_backtest
from agents.data_agent import select_and_load_data
from agents.literature_agent import summarize_literature
from agents.report_agent import write_report
from agents.research_planner import create_research_plan
from agents.strategy_router import detect_strategy_type, strategy_label


def run_research_pipeline(
    query: str,
    tickers: list[str],
    start: str,
    end: str,
    benchmark: str,
    strategy_config: dict | None = None,
    config_reason: str = "",
    use_online_papers: bool = True,
) -> dict:
    strategy_type = detect_strategy_type(query)
    label = strategy_label(strategy_type)
    if strategy_config is None:
        from quant.config import load_app_config

        strategy_config = load_app_config()["strategies"][strategy_type]
    research_plan = create_research_plan(query, strategy_label=label, benchmark=benchmark)
    papers = summarize_literature(query, strategy_type=strategy_type, use_online=use_online_papers)
    data_notes, prices = select_and_load_data(tickers, start, end, benchmark)
    backtest = run_backtest(
        prices,
        strategy_type=strategy_type,
        benchmark=benchmark,
        strategy_config=strategy_config,
    )

    report = write_report(
        {
            "query": query,
            "strategy_type": strategy_type,
            "strategy_label": label,
            "benchmark": benchmark,
            "strategy_config": strategy_config,
            "config_reason": config_reason,
            "research_plan": research_plan,
            "papers": papers,
            "data_notes": data_notes,
            "metrics": backtest["metrics"],
            "source": backtest["source"],
        }
    )

    evaluation_map = """
| Kaggle key concept | Where demonstrated | Implementation |
|---|---|---|
| Agent / Multi-agent system | Code | `agents/orchestrator.py` coordinates Research Planner, Literature Agent, Data Agent, Backtest Agent, and Report Agent. |
| MCP Server | Code | `mcp_server/tools.py` exposes paper search, data loading, multiple backtesting tools, and report generation tools. |
| Agent skills | Code or Video | `skills/` documents reusable quant research capabilities such as momentum research and report writing. |
"""

    return {
        "strategy_type": strategy_type,
        "strategy_label": label,
        "benchmark": benchmark,
        "strategy_config": strategy_config,
        "config_reason": config_reason,
        "research_plan": research_plan,
        "papers": papers,
        "paper_source": papers[0].get("source", "Local library") if papers else "No papers found",
        "data_notes": data_notes,
        "prices": prices,
        "metrics": backtest["metrics"],
        "equity_curve": backtest["equity_curve"],
        "generated_code": backtest["generated_code"],
        "report": report,
        "evaluation_map": evaluation_map.strip(),
    }
