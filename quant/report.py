def build_research_report(payload: dict) -> str:
    metrics = payload["metrics"]
    papers = payload["papers"]
    strategy_label = payload.get("strategy_label", "Momentum")
    strategy_type = payload.get("strategy_type", "momentum")
    benchmark = payload.get("benchmark", "benchmark")
    strategy_config = payload.get("strategy_config", {})
    config_reason = payload.get("config_reason", "")
    if strategy_type == "mean_reversion":
        thesis = "Mean reversion strategies test whether short-term losers rebound after temporary overreaction. This MVP evaluates a monthly rebalanced 20-day reversal implementation."
        methodology = """- Rank non-benchmark stocks by 20-day trailing return.
- Select the 3 stocks with the weakest short-term returns at each month-end rebalance.
- Allocate equal weights to selected names.
- Compare the resulting equity curve against {benchmark}."""
    else:
        thesis = "Momentum strategies test whether assets with stronger trailing performance continue to outperform over the next holding period. This MVP evaluates a monthly rebalanced large-cap US equity implementation."
        methodology = """- Rank non-benchmark stocks by 12-month trailing return.
- Select the top 3 stocks at each month-end rebalance.
- Allocate equal weights to selected names.
- Compare the resulting equity curve against {benchmark}."""
    methodology = methodology.format(benchmark=benchmark)
    paper_lines = "\n".join(
        f"- **{paper['citation']}**, _{paper['title']}_: {paper['summary']}"
        for paper in papers
    )
    return f"""
# Quantitative Research Report

## Strategy Idea
{payload["query"]}

## Research Thesis
{thesis}

## Strategy Type
{strategy_label}

## Agent-Recommended Configuration
- Benchmark: `{benchmark}`
- Lookback days: `{strategy_config.get("lookback_days", "n/a")}`
- Rebalance: `{strategy_config.get("rebalance", "n/a")}`
- Top N: `{strategy_config.get("top_n", "n/a")}`

{config_reason}

## Literature Review
{paper_lines}

## Data
{payload["data_notes"]}

## Methodology
{methodology}

## Results
- Total return: **{metrics['total_return']:.1%}**
- Annualized return: **{metrics['annualized_return']:.1%}**
- Volatility: **{metrics['volatility']:.1%}**
- Sharpe ratio: **{metrics['sharpe_ratio']:.2f}**
- Max drawdown: **{metrics['max_drawdown']:.1%}**

## Risks and Limitations
- The first version ignores transaction costs, slippage, taxes, liquidity limits, and survivorship bias.
- Momentum can reverse sharply during regime changes and market rebounds.
- The sample universe is intentionally small for demo clarity.

## Next Research Steps
- Add transaction cost assumptions and turnover analysis.
- Expand the universe to all S&P 500 constituents.
- Test alternative lookback windows and rebalance frequencies.
- Compare momentum with value, quality, and low-volatility factors.
""".strip()
