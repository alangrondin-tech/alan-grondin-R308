"""Partie A - Classe Grille du jeu de Morpion.

Convention de coordonnées : (x, y) = (ligne, colonne), de 0 à 2.
Exemple : (0, 1) = première ligne, deuxième colonne.
"""

TAILLE = 3  # taille de la grille (3x3)
VIDE = " "  # contenu d'une case libre


class Grille:
    """Grille 3x3 représentée par une liste de listes."""

    def __init__(self):
        # Chaque case contient " " (libre), "X" ou "O"
        self.cases = [[VIDE] * TAILLE for _ in range(TAILLE)]

    def afficher(self):
        """Affiche la grille de façon lisible."""
        lignes = []
        for ligne in self.cases:
            lignes.append(" " + " | ".join(ligne))
        # Les lignes de la grille sont séparées par des tirets
        print("\n---------\n".join(lignes))

    def case_valide(self, x, y):
        """True si (x, y) est dans la grille (sinon : hors grille)."""
        return 0 <= x < TAILLE and 0 <= y < TAILLE

    def jouer(self, x, y, joueur):
        """Place le symbole du joueur en (x, y).

        Retourne True si le coup est accepté, False s'il est refusé
        (case hors grille ou déjà occupée).
        """
        if not self.case_valide(x, y):
            return False  # hors grille
        if self.cases[x][y] != VIDE:
            return False  # case occupée
        self.cases[x][y] = joueur
        return True

    def est_gagnant(self, j):
        """True si le joueur j a aligné 3 symboles (ligne, colonne, diagonale)."""
        # Les 3 lignes
        for i in range(TAILLE):
            if all(self.cases[i][k] == j for k in range(TAILLE)):
                return True
        # Les 3 colonnes
        for k in range(TAILLE):
            if all(self.cases[i][k] == j for i in range(TAILLE)):
                return True
        # Diagonale descendante (haut-gauche -> bas-droite)
        if all(self.cases[i][i] == j for i in range(TAILLE)):
            return True
        # Diagonale montante (haut-droite -> bas-gauche)
        if all(self.cases[i][TAILLE - 1 - i] == j for i in range(TAILLE)):
            return True
        return False

    def est_plein(self):
        """True si aucune case libre."""
        return all(c != VIDE for ligne in self.cases for c in ligne)

    def cases_libres(self):
        """Liste des (x, y) encore libres (utile pour les IA)."""
        return [(x, y) for x in range(TAILLE) for y in range(TAILLE)
                if self.cases[x][y] == VIDE]

    def copie(self):
        """Copie indépendante de la grille (pour simuler des coups)."""
        g = Grille()
        g.cases = [ligne[:] for ligne in self.cases]
        return g


if __name__ == "__main__":
    # Jeu d'essai du sujet
    g = Grille()
    g.jouer(0, 0, "X")
    g.jouer(0, 1, "O")
    g.jouer(1, 1, "X")
    g.afficher()
    print("jouer(0,0,'O') ->", g.jouer(0, 0, "O"), "(refusé : occupée)")
    print("jouer(3,0,'O') ->", g.jouer(3, 0, "O"), "(refusé : hors grille)")
    print("est_gagnant('X') ->", g.est_gagnant("X"))
    g.jouer(2, 2, "X")
    print("après jouer(2,2,'X') ->", g.est_gagnant("X"))
