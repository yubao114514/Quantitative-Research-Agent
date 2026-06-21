from agents.llm import call_llm


def create_research_plan(query: str) -> str:
    fallback = f"""
### Objective
Evaluate whether a simple cross-sectional momentum strategy can create persistent excess returns for a large-cap US equity universe.

### User Query
`{query}`

### Agent Plan
1. Translate the strategy idea into a testable hypothesis.
2. Review classic academic evidence on momentum and implementation risk.
3. Select a practical equity universe and benchmark.
4. Run a monthly rebalanced 12-month momentum backtest.
5. Compare the result with SPY and summarize risks, limitations, and next research steps.
"""
    return call_llm(
        "You are a quant research planning agent. Produce concise, testable research plans.",
        f"Create a research plan for: {query}",
        fallback.strip(),
    )
