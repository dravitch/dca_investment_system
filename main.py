"""
main.py
Point d'entrée unique avec menu.
"""

from config.settings import BACKTEST_CONFIG
from config.asset_config import ASSETS


# main.py - Exemple conceptuel

def main():
    """Point d'entrée unique avec menu progressif"""
    
    print_welcome_banner()
    
    # Menu principal
    print("\n🎯 SYSTÈME D'INVESTISSEMENT CONSCIENT")
    print("=" * 60)
    print("\nÀ quel niveau êtes-vous ?")
    print("\n  [1] Niveau 1 : DCA Simple (Article A)")
    print("      → Accumulation disciplinée Bitcoin")
    print("      → Pour : Débutants, maximalistes BTC")
    print()
    print("  [2] Niveau 2 : Rebalancement Classique (Article B)")
    print("      → Portfolio 60/40 BTC/PAXG")
    print("      → Pour : Intermédiaires cherchant stabilité")
    print()
    print("  [3] Niveau 2.5 : Rebalancement Dynamique (Article C)")
    print("      → Stratégies adaptatives (Momentum, Volatilité...)")
    print("      → Pour : Avancés optimisant leur système")
    print()
    print("  [4] Comparaison Globale (Tous les niveaux)")
    print("      → Comparer DCA vs Rebalancement vs Dynamique")
    print()
    print("  [5] Mode Recherche (Expérimentation)")
    print("      → Tester vos propres paramètres")
    print()
    
    choice = input("Votre choix (1-5) : ")
    
    # Routage vers le niveau approprié
    if choice == "1":
        run_level1_dca()
    elif choice == "2":
        run_level2_rebalance()
    elif choice == "3":
        run_level25_dynamic()
    elif choice == "4":
        run_global_comparison()
    elif choice == "5":
        run_research_mode()
    else:
        print("❌ Choix invalide")
        return
    
    # Proposition de progression
    suggest_next_level(choice)

def suggest_next_level(current_level):
    """Suggère le niveau suivant"""
    suggestions = {
        "1": "\n💡 Prêt à réduire la volatilité ? Explorez le Niveau 2 (Rebalancement)",
        "2": "\n💡 Vous maîtrisez le rebalancement ? Découvrez le Niveau 2.5 (Dynamique)",
        "3": "\n🎓 Vous êtes au sommet ! Explorez le Mode Recherche pour aller plus loin"
    }
    
    if current_level in suggestions:
        print(suggestions[current_level])
        print("📚 Lire l'article : [lien vers article suivant]")


if __name__ == "__main__":
    main()
    ensure_not_tracked()

