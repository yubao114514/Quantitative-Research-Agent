# Quantitative Research Assistant Demo Script

## 60-90 Second Version

Hi, this is **Quantitative Research Assistant**, an AI-powered quant research assistant that turns a natural-language strategy idea into a research plan, paper review, data selection, backtest, and final report.

For example, I can type:

```text
Mean reversion strategy on technology stocks
```

Before running the full pipeline, the agent recommends a research configuration. It detects the strategy type, suggests a suitable universe, chooses a benchmark such as QQQ, and sets backtest parameters like lookback window, rebalance frequency, and top N holdings.

The user can still edit the universe manually. For example, I can add a ticker like RKLB, and the app will include it in the data and backtest workflow.

When I run the pipeline, the app coordinates five agents:

- **Research Planner** creates a structured research plan.
- **Literature Agent** searches or summarizes relevant quant papers.
- **Data Agent** loads market data from yfinance, with fallback data for demo stability.
- **Backtest Agent** runs the selected strategy and calculates performance metrics.
- **Report Agent** writes the final markdown research report.

The project demonstrates three Kaggle evaluation concepts:

- **Agent / Multi-agent system**: the workflow is split across specialized agents.
- **MCP Server**: local MCP-style tools expose paper search, market data, backtesting, and report generation.
- **Agent skills**: reusable skill modules define strategy research, literature review, data selection, backtest analysis, and report writing.

The final output includes the research plan, literature review, data notes, generated strategy logic, performance metrics, equity curve, and downloadable report.

## 2-3 Minute Extended Version

The problem I wanted to solve is that early-stage quant research is repetitive. A researcher often starts with a vague idea like "momentum strategy" or "mean reversion strategy", then has to search papers, choose a universe, find data, write backtest code, interpret performance, and draft a report.

This project automates that first-pass workflow.

The first screen is a Streamlit research workbench. There is no landing page; the user can immediately enter a strategy idea.

For this demo, I will use:

```text
Mean reversion strategy on technology stocks
```

When I click **Suggest research config**, the agent detects that this is a mean reversion strategy and recommends a technology-focused universe, a benchmark, and default backtest settings. The benchmark is used as a comparison curve, so the strategy is evaluated against a simple buy-and-hold alternative like QQQ.

The sidebar also lets the user customize the universe. This is important because a quant researcher may want the agent's recommendation as a starting point, but still add or remove tickers manually before running the experiment.

After I click **Run research pipeline**, the multi-agent workflow begins.

First, the **Research Planner Agent** converts the strategy idea into a testable plan. This keeps the workflow grounded in a clear hypothesis.

Second, the **Literature Agent** searches online papers through arXiv when available. If online search fails, it uses a local paper library, so the demo remains stable.

Third, the **Data Agent** loads market data. It tries yfinance first and falls back to sample data if needed.

Fourth, the **Backtest Agent** runs the selected strategy. The app currently supports momentum and mean reversion logic. It calculates total return, annualized return, volatility, Sharpe ratio, and max drawdown.

Finally, the **Report Agent** creates a research report with thesis, literature, data, methodology, results, risks, and next steps.

The key point is that this is not only a chatbot. It is an agent system that plans, researches, calls tools, runs quantitative analysis, and produces a structured research artifact.

## Kaggle Evaluation Talking Points

**Agent / Multi-agent system**

The orchestration lives in `agents/orchestrator.py`. It coordinates five specialized agents instead of using one monolithic prompt.

**MCP Server**

The local MCP-style tool layer lives in `mcp_server/tools.py`. It exposes tools such as `search_papers`, `get_market_data`, `run_momentum_backtest`, `run_mean_reversion_backtest`, and `generate_research_report`.

**Agent skills**

The `skills/` folder contains reusable skill definitions for momentum research, literature review, market data selection, backtest analysis, and quant report writing.

## Recording Checklist

- [ ] Start from the Streamlit workbench.
- [ ] Enter `Mean reversion strategy on technology stocks`.
- [ ] Click **Suggest research config**.
- [ ] Explain the suggested universe, benchmark, lookback, rebalance, and top N.
- [ ] Add a custom ticker such as `RKLB`.
- [ ] Click **Run research pipeline**.
- [ ] Show the agent status messages.
- [ ] Open **Research Plan**.
- [ ] Open **Literature** and show paper summaries.
- [ ] Open **Data** and show selected data.
- [ ] Open **Backtest** and show metrics plus equity curve.
- [ ] Open **Report** and show the final markdown report.
- [ ] Open **Evaluation Map** and connect it to the Kaggle requirements.

## Backup Talking Points

- If yfinance fails: "The app includes fallback data so the demo remains reproducible."
- If arXiv search fails: "The app falls back to a local paper library."
- If Gemini is unavailable: "The app can still run deterministic fallback outputs, but it is designed to use Gemini or OpenAI when an API key is configured."
- If asked about limitations: "This MVP does not yet include transaction costs, slippage, survivorship-bias-free constituents, or production risk controls."
