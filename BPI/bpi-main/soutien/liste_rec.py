#!/usr/bin/env python3
"""
  Manipulations récursives de listes chainees
"""

from random import randint

from cellule import Cellule

def creer(tab):
    """
      Construit la liste en inserant les valeurs du tableau.
      Les elements doivent apparaitre dans le meme ordre.
      Renvoie la liste construite.
      Cas de base :
        - si le tableau est de taille 0 alors la liste renvoyee est vide
      Hypothese de recurrence :
        - si L' est la liste créée à partir de tous les elements du tableau
          sauf le premier alors L est la liste créée en insérant
          le premier element du tableau en tete de L'
    """
    if not tab: # equivalent a len(tab) == 0
        return None
    liste_p = creer(tab[1:])
    return Cellule(tab[0], liste_p)

def main():
    """
      Fonction principale
    """
    for taille in range(8):
        print(f"-- Taille = {taille} --")
        tab = [randint(0, 9) for _ in range(taille)]
        print("Tableau initial :", tab)
        liste = creer(tab)
        print("Liste initiale  : ", end="")
        afficher(liste)
        liste1, liste2 = separer(liste)
        print("Listes separees :")
        print("  ", end="")
        afficher(liste1)
        print("  ", end="")
        afficher(liste2)
        liste = trier(creer(tab))
        print("Liste triee     : ", end="")
        afficher(liste)
        print()
    # tests de la fonction fusionner avec des listes deja triees
    tabs = (([], []), ([], [1]), ([2], []), ([1], [2]), ([1, 3], [2]),
            ([3], [2, 4]), ([1, 5, 7], [2, 4, 6, 8]))
    for tab1, tab2 in tabs:
        print(f"Fusion de {tab1} et {tab2} :")
        liste = fusionner(creer(tab1), creer(tab2))
        print("  liste fusionnee : ", end="")
        afficher(liste)
        print()

main()
