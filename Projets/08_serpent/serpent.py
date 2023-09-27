#!/usr/bin/env python3

"""
mini projet 08 : 

"""

import svg

GAUCHE = True
DROITE = False

p1 = svg.Point(0, 0)
p2 = svg.Point(40, 0)
p3 = svg.Point(0, 40)
p4 = svg.Point(40, 40)

numero = 1

while GAUCHE:
    if numero == 20:
        GAUCHE = False
        DROITE = True

    dessine_carre([p1, p2, p3, p4], numero)
    numero += 1


def dessine_gauche(points:list,numero):
    while GAUCHE :
    
    


def dessine_droite():
    pass


def dessine_carre(points: list, numero):
    "points = [p1,p2,p3,p4]"
    print(svg.genere_polygone(points))
    if numero == 41:
        print(svg.genere_texte(points[0].x, points[0].y, numero, 10))
    print(svg.genere_texte(points[0].x, points[0].y, numero, 5))


def main():
    pass


if __name__ == "__main__":
    main()
