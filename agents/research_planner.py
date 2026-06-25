from agents.llm import call_llm


def create_research_plan(query: str, strategy_label: str, benchmark: str) -> str:
    fallback = f"""
### Objective
Evaluate whether a {strategy_label.lower()} strategy can create persistent excess returns for the selected universe.

### User Query
`{query}`

### Agent Plan
1. Translate the strategy idea into a testable hypothesis.
2. Review relevant academic evidence and implementation risk.
3. Select a practical equity universe and benchmark.
4. Run the configured {strategy_label.lower()} backtest.
5. Compare the result with {benchmark} and summarize risks, limitations, and next research steps.
"""
    return call_llm(
        "You are a quant research planning agent. Produce concise, testable research plans.",
        f"Create a research plan for: {query}\nStrategy type: {strategy_label}\nBenchmark: {benchmark}",
        fallback.strip(),
    )
