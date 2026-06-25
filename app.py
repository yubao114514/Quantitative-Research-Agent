import os
from datetime import date

import plotly.graph_objects as go
import streamlit as st

from agents.orchestrator import run_research_pipeline


DEFAULT_QUERY = "Momentum strategy on S&P 500 stocks"


st.set_page_config(
    page_title="Quantitative Research Assistant",
    page_icon="Q",
    layout="wide",
)

st.title("Quantitative Research Assistant")
st.caption("From strategy idea to literature review, backtest, and research report.")

with st.sidebar:
    st.header("Demo Settings")
    tickers = st.text_area(
        "Universe",
        "AAPL, MSFT, NVDA, AMZN, META, GOOGL, JPM, XOM, UNH, SPY",
        height=92,
    )
    start = st.date_input("Start date", value=date(2018, 1, 1))
    end = st.date_input("End date", value=date(2025, 12, 31))
    st.divider()
    st.markdown("**Kaggle Evaluation Coverage**")
    st.checkbox("Agent / Multi-agent system", value=True, disabled=True)
    st.checkbox("MCP Server", value=True, disabled=True)
    st.checkbox("Agent skills", value=True, disabled=True)

has_llm_key = bool(os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY"))
if not has_llm_key:
    st.warning(
        "No LLM API key found. Set GEMINI_API_KEY or OPENAI_API_KEY for live agent writing; otherwise the app uses deterministic fallback outputs."
    )

query = st.text_input("Strategy idea", value=DEFAULT_QUERY)
run_button = st.button("Run research pipeline", type="primary")

if run_button:
    ticker_list = [ticker.strip().upper() for ticker in tickers.split(",") if ticker.strip()]
    with st.status("Running multi-agent research pipeline...", expanded=True) as status:
        st.write("Research Planner is creating the study plan.")
        result = run_research_pipeline(
            query=query,
            tickers=ticker_list,
            start=str(start),
            end=str(end),
        )
        st.write("Literature Agent summarized relevant papers.")
        st.write("Data Agent selected the market data source.")
        st.write("Backtest Agent ran the momentum simulation.")
        st.write("Report Agent drafted the research report.")
        status.update(label="Research pipeline complete", state="complete")

    tabs = st.tabs(
        [
            "Research Plan",
            "Literature",
            "Data",
            "Backtest",
            "Report",
            "Evaluation Map",
        ]
    )

    with tabs[0]:
        st.caption(f"Detected strategy: {result['strategy_label']}")
        st.subheader("Research Plan")
        st.markdown(result["research_plan"])

    with tabs[1]:
        st.subheader("Literature Review")
        for paper in result["papers"]:
            with st.expander(paper["title"], expanded=True):
                st.markdown(f"**Citation:** {paper['citation']}")
                st.markdown(paper["summary"])

    with tabs[2]:
        st.subheader("Data Source Notes")
        st.markdown(result["data_notes"])
        st.dataframe(result["prices"].tail(10), use_container_width=True)

    with tabs[3]:
        st.subheader("Backtest Results")
        metrics = result["metrics"]
        cols = st.columns(5)
        cols[0].metric("Total Return", f"{metrics['total_return']:.1%}")
        cols[1].metric("Annual Return", f"{metrics['annualized_return']:.1%}")
        cols[2].metric("Volatility", f"{metrics['volatility']:.1%}")
        cols[3].metric("Sharpe", f"{metrics['sharpe_ratio']:.2f}")
        cols[4].metric("Max Drawdown", f"{metrics['max_drawdown']:.1%}")

        curve = result["equity_curve"]
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=curve.index,
                y=curve["strategy"],
                mode="lines",
                name="Momentum strategy",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=curve.index,
                y=curve["benchmark"],
                mode="lines",
                name="SPY benchmark",
            )
        )
        fig.update_layout(
            height=440,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Growth of $1",
            legend=dict(orientation="h"),
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Generated Strategy Logic")
        st.code(result["generated_code"], language="python")

    with tabs[4]:
        st.subheader("Final Research Report")
        st.markdown(result["report"])
        st.download_button(
            "Download report",
            data=result["report"],
            file_name="quantitative_research_report.md",
            mime="text/markdown",
        )

    with tabs[5]:
        st.subheader("Kaggle Evaluation Map")
        st.markdown(result["evaluation_map"])
else:
    st.info("Enter a strategy idea and run the pipeline. The default query is ready for demo.")
