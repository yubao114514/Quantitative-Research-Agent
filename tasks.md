# Quant Research Assistant Tasks

## Day 1: Define the MVP

- [x] Confirm project name, one-line pitch, and target user.
- [x] Choose the first demo query: `Momentum strategy on S&P 500 stocks`.
- [x] Define the expected final output: research summary, data notes, backtest code, metrics, and report.
- [x] Decide the first supported strategy family: momentum only.
- [x] Write a short problem statement for the Kaggle submission.

## Day 2: Design the Agent Workflow

- [x] Map the workflow: user query -> research planning -> paper search -> summary -> data selection -> backtest code -> report.
- [x] Define each agent role:
  - Research Planner
  - Literature Summarizer
  - Data Finder
  - Backtest Generator
  - Report Writer
- [x] Decide what each agent receives and returns.
- [x] Create a simple prompt template for each agent.

## Day 3: Build the App Skeleton

- [x] Choose the app framework: Streamlit for fastest MVP, or Next.js for a polished web app.
- [x] Create the main input page.
- [x] Add sections for research summary, data source, generated code, performance chart, and final report.
- [x] Add a sample hardcoded run for the momentum strategy.

## Day 4: Add Research and Paper Search

- [ ] Connect a paper search source such as Semantic Scholar or arXiv.
- [x] Cache a small set of classic quant papers for reliable demos.
- [x] Summarize each paper into thesis, method, data, findings, and limitations.
- [x] Rank papers by relevance to the user's query.

## Day 5: Add Data and Backtest Logic

- [x] Use yfinance or a local sample dataset for the first version.
- [x] Implement a simple momentum strategy:
  - Calculate trailing returns.
  - Rank assets.
  - Select top performers.
  - Rebalance monthly.
- [x] Calculate core metrics:
  - Total return
  - Annualized return
  - Volatility
  - Sharpe ratio
  - Max drawdown
- [x] Generate a basic equity curve chart.

## Day 6: Generate the Research Report

- [x] Create a markdown report template.
- [x] Fill the report with strategy thesis, literature review, data source, backtest methodology, results, risks, and next steps.
- [x] Add a download/export option if time allows.
- [x] Make the final report readable enough for a recruiter or judge.

## Day 7: Polish the Demo

- [x] Improve the UI copy and layout.
- [x] Add loading states for each agent step.
- [x] Add one clear example run.
- [x] Prepare a short demo script.
- [x] Record or rehearse the final Kaggle walkthrough.

## Stretch Goals

- [ ] Add support for mean reversion strategies.
- [ ] Add support for value or quality factor strategies.
- [ ] Add citations in the final report.
- [ ] Add code export as a notebook.
- [ ] Add comparison against a benchmark such as SPY.
- [ ] Add a simple memory layer for previous research sessions.

## Submission Checklist

- [ ] Working app or notebook.
- [x] Clear README.
- [x] Demo query with reproducible output.
- [ ] Screenshots or demo video.
- [x] Explanation of agent architecture.
- [x] Limitations and future improvements section.
