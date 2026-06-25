import json
from typing import Any

from quant.backtest import run_mean_reversion_strategy, run_momentum_strategy
from quant.data import load_market_data
from quant.papers import search_strategy_papers
from quant.report import build_research_report


def search_papers(query: str, strategy_type: str = "momentum", use_online: bool = True) -> list[dict]:
    return search_strategy_papers(query, strategy_type, use_online=use_online)


def get_market_data(tickers: list[str], start: str, end: str):
    return load_market_data(tickers=tickers, start=start, end=end)


def run_momentum_backtest(config: dict[str, Any]) -> dict:
    return run_momentum_strategy(**config)


def run_mean_reversion_backtest(config: dict[str, Any]) -> dict:
    return run_mean_reversion_strategy(**config)


def generate_research_report(payload: dict[str, Any]) -> str:
    return build_research_report(payload)


TOOLS = {
    "search_papers": search_papers,
    "get_market_data": get_market_data,
    "run_momentum_backtest": run_momentum_backtest,
    "run_mean_reversion_backtest": run_mean_reversion_backtest,
    "generate_research_report": generate_research_report,
}


def call_tool(name: str, arguments: dict[str, Any]) -> Any:
    if name not in TOOLS:
        raise ValueError(f"Unknown MCP tool: {name}")
    return TOOLS[name](**arguments)


def tool_manifest() -> str:
    return json.dumps(
        {
            "server": "quantitative-research-assistant",
            "tools": sorted(TOOLS.keys()),
        },
        indent=2,
    )
