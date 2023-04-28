#!/usr/bin/env python3

"""Listes simplements chainees + quelques operations"""

import traceur


class Cellule:
    """Une cellule d'une liste."""

    def __init__(self):
        self.valeur=''
        self.suivant=''



class ListeSimplementChainee:
    """Une liste simplement chainee."""

    def __init__(self):
        self.tete=''
        self.queue=''
        self.taille=''



def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tete"""

    c1=Cellule()
    c1.valeur=valeur
    c1.suivant=0
    liste_chainee.tete=c1


def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une cellule en queue."""
    c1=Cellule()
    c1.valeur=valeur
    c1.suivant=None
    liste_chainee.queue=c1

def recupere_cellules(liste_chainee):
    """Renvoie un vecteur contenant toutes les cellules de la liste_chainee"""
    l=[]
    while liste_chainee.tete.suivant
    
    l.append(liste_chainee.tete)
    l.append(liste_chainee.tete.suivant)
    l.append(liste_chainee.tete.suivant)

    
    

def recherche(liste_chainee, valeur):
    """Recherche uen valeur dans la liste_chainee donnée.

    Renvoie la premiere cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    # TODO
    ...


# TODO
...


def supprime(liste_chainee, valeur):
    """Enleve la premiere cellule contenant la valeur donnée."""
    # TODO
    ...


def test_listes():
    """On teste les operations de base, dans differentes configurations."""
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


if __name__ == "__main__":
    test_listes()
