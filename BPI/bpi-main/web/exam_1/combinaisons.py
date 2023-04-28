#!/usr/bin/env python3

"""Un programme qui ne sert à pas grand chose."""

import sys


def teste():
    """Teste les fonctions :
        - `recupere_combinaisons_2`
        - `renverse`
        - `recupere_combinaisons`
        - `recupere_parametres`

    Ces trois fonctions testées seront écrites plus tard, mais c'est
    souvent une bonne chose de commencer par les tests, donc allons-y.
    En plus, écrire ce test vous obligera à réfléchir à l'algorithme
    général à appliquer pour générer les combinaisons, sur des séquences
    simples.

    Les spécifications du travail à réaliser sont données en commentaire
    dans le corps de la fonction ci-dessous.
    Vous devez rajouter une ou plusieurs lignes de code à chaque fois
    qu'il y a un TODO suivi de trois points.
    Pensez à bien enlever ces TODO et ces trois points dès que vous les
    avez implémentés.
    Merci de respecter les spécifications À LA LETTRE pour que la
    correction automatique soit possible.

    Pour rappel, en Python une séquence `seq` est un objet sur lequel on
    peut :
      - utiliser la fonction `len(seq)` pour connaître sa taille. Cette
        opération s'effectue en temps constant ;
      - utiliser une boucle `for` pour parcourir ses éléments ;
      - accéder au ième élément avec `seq[i]` (le premier élément est à
        l'indice `0`).
    """

    print('Résultats calculés dans ma tête pour la séquence "ABCD" et k=2')
    # affiche sur la sortie standard ces combinaisons calculées dans notre
    # tête (c'est à dire pour la séquence "ABCD" et k=2), avec une seule
    # combinaison par ligne, sous forme de chaîne de caractères,
    # par exemple AC
    # TODO
    ...

    print('Résultats calculés par recupere_combinaisons_2("ABCD")')
    # effectue l'appel à recupere_combinaisons_2('ABCD'), puis affiche
    # sur la sortie standard les combinaisons renvoyées par cet appel,
    # avec une seule combinaison par ligne. Une combinaison étant un
    # tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print``, c'est à dire de ne faire aucun
    # formatage. La combinaison AC sera donc affichée de la façon
    # suivante : ('A', 'C')
    # TODO
    ...

    # affiche sur la sortie standard une ligne vide
    print()

    print("Résultat de renverse sur [1, 2, 3]")
    # effectue l'appel à renverse([1, 2, 3]), puis
    # puis affiche sur ce résultat
    print(renverse([1, 2, 3]))

    # affiche sur la sortie standard une ligne vide
    print()

    print("Résultats calculés dans ma tête pour la séquence [0, 1, 2, 3, 4] et k=3")
    # affiche sur la sortie standard ces combinaisons calculées dans notre
    # tête (c'est à dire pour la séquence [0, 1, 2, 3, 4] et k=3), avec
    # une seule combinaison par ligne, sous forme de chaîne de caractères,
    # par exemple 014
    # TODO
    ...

    print("Résultats calculés par recupere_combinaisons([0, 1, 2, 3, 4], 3)")
    # effectue l'appel à recupere_combinaisons([0, 1, 2, 3, 4], 3), puis
    # affiche sur la sortie standard les combinaisons renvoyées par cet
    # appel, avec une seule combinaison par ligne. Une combinaison étant
    # un tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print`, c'est à dire de ne faire aucun formatage.
    # La combinaison 014 sera donc affichée de la façon suivante : (0, 1, 4)
    # TODO
    ...

    # affiche sur la sortie standard une ligne vide
    print()

    # effectue l'appel recupere_parametres(x) avec x étant premier
    # argument de la ligne de commande.
    # Par exemple pour l'exécution de `python combinaisons.py input.txt`
    # x est `input.txt`.
    # affiche ensuite la séquence et l'entier k renvoyés par cet
    # appel sur la sortie standard avec la séquence sur une ligne
    # et k sur une autre ligne.
    print(
        "Résultats de recupere_parametres sur le fichier donné "
        "en paramètre sur la ligne de commande"
    )
    # TODO
    ...

    # affiche sur la sortie standard une ligne vide
    print()

    print(
        "Résultats calculés par recupere_combinaisons sur "
        "les paramètres dans le fichier"
    )
    # effectue l'appel à recupere_combinaisons en utilisant les paramètres
    # renvoyés par l'appel à recupere_parametres(x), puis affiche sur la
    # sortie standard les combinaisons renvoyées par cet appel, avec une
    # seule combinaison par ligne. Une combinaison étant un tuple, on vous
    # demande pour l'affichage de passer directement ce tuple à la fonction
    # `print`, c'est à dire de ne faire aucun formatage. La combinaison AC
    # sera donc affichée de la façon suivante : ('A', 'C')
    # TODO
    ...


