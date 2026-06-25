def detect_strategy_type(query: str) -> str:
    """Route the user's research idea to the closest implemented strategy."""
    normalized = query.lower()
    if any(term in normalized for term in ["mean reversion", "reversal", "oversold", "short-term loser"]):
        return "mean_reversion"
    return "momentum"


def strategy_label(strategy_type: str) -> str:
    labels = {
        "momentum": "Momentum",
        "mean_reversion": "Mean Reversion",
    }
    return labels.get(strategy_type, "Momentum")
