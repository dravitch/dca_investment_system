# strategies/level1_dca.py

def run_level1_dca():
    """
    Article A : Dollar-Cost Averaging Simple
    
    Ce que l'utilisateur va faire :
    1. Choisir son investissement mensuel (ex: 100€)
    2. Choisir la période (1, 5, 10 ans)
    3. Comparer BTC vs Or vs Actions vs Commodités
    4. Voir graphiques et métriques
    """
    
    print("\n" + "="*60)
    print("NIVEAU 1 : DOLLAR-COST AVERAGING (DCA)")
    print("Article A : La Méthode Ultime")
    print("="*60)
    
    # Paramètres
    monthly_amount = get_user_input_float(
        "💰 Investissement mensuel (€) : ", 
        default=100
    )
    
    periods = get_user_input_periods(
        "📅 Périodes à tester (ex: 1,5,10) : ",
        default=[1, 5, 10]
    )
    
    # Choix des actifs
    print("\n🎯 Actifs à comparer :")
    print("  [1] Bitcoin (BTC)")
    print("  [2] Or (PAXG)")
    print("  [3] Actions (S&P 500)")
    print("  [4] Tous (comparaison complète)")
    
    asset_choice = input("Votre choix : ")
    
    assets = get_assets_from_choice(asset_choice)
    
    # Simulation avec progress bar
    print("\n🔄 Simulation en cours...")
    results = run_dca_simulation(
        assets=assets,
        monthly_amount=monthly_amount,
        periods=periods
    )
    
    # Affichage résultats
    display_dca_results(results, monthly_amount, periods)
    
    # Génération graphiques
    generate_dca_graphs(results, periods)
    
    # Export optionnel
    if ask_yes_no("\n💾 Exporter les résultats (CSV) ?"):
        export_results(results, "level1_dca_results.csv")
    
    print("\n" + "="*60)
    print("✅ Simulation Niveau 1 terminée !")
    print("📊 Les graphiques ont été sauvegardés")
    print("="*60)