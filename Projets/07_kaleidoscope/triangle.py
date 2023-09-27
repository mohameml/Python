#!/usr/bin/env python3

"""
Module triangle 
"""

import random
from svg import Point


from math import cos, sin


def genere_point(zone_x, zone_y):
    "genere une point dans l'espace : [zone_x , zone_y]"

    abscisse = random.randint(zone_x[0], zone_x[1])
    ordonneé = random.randint(zone_y[0], zone_y[1])

    return Point(abscisse, ordonneé)


def triangle_aleatoire(zone_x: tuple, zone_y: tuple):
    "return les coorrdoneés d'un triangle aléatoire "

    return [genere_point(zone_x, zone_y) for _ in range(3)]


def coordonneé_point_rotation(point, centre, angle):
    """
    return les coordonnées de la point = r(centre , angle)
    x' = (x - xc) x cos(alpha) - (y - yc) x sin(alpha) + xc

    y' = (x - xc) x sin(alpha) + (y - yc) x cos(alpha) + yc
    """
    abscisse = (point.x - centre.x)*cos(angle) - \
        (point.y - centre.y)*sin(angle) + centre.x

    ordoneé = (point.x - centre.x)*sin(angle) + \
        (point.y - centre.y)*cos(angle) + centre.y

    return Point(abscisse, ordoneé)


def tourne_triangle_autour(triangle, centre, angle):
    "return les cordonnées d'un Trinagle obtenu par rotation d'un autre triangle"

    return [coordonneé_point_rotation(point, centre, angle) for point in triangle]
