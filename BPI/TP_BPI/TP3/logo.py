"""Module tortue logo.

Ce module implémente les primitives graphiques basiques
d'une tortue logo.
"""

from math import cos, sin, pi

import svg


def avance(abscisse, ordonnee, direction, crayon_en_bas, distance):
    """Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un Point (défini dans notre module svg).
    """
    # Il faut que l'on fasse un peu de trigonométrie.
    # On avance suivant un vecteur donné par la direction.
    # Attention : comme la doc nous le rappelle cos et sin
    # prennent des angles en radians.
    vecteur = (cos(direction * pi / 180), sin(direction * pi / 180))
    nouvelle_abscisse = abscisse + vecteur[0] * distance
    nouvelle_ordonnee = ordonnee - vecteur[1] * distance
    nouveau_point = svg.Point(nouvelle_abscisse, nouvelle_ordonnee)
    # On dessine maintenant
    if crayon_en_bas:
        segment_svg = svg.genere_segment(svg.Point(abscisse, ordonnee), nouveau_point)
        print(segment_svg)

    return nouveau_point


def tourne_droite(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return direction - angle


def tourne_gauche(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return direction + angle
  
