"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaine de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l’origine est en haut à gauche et l’axe des Y est orienté vers le
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
        f'<rect width="100%" height="100%" fill="white"/>'
    )


def genere_balise_fin_image():
    """
    Retourne la chaine de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l’image, juste avant la fin du fichier.
    """
    return '</svg>'


def genere_segment(dep, arr, color):
    """
    Retourne la chaine de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr.
    """
    return f'<line x1="{dep.x}" x2="{arr.x}" y1="{dep.y}" y2="{arr.y}" stroke="{color}"/>'
