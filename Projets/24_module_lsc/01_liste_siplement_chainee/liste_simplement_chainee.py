#!/usr/bin/env python3

"""Listes simplement chaînées + quelques operations."""

import traceur


class Cellule:
    """Une cellule d'une liste."""

    # TODO
    ...


class ListeSimplementChainee:
    """Une liste simplement chaînée."""

    # TODO
    ...


def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tête."""
    # TODO
    ...


def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une cellule en queue."""
    # TODO
    ...


def recherche(liste_chainee, valeur):
    """Recherche une valeur dans la liste_chainee donnée.

    Renvoie la première cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    # TODO
    ...




def supprime(liste_chainee, valeur):
    """Supprime la premiere cellule contenant la valeur donnée."""
    # TODO
    ...


def teste_listes():
    """On teste les operations de base, dans différentes configurations."""
    liste_chainee = ListeSimplementChainee()
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_0"
    )
    ajoute_en_tete(liste_chainee, 3)
    ajoute_en_tete(liste_chainee, 5)
    ajoute_en_tete(liste_chainee, 2)
    ajoute_en_tete(liste_chainee, 4)
    print("liste_chainee : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_1"
    )
    print("recherche : ", recherche(liste_chainee, 3).valeur)
    supprime(liste_chainee, 5)
    print("apres suppression de 5 : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_2"
    )
    supprime(liste_chainee, 4)
    print("apres suppression de 4 : ", liste_chainee)
    traceur.display_instance(
        liste_chainee, visualize=False, image_name="liste_chainee_3"
    )


teste_listes()
