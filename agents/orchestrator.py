from agents.backtest_agent import run_backtest
from agents.data_agent import select_and_load_data
from agents.literature_agent import summarize_literature
from agents.report_agent import write_report
from agents.research_planner import create_research_plan
from agents.strategy_router import detect_strategy_type, strategy_label


def run_research_pipeline(query: str, tickers: list[str], start: str, end: str) -> dict:
    strategy_type = detect_strategy_type(query)
    research_plan = create_research_plan(query)
    papers = summarize_literature(query)
    data_notes, prices = select_and_load_data(tickers, start, end)
    backtest = run_backtest(prices, strategy_type=strategy_type)

    report = write_report(
        {
            "query": query,
            "strategy_type": strategy_type,
            "strategy_label": strategy_label(strategy_type),
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
        "strategy_label": strategy_label(strategy_type),
        "research_plan": research_plan,
        "papers": papers,
        "data_notes": data_notes,
        "prices": prices,
        "metrics": backtest["metrics"],
        "equity_curve": backtest["equity_curve"],
        "generated_code": backtest["generated_code"],
        "report": report,
        "evaluation_map": evaluation_map.strip(),
    }
