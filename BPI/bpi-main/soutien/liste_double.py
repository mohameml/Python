#!/usr/bin/env python3
"""
  Listes doublement chainees
"""

from random import randint

from cellule_double import Cellule

IX_T = 0
IX_Q = 1

def creer():
    """
      Cree une liste doublement chainee
    """
    liste = (Cellule('T', None, None), Cellule('Q', None, None))
    liste[IX_T].suiv = liste[IX_Q]
    liste[IX_Q].prec = liste[IX_T]
    return liste

def main():
    """
      Fonction principale
    """
    liste = creer()
    remplir(liste, [randint(0, 9) for _ in range(5)])
    print("Liste initiale : ", end="")
    afficher(liste)
    print("Liste inversee : ", end="")
    afficher(liste, True)
    cell = liste[IX_T].suiv
    while cell is not liste[IX_Q].prec:
        echanger(cell)
        print("Test echanger  : ", end="")
        afficher(liste)
    trier(liste)
    print("Liste triee    : ", end="")
    afficher(liste)
    print("Sens inverse   : ", end="")
    afficher(liste, True)

main()
