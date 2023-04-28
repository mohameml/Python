"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

from collections import namedtuple

# Definition de la structure Point composée de deux attributs x et y
Point = namedtuple("Point", "x y")

# À implémenter dans 'TP2. Module SVG'


def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaîne de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l'origine est en haut à gauche et l'axe des Y est orienté vers le
    bas.
    """
    # Les parenthèses sont utilisées ici uniquement pour permettre
    # de "couper" la f-string en deux ligne afin de ne pas avoir
    # une ligne trop longue. Il existe d'autres moyen de faire,
    # mais l'utilisation de parenthèses est celui recommandé par
    # le guide de style officiel python.
    #
    # On notera également que la chaîne de caractère renvoyée
    # contient des guillemets doubles. Pour que celles-ci ne
    # soient pas considérées comme la fin de la f-string, on
    # utilise des guillemets simples pour délimiter cette
    # dernière.
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
        f'width="{largeur}" height="{hauteur}">'
    )


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_image():
    """
    Retourne la chaîne de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l'image, juste avant la fin du fichier.
    """
    return "</svg>"


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrante
    définissant un groupe d'éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l'image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d'épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    return (
        f'<g stroke="{couleur_ligne}" fill="{couleur_remplissage}" '
        f'stroke-width="{epaisseur_ligne}">'
    )


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_groupe():
    """
    Retourne la chaîne de caractères correspondant à la balise fermante pour un
    groupe d'éléments.
    """
    return "</g>"


# À implémenter dans 'TP2. Module SVG'
def genere_cercle(centre, rayon):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
    """
    return f'<circle cx="{centre.x}" cy="{centre.y}" r="{rayon}" />'
# À implémenter dans 'TP3'


def genere_segment(dep, arr):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr.
    """
    return f'<line x1="{dep.x}" x2="{arr.x}" y1="{dep.y}" y2="{arr.y}" />'

# A implèmenter dans 'TP7'


def genere_polygone(points):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG
    représentant un polygone. `points` est un tableaux de points.
    """
    coordonnees_points = ""
    for point in points:
        coordonnees_points += f"{point.x}, {point.y} "
    return f'<polygon points="{coordonnees_points}" />'


def genere_balise_debut_groupe_transp(niveau_opacite):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrant un
    groupe d'éléments qui, dans son ensemble, sera partiellement transparent.
    Les éléments qui composent le groupe se masquent les uns les autres dans
    l'ordre d'apparition (ils ne sont pas transparents entre eux).
    `niveau_opacite` doit être un nombre entre 0 et 1. Ce groupe doit être
    refermé de la même manière que les groupes définissant un style.
    """
    return f'<g opacity="{niveau_opacite}">'
# À implémenter dans `TP8. Plateau`


def genere_zone_colorie(x_min, y_min, largeur, hauteur, couleur_remplissage):
    """
    Retourne la chaîne de caractères correspondant à un élément qui colorie une
    zone rectangulaire de la couleur indiquée
    """
    return (
        f'<rect x="{x_min}" y ="{y_min}" '
        f'width="{largeur}" height="{hauteur}" '
        f'stroke="none" fill="{couleur_remplissage}" />'
    )


# À implémenter dans `TP8. Plateau`
def genere_texte(x_min, y_bas, contenu, hauteur):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un texte. Place le texte à la position indiquée. x_min est l'abscisse du
    début du texte. y_bas est l'ordonnée de la ligne de base du texte (le bas
    d'une lettre telle que “n”). Attention, ce n'est pas l'ordonnée maximale
    puisque certaines lettres descendent sous cette ligne (g, j, p, q, y). Le
    paramètre hauteur définit la taille de police (c'est-à-dire la hauteur d'une
    ligne de texte)
    """
    balise_ouvrante = f'<text x="{x_min}" y="{y_bas}" font-size="{hauteur}">'
    balise_fermante = "</text>"
    return f"{balise_ouvrante}{contenu}{balise_fermante}"
