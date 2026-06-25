# Quantitative Research Assistant

An AI agent system that turns a natural-language trading idea into a literature review, data selection, backtest, and research report.

Default demo query:

```text
Momentum strategy on S&P 500 stocks
```

## Why This Fits the Kaggle Capstone

The project demonstrates three required Evaluation concepts:

| Key concept | Where demonstrated |
|---|---|
| Agent / Multi-agent system | `agents/orchestrator.py` coordinates five agents: Research Planner, Literature Agent, Data Agent, Backtest Agent, and Report Agent. |
| MCP Server | `mcp_server/tools.py` exposes local tools for paper search, data loading, backtesting, and report generation. |
| Agent skills | `skills/` contains reusable quant research skills for strategy research, literature review, data selection, backtest analysis, and report writing. |

## Features

- Streamlit research workbench
- Gemini API support through `GEMINI_API_KEY`
- OpenAI API support through `OPENAI_API_KEY`
- Deterministic fallback outputs when no API key is available
- yfinance market data with sample-data fallback
- Online arXiv paper search with local paper-library fallback
- Monthly 12-month momentum backtest
- Monthly 20-day mean reversion backtest
- Config-driven defaults in `config/app_config.json`
- Config-driven paper library in `config/papers.json`
- Metrics: total return, annualized return, volatility, Sharpe ratio, max drawdown
- Downloadable markdown research report

## Setup

```bash
pip install -r requirements.txt
```

Optional:

```bash
set GEMINI_API_KEY=your_gemini_api_key_here
set OPENAI_API_KEY=your_api_key_here
```

Run:

```bash
streamlit run app.py
```

## Architecture

```text
User query
  -> Research Planner Agent
  -> Literature Agent
  -> Data Agent
  -> Backtest Agent
  -> Report Agent
  -> Streamlit output
```

The agents call the local MCP-style tool layer:

```text
search_papers(query)
get_market_data(tickers, start, end)
run_momentum_backtest(config)
run_mean_reversion_backtest(config)
generate_research_report(payload)
```

## Limitations

This is an MVP for demonstration. It does not yet include transaction costs, slippage, taxes, survivorship-bias-free constituent data, or production portfolio risk controls.
