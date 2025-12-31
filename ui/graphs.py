"""
graphs.py
Génération de graphiques matplotlib (equity curve, drawdown, allocations, etc.)
"""

from typing import Dict, Any


def plot_equity_curve(result: Dict) -> None:
    """Trace l'equity curve."""
    raise NotImplementedError


def plot_allocations(result: Dict) -> None:
    """Trace l'évolution des allocations."""
    raise NotImplementedError
