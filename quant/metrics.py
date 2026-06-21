import numpy as np
import pandas as pd


def calculate_metrics(returns: pd.Series) -> dict:
    returns = returns.dropna()
    if returns.empty:
        return {
            "total_return": 0.0,
            "annualized_return": 0.0,
            "volatility": 0.0,
            "sharpe_ratio": 0.0,
            "max_drawdown": 0.0,
        }

    equity = (1 + returns).cumprod()
    total_return = equity.iloc[-1] - 1
    years = max(len(returns) / 252, 1 / 252)
    annualized_return = equity.iloc[-1] ** (1 / years) - 1
    volatility = returns.std() * np.sqrt(252)
    sharpe_ratio = annualized_return / volatility if volatility else 0.0
    drawdown = equity / equity.cummax() - 1
    return {
        "total_return": float(total_return),
        "annualized_return": float(annualized_return),
        "volatility": float(volatility),
        "sharpe_ratio": float(sharpe_ratio),
        "max_drawdown": float(drawdown.min()),
    }
