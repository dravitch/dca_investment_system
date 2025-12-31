#!/usr/bin/env python3
"""
save.py - Sauvegarde Automatique GitHub
Usage: python save.py "Description des changements"
"""

import sys
import subprocess
from datetime import datetime

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def log(msg, color=RESET):
    print(f"{color}{msg}{RESET}")

def run(cmd, error_msg="Commande échouée"):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        log(f"❌ {error_msg}", RED)
        log(f"   Détails: {e.stderr}", RED)
        return False, e.stderr

def get_commit_message():
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"Mise à jour du projet DCA Investment System - {timestamp}"

def main():
    log("\n=== DCA Investment System - Sauvegarde GitHub ===", BLUE)

    log("Chargement de la clé SSH dravitch...", BLUE)
    success, _ = run("ssh-add ~/.ssh/id_ed25519", "Impossible de charger la clé SSH")
    if not success:
        return 1
    log("OK Clé SSH chargée", GREEN)

    log("Test de connexion SSH avec GitHub...", BLUE)
    success, output = run(
        "ssh -T git@github.com-dravitch",
        "Connexion SSH échouée"
    )
    if "Hi dravitch!" in output:
        log("OK Connexion SSH avec dravitch", GREEN)
    else:
        log("ERREUR: La clé SSH ne correspond pas au compte dravitch", RED)
        return 1

    success, output = run("git remote -v", "Impossible de lire le remote")
    if not success or "dravitch/dca_investment_system" not in output:
        log("ERREUR: Remote 'origin' non configuré vers dravitch/dca_investment_system", RED)
        return 1
    log("OK Remote configuré:", GREEN)
    log(output, BLUE)

    log("\nSynchronisation avec le distant...", BLUE)
    run("git fetch origin", "Fetch échoué")
    run("git pull origin main --rebase", "Pull --rebase échoué")

    run("git add .", "Impossible d'ajouter les fichiers")
    commit_message = get_commit_message()
    success, _ = run(f'git commit -m "{commit_message}"', "Impossible de créer le commit")
    if not success:
        log("Aucun commit créé (peut-être rien à valider)", YELLOW)

    success, _ = run("git push origin main", "Impossible de pousser vers GitHub")
    if success:
        log("OK Modifications sauvegardées sur GitHub", GREEN)
        log(f"Message: {commit_message}", BLUE)
        log("Voir sur GitHub: https://github.com/dravitch/dca_investment_system", BLUE)

    return 0

if __name__ == "__main__":
    sys.exit(main())
