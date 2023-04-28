#!/usr/bin/env python3
""""
L'objectif de se tp de dessiner un arbre

"""

import svg
import random
import sys
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _str__(self):
        chaine = f'Point(x={self.x},y={self.y}'
        return chaine


def main():
    "Point d'entree du programme "
    print(svg.genere_balise_debut_image(400, 400))
    print(svg.genere_segment(Point(350, 200), Point(180, 200)))
    print(svg.genere_balise_fin_image())


if __name__ == "__main__":
    main()
