"""TP1 R3.08 - Partie C : manipulation des mots."""
import random
import unicodedata

MOTS_PAR_DEFAUT = ["python", "reseau", "routeur", "protocole", "serveur",
                   "ordinateur", "algorithme", "variable", "fonction", "éléphant"]


def charger_mots(chemin="mots.txt"):
    """Charge un mot par ligne ; si le fichier est absent/vide, liste par défaut."""
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            mots = [l.strip() for l in f if l.strip()]
        return mots or list(MOTS_PAR_DEFAUT)
    except OSError:
        return list(MOTS_PAR_DEFAUT)


def choisir_mot(liste):
    """Renvoie un mot de la liste en MAJUSCULES."""
    return random.choice(liste).strip().upper()


def masque(mot):
    """Liste de '_' de même longueur que le mot."""
    return ["_"] * len(mot)


def sans_accent(c):
    """'É' -> 'E' (permet de proposer E pour ÉLÉPHANT)."""
    return unicodedata.normalize("NFD", c).encode("ascii", "ignore").decode() or c


if __name__ == "__main__":
    print(masque("PYTHON"))             # ['_', '_', '_', '_', '_', '_']
    print(choisir_mot(charger_mots()))
    print(choisir_mot(["Python"]))      # PYTHON
