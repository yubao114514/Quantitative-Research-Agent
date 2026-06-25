# Quantitative Research Assistant Demo Script

## 60-90 Second Version

Hi, this is **Quantitative Research Assistant**, an AI agent system that turns a natural-language trading idea into a structured quant research workflow.

For this demo, I use the query:

```text
Momentum strategy on S&P 500 stocks
```

After I click **Run research pipeline**, the app coordinates five agents:

- The **Research Planner** converts the idea into a testable research plan.
- The **Literature Agent** summarizes classic momentum research papers.
- The **Data Agent** chooses a liquid US equity universe and benchmark.
- The **Backtest Agent** runs a monthly rebalanced 12-month momentum strategy.
- The **Report Agent** generates a final markdown research report.

The app demonstrates three Kaggle evaluation concepts.

First, it uses a **multi-agent system**: each agent owns one step of the research workflow.

Second, it uses an **MCP-style tool server**: the agents call local tools for paper search, market data loading, backtesting, and report generation.

Third, it defines reusable **agent skills** for momentum research, literature review, market data selection, backtest analysis, and quant report writing.

The final output includes a research plan, literature review, data notes, generated strategy logic, performance metrics, an equity curve, and a downloadable research report.

This is an MVP, so it intentionally keeps the first strategy narrow: cross-sectional momentum. Future versions could add more factor strategies, transaction costs, larger universes, and live paper search.

## 2-3 Minute Extended Version

The problem I wanted to solve is that early-stage quant research is repetitive. A researcher often starts with a vague idea like "momentum strategy", then has to search papers, translate the idea into rules, find data, write a backtest, interpret results, and draft a report.

This project automates that first-pass workflow.

The user starts with a simple strategy idea. In the sidebar, the app exposes the default equity universe and date range. The default demo universe includes large-cap US stocks and SPY as the benchmark.

When the pipeline runs, the system produces a research plan first. This keeps the agent grounded in a testable hypothesis instead of jumping straight into code.

Next, the Literature Agent summarizes classic momentum papers, including Jegadeesh and Titman, Asness and coauthors, and Daniel and Moskowitz. These papers are cached for demo stability, so the walkthrough remains reliable even if live search fails.

Then the Data Agent loads data. It tries yfinance first, and if live data is unavailable, it falls back to deterministic sample data. This makes the app deployable and reproducible for judging.

The Backtest Agent implements a simple monthly rebalanced 12-month momentum strategy. It ranks stocks by trailing return, selects the top names, equal weights them, and compares the result against SPY.

Finally, the Report Agent turns everything into a readable research report with thesis, literature, data, methodology, results, risks, and next steps.

The key point is that this is not just a chatbot. It is an agent workflow that plans, researches, calls tools, runs analysis, and writes a structured output.

## Recording Checklist

- [ ] Start from the Streamlit home screen.
- [ ] Show the default query: `Momentum strategy on S&P 500 stocks`.
- [ ] Point out the sidebar settings: universe, dates, and Kaggle evaluation coverage.
- [ ] Click **Run research pipeline**.
- [ ] Show the loading/status steps for each agent.
- [ ] Open the **Research Plan** tab.
- [ ] Open the **Literature** tab and show paper summaries.
- [ ] Open the **Data** tab and show data notes.
- [ ] Open the **Backtest** tab and show metrics plus equity curve.
- [ ] Open the **Report** tab and show the final markdown report.
- [ ] Open the **Evaluation Map** tab and explain the three required concepts.

## Backup Talking Points

- If live market data fails, say: "The app includes deterministic fallback data so the demo remains reproducible."
- If no OpenAI API key is configured, say: "The app can run with fallback agent outputs, but it is designed to use OpenAI when an API key is available."
- If asked about limitations, say: "The MVP does not yet include transaction costs, survivorship-bias-free constituents, or production-grade risk controls."
