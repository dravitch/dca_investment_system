"""
metrics.py
Calculs métriques (ROI, Sharpe, volatilité, drawdown, etc.)
"""

from typing import Any


def compute_roi(equity_curve: Any) -> float:
    """Calcule le retour sur investissement total."""
    raise NotImplementedError


def compute_sharpe(equity_curve: Any, risk_free_rate: float = 0.0) -> float:
    """Calcule le ratio de Sharpe."""
    raise NotImplementedError


def compute_volatility(equity_curve: Any) -> float:
    """Calcule la volatilité annualisée."""
    raise NotImplementedError
