def build_research_report(payload: dict) -> str:
    metrics = payload["metrics"]
    papers = payload["papers"]
    paper_lines = "\n".join(
        f"- **{paper['citation']}**, _{paper['title']}_: {paper['summary']}"
        for paper in papers
    )
    return f"""
# Quantitative Research Report

## Strategy Idea
{payload["query"]}

## Research Thesis
Momentum strategies test whether assets with stronger trailing performance continue to outperform over the next holding period. This MVP evaluates a monthly rebalanced large-cap US equity implementation.

## Literature Review
{paper_lines}

## Data
{payload["data_notes"]}

## Methodology
- Rank non-benchmark stocks by 12-month trailing return.
- Select the top 3 stocks at each month-end rebalance.
- Allocate equal weights to selected names.
- Compare the resulting equity curve against SPY.

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
