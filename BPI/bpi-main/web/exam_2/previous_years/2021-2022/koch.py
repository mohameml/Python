#! /usr/bin/env python3

"""Dessin d'un joli flocon de Koch. C'est l'hiver."""

import math
import sys
import svg


COS_60 = math.cos(math.pi / 3)
SIN_60 = math.sin(math.pi / 3)
LINE_COLOR = "purple"


class Sommet:
    """Classe représentant un point dans le plan.

    Attributs :
        - x représente l'abscisse du Sommet ;
        - y représente l'ordonnée du Sommet ;
        - suiv permet de chainer des Sommet entre eux.
    """

    # On dit à pylint qu'ON SAIT que x et y sont des
    # noms d'attributs très raisonnables ici.
    # pylint: disable=invalid-name
    def __init__(self, coord_x, coord_y):
        # TODO
        ...

    def __str__(self):
        """Pour débogguer.

        C'est important de pouvoir afficher un sommet
        avec print.
        """
        # TODO
        ...


def cree_polygone_initial():
    """Retourne le polygone représentant le triangle équilatéral initial.

    Un polygone est représenté par une liste chainée circulaire de Sommet.

    Le polygone créé ici contient seulement les sommets du triangle initial qu'on
    a déjà instanciés pour vous (s_a, s_b, s_c). Trop sympas les profs de BPI !

    Retourne le polygone créé, c'est-à-dire comme indiqué en gras dans le sujet,
    le Sommet en tête de la liste chainée créée.
    """
    s_a = Sommet(200, 25)
    s_b = Sommet(50, 284.8)
    s_c = Sommet(350, 284.8)
    # TODO
    ...


def insere_apres(prec, sommet):
    """Insère le sommet dans polygone après le sommet prec.

    paramètres :
    - prec : le Sommet après lequel on va insérer sommet ;
    - sommet : le Sommet à insérer après prec.

    pré-conditions :
    - prec et sommet ne sont pas None.
    """
    # TODO
    ...


def recupere_couples_sommets(polygone, distance=1):
    """Retourne un itérateur sur tous les couples de sommets avec un pas de distance.

    paramètres :
    - polygone : le polygone à parcourir (= le Sommet en tête du chainage) ;
    - distance : le nombre de liens qui séparent les Sommet du couple (dans
                 le chainage s_a -> s_b -> s_c -> s_d, les sommets s_a et s_d
                 sont à une distance de 3).

    pré-conditions :
    - distance est un diviseur du nombre de sommets dans polygone.
    """
    # TODO
    ...


def calcule_coordonnees(s_a, s_e):
    """Calcule les coordonnées des sommets à ajouter entre s_a et s_e.

    paramètres :
    - s_a et s_e sont des Sommet et représentent les sommets du segment
    sur lequel on applique une transformation de Koch.

    Retourne les coordonnées des 3 nouveaux sommets à insérer entre s_a et s_e
    sous la forme d'un triplet de trois couples :
    ((x_b, y_b), (x_c, y_c), (x_d, y_d))
    """
    x_b = s_a.x + (s_e.x - s_a.x) / 3
    y_b = s_a.y + (s_e.y - s_a.y) / 3
    x_d = s_a.x + 2 * (s_e.x - s_a.x) / 3
    y_d = s_a.y + 2 * (s_e.y - s_a.y) / 3
    x_c = (x_b + x_d) * COS_60 - (y_d - y_b) * SIN_60
    y_c = (y_b + y_d) * COS_60 + (x_d - x_b) * SIN_60

    return (x_b, y_b), (x_c, y_c), (x_d, y_d)


def applique_transformation(s_a, s_e):
    """Applique une transformation de Koch sur l'arête [s_a; s_e].

    Cette fonction applique une transformation de Koch sur l'arête délimitée
    par les sommets s_a et s_e. Elle doit donc :
        - créer les sommets intermédiaires s_b, s_c, s_d : pour ce faire,
          on utilisera la fonction calcule_coordonnees(), qui retourne les
          coordonnées des points à créer (se référer à la docstring de la
          fonction pour plus d'informations) ;
        - les chaîner ensemble et avec les sommets s_a et s_e, de manière à obtenir
          le chaînage s_a -> s_b -> s_c -> s_d -> s_e.

    paramètres :
    - s_a, s_e : les Sommet délimitant l'arête sur laquelle appliquer la
    transformation de Koch.
    """

    # TODO
    ...


