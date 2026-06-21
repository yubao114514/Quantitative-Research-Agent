from mcp_server.tools import run_momentum_backtest


GENERATED_CODE = """
def run_momentum_strategy(prices, lookback_days=252, rebalance="M", top_n=3):
    momentum = prices.pct_change(lookback_days)
    rebalance_dates = prices.groupby(pd.Grouper(freq=rebalance)).tail(1).index
    weights = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    tradable = [c for c in prices.columns if c != "SPY"]
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
    benchmark_returns = returns["SPY"]
    return strategy_returns, benchmark_returns
""".strip()


def run_backtest(prices):
    result = run_momentum_backtest(
        {
            "prices": prices,
            "lookback_days": 252,
            "rebalance": "M",
            "top_n": 3,
            "benchmark": "SPY",
        }
    )
    result["generated_code"] = GENERATED_CODE
    return result
