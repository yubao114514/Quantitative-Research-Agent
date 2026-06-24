import pandas as pd

from quant.metrics import calculate_metrics


def normalize_rebalance_frequency(rebalance: str) -> str:
    """Keep older demo configs compatible with pandas 3.x frequency names."""
    return "ME" if rebalance == "M" else rebalance


def run_momentum_strategy(
    prices: pd.DataFrame,
    lookback_days: int,
    rebalance: str,
    top_n: int,
    benchmark: str,
    **_: object,
) -> dict:
    prices = prices.sort_index().ffill().dropna(how="all")
    tradable = [column for column in prices.columns if column != benchmark]
    momentum = prices.pct_change(lookback_days)
    rebalance = normalize_rebalance_frequency(rebalance)
    rebalance_dates = prices.groupby(pd.Grouper(freq=rebalance)).tail(1).index
    weights = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)

    current_weights = pd.Series(0.0, index=prices.columns)
    for date in prices.index:
        if date in rebalance_dates and date in momentum.index:
            leaders = momentum.loc[date, tradable].dropna().nlargest(top_n).index
            current_weights[:] = 0.0
            if len(leaders):
                current_weights.loc[leaders] = 1.0 / len(leaders)
        weights.loc[date] = current_weights

    returns = prices.pct_change().fillna(0)
    strategy_returns = (weights.shift(1).fillna(0) * returns).sum(axis=1)
    benchmark_returns = returns[benchmark] if benchmark in returns else returns.mean(axis=1)

    equity_curve = pd.DataFrame(
        {
            "strategy": (1 + strategy_returns).cumprod(),
            "benchmark": (1 + benchmark_returns).cumprod(),
        },
        index=prices.index,
    )

    return {
        "source": "monthly 12-month cross-sectional momentum",
        "metrics": calculate_metrics(strategy_returns),
        "equity_curve": equity_curve,
        "strategy_returns": strategy_returns,
        "benchmark_returns": benchmark_returns,
    }