def applique_transformations_rec(s_a, s_e, profondeur):
    """Applique profondeur transformations de Koch récursivement, en partant du segment [s_a; s_e].

    paramètres :
    - s_a, s_e : les Sommets entre lesquels appliquer la transformation de Koch ;
    - profondeur : la profondeur maximale de récursion.
    """
    # TODO
    ...


def cree_flocon_koch_v1(polygone, nb_etapes):
    """Version récursive de l'algorithme de création de flocon de Koch.

    Cette version appelle la procédure récursive applique_transformation_rec
    sur chaque arête du polygone passé en paramètre.

    Le flocon n'est donc pas construit étapes par étapes tel que décrit dans
    le sujet, mais arête par arête.

    paramètres :
    - polygone : le polygone sur lequel appliquer les nb_etapes étapes
                 de Koch (= le Sommet en tête du chainage) ;
    - nb_etapes : le nombre d'étapes de Koch à appliquer au polygone
                  passé en paramètre.
    """
    # TODO
    ...


def cree_flocon_koch_v2(polygone, nb_etapes):
    """Version itérative de l'algorithme de création de flocon de Koch.

    Cette version applique une transformation de Koch à la première arête du
    polygone passé en paramètre, puis passe à l'arête suivante, jusqu'à les
    traiter toutes.

    Cette opération est ensuite répétée jusqu'à l'obtention du polygone après
    nb_etapes étapes de Koch.

    Le flocon est donc dans cette version itérative construit étape par étape
    tel que décrit dans le sujet.

    paramètres :
    - polygone : le polygone sur lequel appliquer les nb_etapes étapes de
                 transformation de Koch (= le Sommet en tête du chainage) ;
    - nb_etapes : le nombre d'étapes de Koch à appliquer au polygone passé
                  en paramètre.
    """
    # TODO
    ...


def ecrit_fichier_svg(nom_fichier, polygone, nb_etapes, dump_all_steps=False):
    """Génère une ou plusieurs images SVG représentant le polygone donné.

    Paramètres :
    - nom_fichier : le chemin complet vers le fichier de sortie SVG ;
    - polygone : le polygone à parcourir (= le Sommet en tête du chainage) ;
    - nb_etapes : le nombre d'étapes appliquées au polygone passé en paramètre ;
    - dump_all_steps : si True, écrit un fichier par étape de l'algorithme de Koch.
    """
    # TODO
    ...


def affiche_usage():
    """Fonction d'usage du programme koch.py.

    Il est d'usage que la fonction d'usage d'un programme
    rappelle poliment à l'utilisateur comment lancer le
    programme.
    """
    print(*sys.argv, " ? Sérieux ? N'importe quoi !")
    print("C'est comme ça qu'on utilise ce programme, enfin...")
    print(main.__doc__)


def main():
    """Usage :
    ./koch.py profondeur fichier.svg

    avec :
    - nb_etapes le nombre d'étapes à appliquer sur le triangle initial
    - fichier.svg le nom du fichier de sortie SVG. Ce nom de fichier sera
    utilisé pour générer un fichier par étape
    (0-fichier.svg, 1-fichier.svg, ...).
    """
    args = sys.argv
    if len(args) < 2:
        affiche_usage()
        sys.exit(1)

    nb_etapes = int(sys.argv[1])
    outfile_name = sys.argv[2]

    # version récursive
    polygone = cree_polygone_initial()
    cree_flocon_koch_v1(polygone, nb_etapes)
    ecrit_fichier_svg(f"rec_{outfile_name}", polygone, nb_etapes)

    # version itérative
    polygone = cree_polygone_initial()
    cree_flocon_koch_v2(polygone, nb_etapes)
    ecrit_fichier_svg(f"iter_{outfile_name}", polygone, nb_etapes)

    # en créant un fichier par étape
    ecrit_fichier_svg(outfile_name, polygone, nb_etapes, dump_all_steps=True)


if __name__ == "__main__":
    main()
