import numpy as np
import pandas as pd


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
        if not prices.empty and {"SPY"}.issubset(set(prices.columns)):
            return prices, "yfinance live adjusted close"
    except Exception:
        pass

    return generate_sample_prices(tickers=tickers, start=start, end=end), "deterministic sample data"


def generate_sample_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    index = pd.bdate_range(start=start, end=end)
    rng = np.random.default_rng(42)
    prices = {}
    drift_map = {
        "NVDA": 0.0007,
        "MSFT": 0.00045,
        "AAPL": 0.00042,
        "META": 0.0005,
        "AMZN": 0.0004,
        "GOOGL": 0.00035,
        "JPM": 0.00025,
        "XOM": 0.00022,
        "UNH": 0.0003,
        "SPY": 0.00028,
    }
    for i, ticker in enumerate(tickers):
        drift = drift_map.get(ticker, 0.00025)
        vol = 0.018 if ticker != "SPY" else 0.011
        cycle = np.sin(np.linspace(0, 12, len(index)) + i) * 0.0015
        shocks = rng.normal(drift, vol, len(index)) + cycle
        prices[ticker] = 100 * np.exp(np.cumsum(shocks))
    return pd.DataFrame(prices, index=index)
