from mcp_server.tools import get_market_data


def select_and_load_data(tickers: list[str], start: str, end: str, benchmark: str) -> tuple[str, object]:
    prices, source = get_market_data(tickers=tickers, start=start, end=end)
    notes = f"""
The Data Agent selected the requested research universe and benchmark.

- Source used: **{source}**
- Tickers: `{", ".join(tickers)}`
- Date range: `{start}` to `{end}`
- Frequency: daily adjusted close prices
- Benchmark: `{benchmark}`

If live data cannot be downloaded, the app uses deterministic sample data so the demo remains reproducible.
"""
    return notes.strip(), prices