def recupere_parametres(filename):
    """Renvoie un tuple à deux entrées contenant la séquence et
    le paramètre k, DANS CET ORDRE, lus à partir du fichier passé
    en paramètre. La séquence renvoyée sera une `list` de chaînes
    de caractères de taille 1.

    Spécifications PRÉCISES (pensons aux tests automatiques)
    sur le format du fichier :
       - la première ligne contient le nombre k
       - les lignes suivantes contiennent les éléments de la séquence

    Vous trouverez un fichier `input.txt` dans votre dossier `exam` à
    titre d'exemple.
    """
    # TODO
    ...


def recupere_combinaisons_2(sequence):
    """ "Renvoie toutes les combinaisons de taille 2 de la séquence donnée.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par une
         `list` de `tuple`.
    """
    # TODO
    ...


def renverse(sequence):
    """
    Renvoie une nouvelle `list` contenant tous les éléments
    de la séquence donnée en paramètre mais dans l'ordre inverse.
    """
    # TODO
    ...


def recupere_combinaisons(sequence, k):
    """
    Renvoie toutes les combinaisons de taille k de la sequence donnée.

    Attention, cette fonction est difficile à implémenter.
    Il est vivement conseillé de réfléchir à un algorithme sur le
    papier avant de se lancer dans le code.
    Vous pouvez utiliser la fonction `renverse` si besoin,
    mais ce n'est pas du tout une obligation.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par
         une `list` de `tuple`.
    """
    # Cette implémentation fonctionne sur les indices des éléments
    # de la prochaine combinaison à ajouter tel que :
    #    - les indices des éléments de n'importe quelle combinaison
    #      soient "strictement croissants entre eux"
    #      (par exemple on n'aura jamais 0 2 1)
    #    - la suite des indices des combinaisons successives soit
    #      "strictement croissante".

    # Par exemple quand on choisit 3 parmi 5, la suite des indices
    # sera la suivante :
    #     - 0 1 2
    #     - 0 1 3
    #     - 0 1 4
    #     - 0 2 3
    #     - 0 2 4
    #     - 0 3 4
    #     - 1 2 3
    #     - 1 2 4
    #     - 1 3 4
    #     - 2 3 4

    # TODO
    ...


def affiche_nombre_combinaisons():
    """Affiche le nombre de k-combinaisons d'une séquence de taille n.

    On vous demande ici d'afficher sur la sortie standard la formule que
    vous écririez au tableau lors d'une séance de TD, pour répondre à cette question.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - l'affichage de la formule se fera en fonction de la taille de la séquence n,
         et du paramètre k
       - les seuls caractères autorisés dans la chaîne affichée sont :
           + `*`, `/` et `-`
           + les lettres `n` et `k`
           + des parenthèses
           + le caractère `!` (factorielle)
    """
    # TODO
    ...


# La fonction teste() est appelée uniquement dans
# le cas où le programme est invoqué comme programme
# principal avec `python combinaisons.py input.txt`
# ou avec `./combinaisons.py input.txt`
if __name__ == "__main__":
    teste()
