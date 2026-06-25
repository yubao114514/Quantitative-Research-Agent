def detect_strategy_type(query: str) -> str:
    """Route the user's research idea to the closest implemented strategy."""
    normalized = query.lower()
    if any(term in normalized for term in ["mean reversion", "reversal", "oversold", "short-term loser"]):
        return "mean_reversion"
    return "momentum"


def strategy_label(strategy_type: str) -> str:
    from quant.config import load_app_config

    strategies = load_app_config()["strategies"]
    return strategies.get(strategy_type, strategies["momentum"])["label"]
