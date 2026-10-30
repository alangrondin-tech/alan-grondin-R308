"""Tests automatiques : jeux d'essai du sujet (parties A, B, C et bonus)."""

from grille import Grille
from joueurs import JoueurIA, JoueurIAMalin, JoueurHumain
from jeu import jouer_partie, jouer_serie
from unittest import mock


def grille_depuis(texte):
    """Construit une grille depuis 'XX_/_O_/___'."""
    g = Grille()
    for i, ligne in enumerate(texte.split("/")):
        for k, c in enumerate(ligne):
            if c != "_":
                g.jouer(i, k, c)
    return g


# Partie A
g = Grille()
assert g.jouer(0, 0, "X") and g.jouer(0, 1, "O") and g.jouer(1, 1, "X")
assert not g.jouer(0, 0, "O")          # occupée
assert not g.jouer(3, 0, "O")          # hors grille
assert not g.est_gagnant("X")
g.jouer(2, 2, "X")
assert g.est_gagnant("X")              # diagonale
assert not g.est_plein()

# Partie B : coups de l'IA toujours valides
g = Grille()
assert JoueurIA().prochain_coup(g, "X") in g.cases_libres()

# Partie C : coup invalide -> le même joueur rejoue (saisies : hors grille, puis valide...)
with mock.patch("builtins.input", side_effect=["3 0", "abc", "0 0"] + ["1 1"] * 0):
    h = JoueurHumain()
    assert h.prochain_coup(Grille(), "X") == (3, 0)
    assert h.prochain_coup(Grille(), "X") == (-1, -1)
    assert h.prochain_coup(Grille(), "X") == (0, 0)

# IA contre IA : 20 parties, victoire ou nul à chaque fois
x, o, n = jouer_serie(JoueurIA(), JoueurIA(), 20, afficher=False)
assert x + o + n == 20

# Bonus : IA maligne
m = JoueurIAMalin()
assert m.prochain_coup(grille_depuis("XX_/_O_/___"), "O") == (0, 2)  # bloque
assert m.prochain_coup(grille_depuis("OO_/XX_/___"), "O") == (0, 2)  # gagne

# L'IA maligne ne doit jamais perdre contre le hasard (en jouant X, 200 parties)
x, o, n = jouer_serie(JoueurIAMalin(), JoueurIA(), 200, afficher=False)
print(f"maligne(X) vs hasard : {x} victoires, {o} défaites, {n} nuls")

print("Tous les tests passent.")
