#!/usr/bin/env python3

"""Listes simplements chainees + quelques operations"""

import traceur


class Cellule:
    """Une cellule d'une liste chaînée"""

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

    def __str__(self):
        return "cellule_" + str(self.valeur)


class ListeSimplementChainee:
    """Une liste simplement chainee."""

    def __init__(self):
        self.tete = None
        self.queue = None
        self.taille = 0

    def __str__(self):
        """Renvoie val1 --> val2 --> val3 ..."""
        return " --> ".join([str(c.valeur) for c in recupere_cellules(self)])


def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tete"""
    # Temps constant
    liste_chainee.taille += 1
    liste_chainee.tete = Cellule(valeur, liste_chainee.tete)
    if liste_chainee.queue is None:
        liste_chainee.queue = liste_chainee.tete
    return liste_chainee


def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une cellule en queue."""
    # Possible en temps constant grace au pointeur de queue.
    liste_chainee.taille += 1
    cellule = Cellule(valeur, None)
    if liste_chainee.queue is not None:
        liste_chainee.queue.suivant = cellule
    else:
        liste_chainee.tete = cellule
    liste_chainee.queue = cellule
    return liste_chainee


def recupere_cellules(liste_chainee):
    """Renvoie un vecteur contenant toutes les cellules de la liste_chainee"""
    vecteur = []
    cellule = liste_chainee.tete
    while(cellule is not None):
        vecteur.append(cellule)
        cellule = cellule.suivant
    return vecteur


def recherche(liste_chainee, valeur):
    """Recherche une valeur dans la liste_chainee donnée.

    Renvoie la premiere cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    cellule = liste_chainee.tete
    while(cellule is not None):
        if cellule.valeur == valeur:
            return cellule
        cellule = cellule.suivant
    return None


def supprime(liste_chainee, valeur):
    """Enleve la premiere cellule contenant la valeur donnée."""
    if(liste_chainee.tete is None):  # Cas pas d'éléments
        return liste_chainee
    if(liste_chainee.tete.valeur == valeur):  # Cas suppression de la tête
        liste_chainee.taille -= 1
        if liste_chainee.tete.suivant is None:  # Cas suppression seul élément
            liste_chainee.tete = None
            liste_chainee.queue = None
            return liste_chainee
        liste_chainee.tete = liste_chainee.tete.suivant
        return liste_chainee
    if liste_chainee.tete.suivant is None:  # Cas un seul élément à garder
        return liste_chainee

    # Cas avec minimum 2 cellules et la tête est à garder :
    cellule = liste_chainee.tete.suivant
    prec = liste_chainee.tete
    while(cellule is not None):
        if cellule.valeur == valeur:
            liste_chainee.taille -= 1
            prec.suivant = cellule.suivant  # Suppression
            if prec.suivant is None:  # cas de la queue
                liste_chainee.queue = prec
            return liste_chainee
        prec = cellule
        cellule = cellule.suivant
    return liste_chainee


def test_listes():
    """On teste les operations de base, dans differentes configurations."""
    liste_chainee = ListeSimplementChainee()
    traceur.display_instance(liste_chainee,
                             visualize=False,
                             image_name="liste_chainee_0")
    ajoute_en_tete(liste_chainee, 3)
    ajoute_en_tete(liste_chainee, 5)
    ajoute_en_tete(liste_chainee, 2)
    ajoute_en_tete(liste_chainee, 4)
    print("liste_chainee : ", liste_chainee)
    traceur.display_instance(liste_chainee,
                             visualize=False,
                             image_name="liste_chainee_1")
    print("recherche : ", recherche(liste_chainee, 3).valeur)
    supprime(liste_chainee, 5)
    print("apres suppression de 5 : ", liste_chainee)
    traceur.display_instance(liste_chainee,
                             visualize=False,
                             image_name="liste_chainee_2")
    supprime(liste_chainee, 4)
    print("apres suppression de 4 : ", liste_chainee)
    traceur.display_instance(liste_chainee,
                             visualize=False,
                             image_name="liste_chainee_3")


if __name__ == "__main__":
    test_listes()
