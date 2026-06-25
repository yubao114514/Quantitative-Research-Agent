from agents.strategy_router import detect_strategy_type, strategy_label
from quant.config import load_app_config


def recommend_research_config(query: str) -> dict:
    app_config = load_app_config()
    strategy_type = detect_strategy_type(query)
    template_key = detect_universe_template(query)
    template = app_config["universe_templates"][template_key]
    strategy_config = app_config["strategies"][strategy_type]

    return {
        "strategy_type": strategy_type,
        "strategy_label": strategy_label(strategy_type),
        "template": template_key,
        "universe": template["universe"],
        "benchmark": template["benchmark"],
        "start": app_config["default_start"],
        "end": app_config["default_end"],
        "lookback_days": strategy_config["lookback_days"],
        "rebalance": strategy_config["rebalance"],
        "top_n": strategy_config["top_n"],
        "reason": build_reason(template["reason"], strategy_label(strategy_type), strategy_config),
    }


def detect_universe_template(query: str) -> str:
    normalized = query.lower()
    if any(term in normalized for term in ["semiconductor", "chip", "chips", "nvda", "amd"]):
        return "semiconductor"
    if any(term in normalized for term in ["technology", "tech", "software", "ai stocks", "growth stocks"]):
        return "technology"
    if any(term in normalized for term in ["energy", "oil", "gas", "commodity"]):
        return "energy"
    if any(term in normalized for term in ["financial", "bank", "banks", "fintech"]):
        return "financials"
    if any(term in normalized for term in ["crypto", "bitcoin", "ethereum", "btc", "eth"]):
        return "crypto"
    return "us_equities"


def build_reason(template_reason: str, strategy_label_text: str, strategy_config: dict) -> str:
    return (
        f"{template_reason} The detected strategy is {strategy_label_text}, "
        f"using lookback={strategy_config['lookback_days']} days, "
        f"rebalance={strategy_config['rebalance']}, and top_n={strategy_config['top_n']}."
    )
