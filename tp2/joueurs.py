"""Partie B - Classes Joueur (+ bonus : JoueurIAMalin).

Tous les joueurs ont la même méthode prochain_coup(tab, symbole)
qui renvoie un tuple (x, y) avec x = ligne et y = colonne.
"""

import random


def adversaire(symbole):
    """Renvoie le symbole de l'adversaire."""
    return "O" if symbole == "X" else "X"


class JoueurHumain:
    """Joueur qui saisit son coup au clavier."""

    def __init__(self, nom="Humain"):
        self.nom = nom

    def prochain_coup(self, tab, symbole):
        saisie = input(f"{self.nom} ({symbole}) - ligne colonne (0-2), ex: 1 2 : ")
        try:
            x, y = saisie.replace(",", " ").split()
            return int(x), int(y)
        except ValueError:
            # Saisie illisible : on renvoie un coup hors grille,
            # la boucle de jeu affichera le message d'erreur.
            return (-1, -1)


class JoueurIA:
    """IA simple : joue une case libre au hasard."""

    def __init__(self, nom="IA"):
        self.nom = nom

    def prochain_coup(self, tab, symbole):
        return random.choice(tab.cases_libres())


class JoueurIAMalin(JoueurIA):
    """IA qui gagne si possible, sinon bloque l'adversaire, sinon hasard."""

    def __init__(self, nom="IA maligne"):
        super().__init__(nom)

    def _coup_gagnant(self, tab, symbole):
        """Cherche une case qui ferait gagner `symbole` (None sinon)."""
        for (x, y) in tab.cases_libres():
            essai = tab.copie()          # on simule sur une copie
            essai.jouer(x, y, symbole)
            if essai.est_gagnant(symbole):
                return (x, y)
        return None

    def prochain_coup(self, tab, symbole):
        # 1) Coup gagnant pour moi ?
        coup = self._coup_gagnant(tab, symbole)
        if coup:
            return coup
        # 2) Bloquer le coup gagnant de l'adversaire ?
        coup = self._coup_gagnant(tab, adversaire(symbole))
        if coup:
            return coup
        # 3) Sinon : hasard
        return super().prochain_coup(tab, symbole)
