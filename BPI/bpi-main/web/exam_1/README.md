## Introduction

Dans ce premier examen BPI, nous allons développer un programme qui ne sert pas à grand chose.
En effet, ce qu'on cherche à faire est déjà fourni en standard dans Python.
Mais comme on est archi-motivé, on va le recoder par nous mêmes, comme ça, pour le fun.

En plus du fun, on a quand même trois autres bonnes raisons d'écrire un programme qui ne sert pas à grand chose aujourd'hui :

- découvrir le mode examen des machines de l'Ensimag ;

- évaluer nos propres compétences concernant les bases de la programmation impérative, pour savoir s'il faut mettre un coup de collier (travailler plus) pour le reste du semestre, et ça c'est déjà un bel objectif !

- comprendre l'algorithme sous-jacent implémenté dans Python. Et comprendre, c'est bien non ?

## Objectif ultime

Implémenter une fonction `recupere_combinaisons(sequence, k)` qui renvoie toutes les combinaisons de longueur `k` d'une séquence Python donnée.
Lorsque l'on construit toutes les k-combinaisons d'une séquence, **l'ordre des `k` éléments choisis ne compte pas** : par exemple la combinaison `1,2,3` est la même que la combinaison `2,3,1`.
Une combinaison **ne peut contenir qu'une seule fois chaque élément** de la séquence donnée.

Pour rappel, en Python une séquence `seq` est un objet sur lequel on peut :

