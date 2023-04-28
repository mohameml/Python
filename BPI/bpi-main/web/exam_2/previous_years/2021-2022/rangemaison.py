#!/usr/bin/env python3

"""Module implémentant notre range maison."""


def test_range():
    """Teste les deux fonctions ci-dessous."""
    # TODO
    ...


def create_range(start, stop, step):
    """Renvoie un nouveau range dont le type dépend de la structure de
    données choisie.

    Ce range démarre à start (inclus), termine à stop (exclus) et avance
    de step unités à chaque élément. Chacun des trois paramètre peut
    ếtre un nombre négatif.

    Par exemple create_range(0, 5, 1) renvoie un range qui permettra
    d'itérer sur les nombres `0 1 2 3 4` en utilisant la fonction
    get_elements.

    pré-conditions :
    - step != 0

    Autrement dit, dans cet exercice on ne manipulera que des ranges avec
    des steps différents de 0.
    """
    # TODO
    ...


def get_ith(rangemaison, i):
    """Renvoie le ième élément de rangemaison.

    Le premier élément est l'élément 0.

    pré-conditions :
    - rangemaison n'est pas None.
    - il y a au moins i+1 éléments dans rangemaison.

    Autrement dit, pas besoin de vérifier quoi que ce soit dans la fonction.
    """
    # TODO
    ...


def get_elements(rangemaison):
    """Renvoie un itérateur sur tous les éléments de rangemaison.

    pré-conditions :
    - rangemaison n'est pas None.
    """
    # TODO
    ...


# Ce module doit également être un programme exécutable
# qui appelle la fonction `test_range`.
# TODO
...
