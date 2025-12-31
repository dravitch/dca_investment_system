"""
data_fetcher.py
DQF + acquisition données (Yahoo, Polygon, etc.)
"""

from typing import Dict, Any


def fetch_historical_data(symbol: str, source: str = "yahoo") -> Any:
    """
    Récupère les données historiques pour un symbole donné.
    TODO: implémenter intégration Yahoo / Polygon.
    """
    raise NotImplementedError("fetch_historical_data n'est pas encore implémenté.")


def build_dataset(assets_config: Dict[str, Any]) -> Any:
    """
    Construit un dataset multi-actifs à partir de la configuration.
    """
    raise NotImplementedError("build_dataset n'est pas encore implémenté.")
