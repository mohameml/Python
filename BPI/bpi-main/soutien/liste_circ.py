#!/usr/bin/env python3
"""
listes circulaires avec sentinelle.
"""

from random import randint

from cellule import Cellule

def creer():
    """
      La sentinelle est chainee a elle-meme quand la liste est vide
    """
    fictif = Cellule('?', None)
    fictif.suiv = fictif
    return fictif

def main():
    """
      Programme principal
    """
    liste = creer()
    for _ in range(12):
        val = randint(0, 9)
        print("Insertion de", val, ":")
        inserer(liste, val)
        print("  ", end="")
        afficher(liste)
    for _ in range(5):
        val = randint(0, 9)
        print("Suppression de", val, ":")
        if supprimer(liste, val):
            print("  ", end="")
            afficher(liste)
        else:
            print("  valeur absente de la liste")
    print("Tri de la liste :")
    liste = trier_ins(liste)
    print("  ", end="")
    afficher(liste)
    print("Decoupage de la liste :")
    listes = decouper(liste)
    print("  ", end="")
    afficher(liste)
    for liste in listes:
        print("  ", end="")
        afficher(liste)

main()
