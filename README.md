# DCA Investment System

Système modulaire pour tester des stratégies de DCA et de rebalancement sur plusieurs actifs (BTC, PAXG, OR, SPY, etc.).

## Structure

- `config/` : configuration globale et des actifs
- `core/` : moteur de backtest, récupération de données, métriques
- `strategies/` : implémentations des différentes stratégies (Article A, B, C)
- `ui/` : affichage console et graphiques
- `main.py` : point d'entrée avec menu

## Installation rapide

```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
pip install -r requirements.txt
python main.py
```