- utiliser la fonction `len(seq)` pour connaître sa taille. Cette opération s'effectue en temps constant ;
- utiliser une boucle `for` pour parcourir tous ses éléments ;
- accéder au ième élément avec `seq[i]` (le premier élément est à l'indice `0`).

## Consignes

- faites bien attention aux éléments en gras dans le paragraphe "Objectif ultime" ci-dessus ;
- le travail à effectuer se trouve dans les "docstring" et les `# TODO ...` du squelette de programme Python disponible dans votre dossier `exam` et affiché ci-dessous ;
- il est recommandé d'implémenter les fonctions dans l'ordre dans lequel elles apparaissent dans le fichier ;
- lire TOUT le fichier avant de coder ;
- il faut respecter strictement les consignes, PENSER aux tests automatiques (les pauvres ...) ;
- si vous utilisez `print` pour déboguer votre programme, pensez à les enlever une fois que vous avez fini, PENSER aux tests automatiques (les pauvres ...) ;
- s'interroger sur la COMPLEXITÉ en temps de chaque fonction ;
- il est INTERDIT de rajouter des `import` ;
- la méthode `strip` de la classe `str` pourra vous être utile ;
- chose promise chose due, `pylint` sera lancé par les tests automatiques.

## Squelette de code à compléter

```python
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
```

## Tests automatiques pour le TP14

Pour lancer les tests automatiques, il faut :

- récupérer votre fichier `combinaisons.py` réalisé pendant l'examen. Pour cela utiliser la commande `grep` pour retrouver votre machine puis la commande `cp` comme ci dessous en remplaçant bien sûr `beaufilt` par votre propre login :

```console
selvama@ensipc208:~/bpi$ grep -Irn "beaufilt" /matieres/3MMBPI/exam_mi_parcours/
/matieres/3MMBPI/exam_mi_parcours/g4-2022-10-21/ensipc325/exam/whoami.txt:5:Login: beaufilt
selvama@ensipc208:~/bpi$ cp /matieres/3MMBPI/exam_mi_parcours/g4-2022-10-21/ensipc325/exam/combinaisons.py .
```

- télécharger le programme de correction automatique [disponible ici](correct.py) et le placer dans le même répertoire que le programme `combinaisons.py` ;
- télécharger le fichier `input.txt` [disponible ici](input.txt) à côté de `combinaisons.py` et `./correct.py` ;
- télécharger le fichier `combinaisons_corrigee.py` [disponible ici](combinaisons_corrigee.py) toujours au même endroit ;
- enfin, lancer la correction automatique avec `./correct.py`.

**ATTENTION** l'objectif de la séance est de corriger **SOI-MÊME** son travail, il ne faut donc **SURTOUT PAS REGARDER** la correction dans le fichier `combinaisons_corrigee.py`.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>


Le code de correction avec commentaires est également affiché ci-dessous.

```python
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
    print("AB", "AC", "AD", "BC", "BD", "CD", sep="\n")

    print('Résultats calculés par recupere_combinaisons_2("ABCD")')
    # effectue l'appel à recupere_combinaisons_2('ABCD'), puis affiche
    # sur la sortie standard les combinaisons renvoyées par cet appel,
    # avec une seule combinaison par ligne. Une combinaison étant un
    # tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print``, c'est à dire de ne faire aucun
    # formatage. La combinaison AC sera donc affichée de la façon
    # suivante : ('A', 'C')
    print(*recupere_combinaisons_2("ABCD"), sep="\n")

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
    print(
        "012", "013", "014", "023", "024", "034", "123", "124", "134", "234", sep="\n"
    )

    print("Résultats calculés par recupere_combinaisons([0, 1, 2, 3, 4], 3)")
    # effectue l'appel à recupere_combinaisons([0, 1, 2, 3, 4], 3), puis
    # affiche sur la sortie standard les combinaisons renvoyées par cet
    # appel, avec une seule combinaison par ligne. Une combinaison étant
    # un tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print`, c'est à dire de ne faire aucun formatage.
    # La combinaison 014 sera donc affichée de la façon suivante : (0, 1, 4)
    print(*recupere_combinaisons([0, 1, 2, 3, 4], 3), sep="\n")

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
    sequence, k = recupere_parametres(sys.argv[1])
    print(sequence)
    print(k)

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
    print(*recupere_combinaisons(sequence, k), sep="\n")


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
    input_file = open(filename, "r")
    k = -1
    elems = []
    for line in input_file:
        # Nous sommes sur la première ligne
        # On ferait du next en VRAI Python,
        # mais on l'a pas encore vu.
        if k == -1:
            k = int(line)
        # Nous sommes sur une ligne contenant un élément
        else:
            elems.append(line.strip())
    input_file.close()
    return elems, k


def recupere_combinaisons_2(sequence):
    """ "Renvoie toutes les combinaisons de taille 2 de la séquence donnée.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par une
         `list` de `tuple`.
    """
    combins = []
    for i, elem_i in enumerate(sequence):
        for j in range(i + 1, len(sequence)):
            combins.append((elem_i, sequence[j]))
    return combins


def renverse(sequence):
    """
    Renvoie une nouvelle `list` contenant tous les éléments
    de la séquence donnée en paramètre mais dans l'ordre inverse.
    """
    reversed_sequence = []
    for i in range(len(sequence) - 1, -1, -1):
        reversed_sequence.append(sequence[i])
    return reversed_sequence


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

    # list des combinaisons qui sera renvoyée
    combins = []

    # Rien à faire si k > n
    nb_elems = len(sequence)
    if k > nb_elems:
        return combins

    # Le tableau `indices` de taille k, contient les indices
    # dans sequence, des k éléments composant la prochaine
    # combinaison à ajouter.

    # On commence par renvoyer les k premiers éléments.
    indices = list(range(k))
    combins.append(tuple(sequence[i] for i in indices))

    # On va construire tous les autres tuples de k éléments
    while True:

        # On cherche l'indice i qu'il faut incrémenter
        # en partant du plus grand.
        found = False
        for i in renverse(range(k)):
            if indices[i] != i + nb_elems - k:
                found = True
                break

        # Si on a pas trouvé d'indice à incrémenter,
        # ça veut dire qu'on a fini
        if not found:
            break

        # Ici on va dire à pylint, pour avoir 10/10 et donc pas
        # de malus sur notre note BPI :
        # "ÉCOUTE MOI MON PETIT, JE TE DIS QUE i EST DÉFINI !"
        # pylint: disable=undefined-loop-variable

        # On incrémente l'indice i trouvé
        indices[i] += 1

        # On affecte tous les indices suivants i
        # à i+2, i+3, etc pour avoir notre suite croissante
        # sans répétition
        for j in range(i + 1, k):
            indices[j] = indices[j - 1] + 1

        # On renvoie le tuple associé à indices
        combins.append(tuple(sequence[i] for i in indices))

    return combins


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
    print("n! / (k! * (n-k)!")


# La fonction teste() est appelée uniquement dans
# le cas où le programme est invoqué comme programme
# principal avec `python combinaisons.py input.txt`
# ou avec `./combinaisons.py input.txt`
if __name__ == "__main__":
    teste()
```

Pour la dernière question concernant le dénombrement, pour ceux qui ne seraient pas à l'aise avec ça, l'arbre suivant peut aider et peut être assez facilement retrouvé par soi-même si on s'y prend dans l'ordre suivant :

- produit cartésien ;
- arrangement ;
- combinaison.

Pour les combinaisons avec répétitions, c'est un peu plus complexe.

![Arbre dénombrement](denombrement.svg)
</details>
