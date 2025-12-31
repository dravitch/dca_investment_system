"""
backtest_engine.py
Moteur de simulation DCA / rebalancement.
"""

from typing import Any, Dict, Callable


def run_backtest(
    price_data: Any,
    strategy_fn: Callable,
    config: Dict,
    assets_config: Dict,
) -> Dict:
    """
    Exécute un backtest générique pour une stratégie de DCA / rebalancement.
    """
    raise NotImplementedError("run_backtest n'est pas encore implémenté.")
