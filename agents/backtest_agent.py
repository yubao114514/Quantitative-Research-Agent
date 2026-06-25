from mcp_server.tools import run_mean_reversion_backtest, run_momentum_backtest


MOMENTUM_CODE = """
def run_momentum_strategy(prices, lookback_days=252, rebalance="ME", top_n=3):
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

MEAN_REVERSION_CODE = """
def run_mean_reversion_strategy(prices, lookback_days=20, rebalance="ME", top_n=3):
    short_term_return = prices.pct_change(lookback_days)
    rebalance_dates = prices.groupby(pd.Grouper(freq=rebalance)).tail(1).index
    weights = pd.DataFrame(0.0, index=prices.index, columns=prices.columns)
    tradable = [c for c in prices.columns if c != "SPY"]
    current_weights = pd.Series(0.0, index=prices.columns)

    for date in prices.index:
        if date in rebalance_dates and date in short_term_return.index:
            candidates = short_term_return.loc[date, tradable].dropna().nsmallest(top_n).index
            current_weights[:] = 0.0
            if len(candidates):
                current_weights.loc[candidates] = 1.0 / len(candidates)
        weights.loc[date] = current_weights

    returns = prices.pct_change().fillna(0)
    strategy_returns = (weights.shift(1).fillna(0) * returns).sum(axis=1)
    benchmark_returns = returns["SPY"]
    return strategy_returns, benchmark_returns
""".strip()


def run_backtest(prices, strategy_type: str):
    if strategy_type == "mean_reversion":
        result = run_mean_reversion_backtest(
            {
                "prices": prices,
                "lookback_days": 20,
                "rebalance": "ME",
                "top_n": 3,
                "benchmark": "SPY",
            }
        )
        result["generated_code"] = MEAN_REVERSION_CODE
        return result

    result = run_momentum_backtest(
        {
            "prices": prices,
            "lookback_days": 252,
            "rebalance": "ME",
            "top_n": 3,
            "benchmark": "SPY",
        }
    )
    result["generated_code"] = MOMENTUM_CODE
    return result
