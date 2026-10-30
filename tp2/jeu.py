"""Partie C - Jeu complet du Morpion (boucle de jeu, scores, menu)."""

from grille import Grille
from joueurs import JoueurHumain, JoueurIA, JoueurIAMalin


def jouer_partie(joueur_x, joueur_o, afficher=True):
    """Joue une partie. Renvoie "X", "O" ou None (match nul)."""
    grille = Grille()
    joueurs = {"X": joueur_x, "O": joueur_o}
    courant = "X"  # X commence

    while True:
        if afficher:
            print()
            grille.afficher()

        # Boucle de validation : le même joueur rejoue tant que le coup est invalide
        while True:
            x, y = joueurs[courant].prochain_coup(grille, courant)
            if not grille.case_valide(x, y):
                if afficher:
                    print("Coup invalide : hors grille, rejouez.")
            elif not grille.jouer(x, y, courant):
                if afficher:
                    print("Coup invalide : case déjà occupée, rejouez.")
            else:
                break  # coup accepté

        # Fin de partie ?
        if grille.est_gagnant(courant):
            if afficher:
                print()
                grille.afficher()
                print(f"\n{joueurs[courant].nom} ({courant}) gagne !")
            return courant
        if grille.est_plein():
            if afficher:
                print()
                grille.afficher()
                print("\nMatch nul.")
            return None

        courant = "O" if courant == "X" else "X"  # on change de joueur


def jouer_serie(joueur_x, joueur_o, nb_parties, afficher=True):
    """Bonus : score sur plusieurs parties. Renvoie (victoires X, victoires O, nuls)."""
    score = {"X": 0, "O": 0, None: 0}
    for _ in range(nb_parties):
        score[jouer_partie(joueur_x, joueur_o, afficher)] += 1
    return score["X"], score["O"], score[None]


def menu():
    print("=== MORPION ===")
    print("1. Humain contre IA")
    print("2. Humain contre IA maligne")
    print("3. 2 humains")
    print("4. IA contre IA (20 parties)")
    print("5. IA maligne contre IA (20 parties)")
    choix = input("Votre choix : ").strip()

    if choix == "1":
        jouer_partie(JoueurHumain("Joueur"), JoueurIA())
    elif choix == "2":
        jouer_partie(JoueurHumain("Joueur"), JoueurIAMalin())
    elif choix == "3":
        # Bonus : mode 2 humains avec score
        j1, j2 = JoueurHumain("Joueur 1"), JoueurHumain("Joueur 2")
        score = {"X": 0, "O": 0}
        while True:
            gagnant = jouer_partie(j1, j2)
            if gagnant:
                score[gagnant] += 1
            print(f"Score - X : {score['X']} | O : {score['O']}")
            if input("Rejouer ? (o/n) ").lower() != "o":
                break
    elif choix == "4":
        x, o, n = jouer_serie(JoueurIA("IA 1"), JoueurIA("IA 2"), 20, afficher=False)
        print(f"20 parties - victoires X : {x}, victoires O : {o}, nuls : {n}")
    elif choix == "5":
        x, o, n = jouer_serie(JoueurIAMalin(), JoueurIA(), 20, afficher=False)
        print(f"20 parties - maligne (X) : {x}, aléatoire (O) : {o}, nuls : {n}")
    else:
        print("Choix inconnu.")


if __name__ == "__main__":
    menu()
