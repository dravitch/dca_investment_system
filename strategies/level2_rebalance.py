# strategies/level25_dynamic.py

def run_level25_dynamic():
    """
    Article C : Rebalancement Dynamique
    
    Ce que l'utilisateur va faire :
    1. Choisir sa stratégie (Momentum, Volatilité, Composite...)
    2. Définir ses paramètres (ou utiliser les défauts optimisés)
    3. Comparer avec rebalancement classique
    4. Voir l'allocation dynamique BTC au fil du temps
    """
    
    print("\n" + "="*60)
    print("NIVEAU 2.5 : REBALANCEMENT DYNAMIQUE INTELLIGENT")
    print("Article C : La Supériorité du Momentum Adaptatif")
    print("="*60)
    
    # Choix de la stratégie
    print("\n🎯 Stratégies disponibles :")
    print("  [1] Momentum Adaptatif (Recommandé)")
    print("  [2] Volatilité Adaptative")
    print("  [3] Corrélation Adaptative")
    print("  [4] Suivi de Trend")
    print("  [5] Composite Intelligent")
    print("  [6] Toutes (comparaison)")
    
    strategy_choice = input("Votre choix : ")
    
    strategies = get_strategies_from_choice(strategy_choice)
    
    # Paramètres avancés (optionnel)
    use_advanced = ask_yes_no("\n⚙️  Configurer les paramètres avancés ?")
    
    if use_advanced:
        params = configure_advanced_params()
    else:
        params = get_default_params()
        print("✓ Utilisation des paramètres optimisés par défaut")
    
    # Simulation
    print("\n🔄 Simulation des stratégies dynamiques...")
    print("⏱️  Cela peut prendre 30-60 secondes...")
    
    results = run_dynamic_simulation(
        strategies=strategies,
        params=params,
        periods=[3, 5, 7]  # Périodes intermédiaires pour voir l'effet
    )
    
    # Affichage détaillé
    display_dynamic_results(results)
    
    # Graphiques comparatifs
    print("\n📊 Génération des visualisations...")
    generate_dynamic_graphs(results)
    
    # Allocation BTC au fil du temps (feature clé)
    plot_btc_allocation_timeline(results['Momentum Adaptatif'])
    
    # Recommandations personnalisées
    print("\n💡 RECOMMANDATIONS PERSONNALISÉES")
    print("="*60)
    
    best_strategy = find_best_strategy(results)
    print(f"\n✓ Stratégie optimale : {best_strategy['name']}")
    print(f"  → CAGR: {best_strategy['cagr']:.1f}%")
    print(f"  → Sharpe: {best_strategy['sharpe']:.2f}")
    print(f"  → Max DD: {best_strategy['max_dd']:.1f}%")
    
    print("\n🎯 PLAN D'ACTION :")
    print(f"  1. Commencez avec {best_strategy['name']}")
    print("  2. Vérifiez mensuellement les performances BTC/PAXG (90j)")
    print("  3. Ajustez l'allocation selon les règles (10 min/mois)")
    print("  4. Rebalancez trimestriellement si écart > 5%")
    
    print("\n" + "="*60)
    print("✅ Simulation Niveau 2.5 terminée !")
    print("📈 Vous êtes maintenant un investisseur conscient avancé")
    print("="*60)
```
