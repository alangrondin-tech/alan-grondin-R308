"""TP1 R3.08 - Partie B : « Devine le nombre » (avec bonus rejouabilité et bornes)."""
import random

ESSAIS_MAX = 10


def lire_entier(message, defaut=None):
    """Demande un entier, redemande tant que l'entrée est invalide."""
    while True:
        saisie = input(message).strip()
        if saisie == "" and defaut is not None:
            return defaut
        try:
            return int(saisie)
        except ValueError:
            print("Veuillez entrer un nombre entier.")


def jouer(bas=1, haut=100):
    secret = random.randint(bas, haut)
    for essai in range(1, ESSAIS_MAX + 1):
        n = lire_entier(f"Essai {essai}/{ESSAIS_MAX} - votre proposition ({bas}-{haut}) : ")
        if n < secret:
            print("Trop petit")
        elif n > secret:
            print("Trop grand")
        else:
            print(f"Gagné en {essai} essai(s) !")
            return True
    print(f"Perdu, le nombre était {secret}.")
    return False


def main():
    bas, haut = 1, 100
    if input("Bornes personnalisées ? (o/n) ").strip().lower() == "o":
        bas = lire_entier("Borne basse : ")
        haut = lire_entier("Borne haute : ")
        if bas >= haut:
            print("Bornes invalides, utilisation de 1-100.")
            bas, haut = 1, 100
    while True:
        jouer(bas, haut)
        if input("Rejouer ? (o/n) ").strip().lower() != "o":
            break


if __name__ == "__main__":
    main()
