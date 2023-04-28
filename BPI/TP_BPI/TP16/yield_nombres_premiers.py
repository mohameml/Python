#!/usr/bin/env python3

"""Générateur des premiers nombres premiers"""

import sys
import math

def est_premier(number):
    for diviseur in range(2, int(math.sqrt(number)) + 1):
        if (number % diviseur) == 0:
            return False
    return True

def genere_premiers(maxi):
    """Générateur de nombres premiers.

    La complexité n'est pas le sujet ici, donc on a fait ça
    naïvement. Et donc, attention à ne pas tester avec un maxi trop
    grand pour ne pas attendre trop longtemps, et surtout user la
    planète avec des calculs inutiles.
    """
    # 2 est premier,on le sait, alors on le renvoie directement
    # pour le plaisir, et voir que yield peut s'utiliser en dehors
    # d'une boucle
    yield 2

    # Ensuite on itère jusqu'à maxi
    for number in range(3, maxi +1):
        if est_premier(number):
            # Plutôt que de construire une list (== un vecteur) avec
            # tous les nombres premiers, on rend la main dès qu'on
            # en trouve un
            yield number

def test():
    """Teste le générateur des premiers nombres premiers"""

    # L'utilisateur donne maxi
    if len(sys.argv) == 1:
        print("Usage :", sys.argv[0], "maxi")
        return
    maxi = int(sys.argv[1])

    # On affiche
    for premier in genere_premiers(maxi):
        print(premier)

if __name__ == "__main__":
    test()