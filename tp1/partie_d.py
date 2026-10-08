"""TP1 R3.08 - Partie D : jeu du Pendu (+ Jeu 1 hall of fame, Jeu 2 tournoi, bonus ASCII art)."""
import getpass

from partie_a import charger, sauvegarder
from partie_c import charger_mots, choisir_mot, masque, sans_accent

ERREURS_MAX = 7
FICHIER_SCORES = "scores.txt"

PENDU = [
    "\n\n\n\n\n\n=========",
    "\n      |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]


def jouer_pendu(mot):
    """Joue une partie. Renvoie True si gagné."""
    mot = mot.strip().upper()
    etat = masque(mot)
    # lettres non alphabétiques (tiret, espace...) révélées d'office
    for i, c in enumerate(mot):
        if not c.isalpha():
            etat[i] = c
    erreurs = 0
    proposees = []

    while "_" in etat and erreurs < ERREURS_MAX:
        print(PENDU[erreurs])
        print("Mot :", " ".join(etat))
        print(f"Erreurs : {erreurs}/{ERREURS_MAX}")
        print("Lettres proposées :", " ".join(proposees) if proposees else "-")

        saisie = input("Une lettre : ").strip().upper()
        if len(saisie) != 1 or not saisie.isalpha():
            print("Entrez une seule lettre.")
            continue
        lettre = sans_accent(saisie)
        if lettre in proposees:
            print("Lettre déjà proposée.")  # pas d'erreur de plus
            continue
        proposees.append(lettre)

        positions = [i for i, c in enumerate(mot) if sans_accent(c) == lettre]
        if positions:
            for i in positions:
                etat[i] = mot[i]
        else:
            erreurs += 1

    if "_" not in etat:
        print("Mot :", " ".join(etat))
        print("Gagné !")
        return True
    print(PENDU[erreurs])
    print(f"Perdu, le mot était {mot}")
    return False


def enregistrer_victoire(nom):
    scores = charger(FICHIER_SCORES)
    scores[nom] = scores.get(nom, 0.0) + 1
    sauvegarder(scores, FICHIER_SCORES)


def main():
    nom = input("Votre nom : ").strip() or "Anonyme"
    mots = charger_mots()
    print("Scores actuels :", charger(FICHIER_SCORES))

    while True:
        mode = input("Mot choisi par (o)rdinateur ou par un (v)oisin ? [o/v] ").strip().lower()
        if mode == "v":
            mot = getpass.getpass("Mot du voisin (saisie masquée) : ").strip()
            if not mot:
                print("Mot vide, tirage aléatoire.")
                mot = choisir_mot(mots)
        else:
            mot = choisir_mot(mots)

        if jouer_pendu(mot):
            enregistrer_victoire(nom)
        if input("Rejouer ? (o/n) ").strip().lower() != "o":
            break
    print("Hall of fame :", charger(FICHIER_SCORES))


if __name__ == "__main__":
    main()
