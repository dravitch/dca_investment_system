"""
asset_config.py
Configuration des actifs (BTC, PAXG, OR, SPY, etc.)
"""

ASSETS = {
    "BTC": {
        "symbol": "BTC-USD",
        "class": "crypto",
        "weight_target": 0.25,
    },
    "PAXG": {
        "symbol": "PAXG-USD",
        "class": "crypto_gold",
        "weight_target": 0.25,
    },
    "OR": {
        "symbol": "GC=F",
        "class": "commodity_gold",
        "weight_target": 0.25,
    },
    "SPY": {
        "symbol": "SPY",
        "class": "equity_etf",
        "weight_target": 0.25,
    },
}
