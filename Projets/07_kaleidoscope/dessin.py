"""Quelques fonctions utiles pour générer du SVG.

    - affiche_triangle
    - couleur_aleatoire
"""
# START CORRECTION
from random import choice
import svg


def affiche_triangle(triangle, couleur):
    """Affiche le triangle donné, de la couleur donnée sur la sortie standard.

    Affichage avec une opacité de 0,5 (semi-transparent)
    """
    # Remarque : pour que les triangles soient transparents les uns
    # par rapport aux autres, chacun doit être dans son propre groupe
    # transparent.
    print(svg.genere_balise_debut_groupe_transp(0.5))
    print(svg.genere_balise_debut_groupe("none", couleur, 0))
    print(svg.genere_polygone((triangle.p1, triangle.p2, triangle.p3)))
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_groupe())


def couleur_aleatoire():
    """Renvoie une couleur svg aleatoire."""
    return choice(["red", "green", "blue", "orange", "yellow"])


# END CORRECTION
