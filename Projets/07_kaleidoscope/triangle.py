"""
Module pour manipuler des triangles.

Le module fournit un namedtuple Triangle ainsi
qu'une fonction triangle_aleatoire.
"""
# START CORRECTION
from random import randint
from collections import namedtuple
from math import cos, sin
from svg import Point

Triangle = namedtuple("Triangle", "p1 p2 p3")


def tourne_point(point, centre, angle):
    """Tourne le point donné"""
    x_tourne = (
        (point.x - centre.x) * cos(angle) - (point.y - centre.y) * sin(angle) + centre.x
    )
    y_tourne = (
        (point.x - centre.x) * sin(angle) + (point.y - centre.y) * cos(angle) + centre.y
    )
    return Point(x_tourne, y_tourne)


def tourne_triangle_autour(triangle, centre, angle):
    """Tourne le triangle donné"""
    p1_tourne = tourne_point(triangle.p1, centre, angle)
    p2_tourne = tourne_point(triangle.p2, centre, angle)
    p3_tourne = tourne_point(triangle.p3, centre, angle)
    return Triangle(p1_tourne, p2_tourne, p3_tourne)


def point_aleatoire(intervalle_x, intervalle_y):
    """Renvoie un nouveau point aléatoire dans les intervalles donnés"""
    return Point(
        randint(intervalle_x[0], intervalle_x[1]),
        randint(intervalle_y[0], intervalle_y[1]),
    )


def triangle_aleatoire(intervalle_x, intervalle_y):
    """Renvoie un nouveau triangle aléatoire dans le rectangle specifie par les intervalles.

    Prend deux intervalles (chacun un couple de coordonnees) pour chaque dimension.
    """
    return Triangle(
        point_aleatoire(intervalle_x, intervalle_y),
        point_aleatoire(intervalle_x, intervalle_y),
        point_aleatoire(intervalle_x, intervalle_y),
    )


# END CORRECTION
