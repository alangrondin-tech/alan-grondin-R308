"""TP1 R3.08 - Partie A : dictionnaire d'étudiants (nom -> note)."""


def ajouter_etudiant(d, nom, note):
    """Ajoute ou met à jour un étudiant. Lève ValueError si la note est invalide."""
    nom = str(nom).strip()
    if not nom:
        raise ValueError("Le nom ne peut pas être vide.")
    try:
        d[nom] = float(str(note).replace(",", "."))
    except (TypeError, ValueError):
        raise ValueError(f"Note invalide : {note!r}")
    return d


def moyenne_classe(d):
    """Moyenne des notes (0.0 si le dictionnaire est vide)."""
    if not d:
        return 0.0
    return sum(d.values()) / len(d)


def meilleur_etudiant(d):
    """Renvoie (nom, note) du meilleur étudiant, ou None si le dictionnaire est vide."""
    if not d:
        return None
    nom = max(d, key=d.get)
    return nom, d[nom]


def sauvegarder(d, chemin):
    """Écrit le dictionnaire (une ligne 'nom:note'). Renvoie True si OK."""
    try:
        with open(chemin, "w", encoding="utf-8") as f:
            for nom, note in d.items():
                f.write(f"{nom}:{note}\n")
        return True
    except OSError as e:
        print(f"Erreur d'écriture ({chemin}) : {e}")
        return False


def charger(chemin):
    """Charge un fichier 'nom:note'. Fichier absent/illisible -> {} ; lignes mal formées ignorées."""
    d = {}
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for i, ligne in enumerate(f, 1):
                ligne = ligne.strip()
                if not ligne:
                    continue
                if ":" not in ligne:
                    print(f"Ligne {i} ignorée (mal formée) : {ligne!r}")
                    continue
                nom, note = ligne.rsplit(":", 1)
                try:
                    ajouter_etudiant(d, nom, note)
                except ValueError as e:
                    print(f"Ligne {i} ignorée : {e}")
    except FileNotFoundError:
        pass  # fichier absent : on démarre à vide
    except OSError as e:
        print(f"Erreur de lecture ({chemin}) : {e}")
    return d


if __name__ == "__main__":
    d = {}
    for nom, note in [("Alice", 12), ("Bob", 15), ("Claire", 9.5)]:
        ajouter_etudiant(d, nom, note)
    print(f"{moyenne_classe(d):.2f}")      # 12.17
    print(meilleur_etudiant(d))            # ('Bob', 15.0)

    sauvegarder(d, "etudiants.txt")
    print(charger("etudiants.txt"))

    # cas limites : pas de plantage
    print(moyenne_classe({}), meilleur_etudiant({}))
    print(charger("fichier_inexistant.txt"))
