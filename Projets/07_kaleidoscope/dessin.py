#!/usr/bin/env python3

"""
Module dessin

"""

from random import choice
import svg


def affiche_triangle(triangle_tourne, couleur):

    print(svg.genere_balise_debut_groupe_transp(0.5))
    print(svg.genere_balise_debut_groupe("none", couleur, 0))
    print(svg.genere_polygone((triangle_tourne)))
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_groupe())


def couleur_aleatoire():
    " return un couleur aléatoire "
    couleur = ["yellow", "green" "red", "blue", "orange"]

    return choice(couleur)
