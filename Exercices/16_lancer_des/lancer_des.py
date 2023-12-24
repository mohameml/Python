#!/usr/bin/env python3

"""TD sur les lancers de dés."""

# START CORRECTION

import random


def lance(nb_des):
    """Renvoie la somme des valeurs du nombre de dés lancés aléatoirement."""
    if nb_des == 0:
        return 0
    return random.randint(1, 6) + lance(nb_des - 1)


def enumere_lancers_rec(des, des_restants, somme=None):
    """Enumere toutes les lancers possibles de des_restants dés.

    Nombre d'appels récursifs = 6^des_restants.
    """

    # Cas de base
    if des_restants == 0:
        if sum(des) == somme:
            print("***", des, "***")
        else:
            print(des)
        return

    # Sinon on tire le dés "courant" 6 fois
    # et on fait les appels récursifs
    for de_courant in range(1, 7):
        des[-des_restants] = de_courant
        enumere_lancers_rec(des, des_restants - 1, somme)


def enumere_lancers(nb_des):
    """Enumere toutes les lancers possibles de nb_des dés: complexité = 6^nb_des"""
    enumere_lancers_rec([0] * nb_des, nb_des)


def enumere_lancers_somme(nb_des, somme):
    """Enumere toutes les lancers possibles de nb_des dés.

    Les lancés dont la somme vaut somme sont affichés entre "***".
    """
    enumere_lancers_rec([0] * nb_des, nb_des, somme=somme)


def compte_occurence_somme(nb_des, somme):
    """Renvoie le nombre de lancers de la taille donnée atteignant la somme demandée."""

    # Cas de base
    if nb_des == 0:
        if somme == 0:
            return 1
        return 0

    # Si en ne faisant que des 1 ensuite on dépasse
    # alors on peut s'arréter
    if nb_des * 1 > somme:
        return 0

    # Si en ne faisant que des 6 ensuite on y arrive pas
    # alors on s'arrête aussi
    if nb_des * 6 < somme:
        return 0

    # Sinon on tire le dés "courant" 6 fois
    # et on fait les appels récursifs
    compte = 0
    for de_courant in range(1, 7):

        # Sinon on fait l'appel récursif
        compte += compte_occurence_somme(nb_des - 1, somme - de_courant)

    return compte


def compte_lancers_valides_rec(fonction_validation, des, des_restants):
    """Renvoie le nombre de lancers valides de nb_des dés."""

    # Cas de base
    if des_restants == 0:
        return int(fonction_validation(des))

    # Sinon on tire le dés "courant" 6 fois
    # et on fait les appels récursifs si besoin
    compte = 0
    for de_courant in range(1, 7):
        des[des_restants - 1] = de_courant
        compte += compte_lancers_valides_rec(fonction_validation, des, des_restants - 1)

    return compte


def compte_lancers_valides(nb_des, fonction_validation):
    """Renvoie le nombre de lancers valides de nb_des dés."""
    return compte_lancers_valides_rec(fonction_validation, [0] * nb_des, nb_des)


def enumere_lancers_distincts_rec(des, des_restants, vmin):
    """Enumere toutes les lancers distincts possibles de des_restants dés."""

    # Cas de base
    if des_restants == 0:
        print(des)
        return

    # Sinon on tire le dés "courant" 6 fois
    # et on fait les appels récursifs
    for de_courant in range(vmin, 7):
        des[-des_restants] = de_courant
        enumere_lancers_distincts_rec(des, des_restants - 1, de_courant)


def enumere_lancers_distincts(nb_des):
    """Enumere toutes les lancers distincts possibles de nb_des dés.

    Complexité = (nb_des + 5, 5)
               = (nb_des + 5)! / (5! * (nb_des + 5 - 5)!)
               = (nb_des + 5)! / (5! * nb_des!)

    Pour 3 dés ça donne : (8*7*6) / 5! = 56.

    Sinon pour info, itertools.combinations_with_replacement(range(1, 7), 3)
    fait exactement ce qu'on veut ici :)
    """
    enumere_lancers_distincts_rec([0] * nb_des, nb_des, 1)


def teste():
    """Teste toutes les fonctions ci-dessus."""
    random.seed(42)
    print("somme de 6 dés =", lance(6))
    print("somme de 6 dés =", lance(6))
    print("somme de 6 dés =", lance(6))

    for nb_des in range(1, 3):
        enumere_lancers(nb_des)

    for nb_des in range(1, 3):
        enumere_lancers_somme(nb_des, 7)

    print("avec 2 dés,", compte_occurence_somme(2, 7), "lancers valent 7")
    print("avec 6 dés,", compte_occurence_somme(6, 17), "lancers valent 17")

    print(
        "avec 6 dés,",
        compte_lancers_valides(6, lambda des: sum(des) == 17),
        "lancers valent 17",
    )

    for nb_des in range(1, 4):
        enumere_lancers_distincts(nb_des)


if __name__ == "__main__":
    teste()

# END CORRECTION
