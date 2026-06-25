import numpy as np
import pandas as pd
from pandas.util import hash_pandas_object


def load_market_data(tickers: list[str], start: str, end: str):
    try:
        import yfinance as yf

        data = yf.download(
            tickers=tickers,
            start=start,
            end=end,
            auto_adjust=True,
            progress=False,
            group_by="column",
        )
        if "Close" in data:
            prices = data["Close"].dropna(how="all")
        else:
            prices = data.dropna(how="all")
        prices = prices.ffill().dropna(how="all")
        if not prices.empty:
            return prices, "yfinance live adjusted close"
    except Exception:
        pass

    return generate_sample_prices(tickers=tickers, start=start, end=end), "deterministic sample data"


def generate_sample_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    index = pd.bdate_range(start=start, end=end)
    rng = np.random.default_rng(42)
    prices = {}
    for i, ticker in enumerate(tickers):
        ticker_seed = int(hash_pandas_object(pd.Index([ticker]))[0] % 1000)
        drift = 0.00018 + ticker_seed / 1_000_000
        vol = 0.010 + (ticker_seed % 12) / 1000
        cycle = np.sin(np.linspace(0, 12, len(index)) + i) * 0.0015
        shocks = rng.normal(drift, vol, len(index)) + cycle
        prices[ticker] = 100 * np.exp(np.cumsum(shocks))
    return pd.DataFrame(prices, index=index)
