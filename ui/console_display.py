"""
console_display.py
Affichage console (tableaux, progress bars)
"""

from typing import Any, Dict


def display_backtest_summary(result: Dict) -> None:
    """Affiche un résumé du backtest sous forme de tableau texte."""
    raise NotImplementedError


def display_progress(current: int, total: int) -> None:
    """Affiche une barre de progression simple."""
    raise NotImplementedError
