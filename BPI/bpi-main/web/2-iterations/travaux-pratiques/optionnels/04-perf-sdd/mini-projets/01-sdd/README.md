## Énoncé

Dans ce mini projet nous allons implémenter et exécuter les deux versions de conversion de données que nous avons vues [dans l'exercice 1 du TD "Structures de données".](../../../../../2-iterations/travaux-diriges/07-sdd-et-complexite).
Les objectifs sont les suivants :

- se familiariser avec le module Python standard `time` ;
- mesurer l'impact d'un choix algorithmique sur la performance.

Le travail demandé est le suivant :

- implémenter les deux versions de conversion de données, et les tester pour vérifier qu'elles soient correctes ;
- mettre en place ce qu'il faut pour pouvoir mesurer le temps d'exécution de chacune des deux versions ;
- analyser les performances.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici une correction possible.

Module `conversion.py` :
```python
"""Module pour convertir les données"""
def convertit_1(tab):
    """Convertit tab en données de façon naïve.

    Cette solution fonctionne, mais coûte
    O(100) + O(n*100) + O(nlogn) dans le pire cas.
    """

    # Initialisation du tableau dynamique données
    # O(100) car append est O(1) en amorti
    donnees = []
    for _ in range(101):
        donnees.append([0, []])

    # On rajoute les étudiants un par un, y a pas le choix
    # O(n * 100) si tout les étudiants ont 0
    # Ici on fait du "tuple unpacking" en récupérant
    # directement note et etudiant.
    for note, etudiant in tab:

        # On fait + 1 sur toutes les notes au dessus
        # O(100) dans le pire cas pour un étudiant ayant 0
        for note_au_dessus in range(note + 1, 101):
            donnees[note_au_dessus][0] += 1

        # On rajoute l'étudiant à sa place
        # O(1) en amorti
        donnees[note][1].append(etudiant)

    # Tri du nom des étudiants
    # O(nlogn) dans le pire cas, si tous les étudiants
    # sont dans la même case.
    for donnee in donnees:
        donnee[1].sort()

    return donnees


def convertit_2(tab):
    """Convertit tab en données de façon plus intelligente.

    Coûte O(100) + O(n) + O(nlogn) dans le pire cas.
    """

    # Initialisation du tableau dynamique données
    # O(100) car append est O(1) en amorti
    donnees = []
    for _ in range(101):
        donnees.append([0, []])

    # On rajoute les étudiants un par un, y a pas le choix
    # Mais cette fois-ci, on a ajoute seulement le nom de
    # l'étudiant dans cette boucle car elle est très grande,
    # donc faut faire le moins de boulot possible ici.
    # O(n)
    for note, etudiant in tab:

        # On rajoute l'étudiant à sa place
        # O(1) en amorti
        donnees[note][1].append(etudiant)

    # Tri du nom des étudiants + mise à jour nb étudiants inférieurs
    # O(nlogn) dans le pire cas, si tous les étudiants sont dans
    # la même case
    compte = 0
    for donnee in donnees:
        donnee[1].sort()  # O(nlogn)
        donnee[0] = compte  # O(1)
        compte += len(donnee[1])  # O(1)

    return donnees


```

Programme principal `bench_conversion.py` :
```python
#!/usr/bin/env python3

"""Un programme pour analyser les performances du TD SDD"""
import random
import time
import conversion


def init_notes(nb_entrees):
    """Initialise un tableau de notes avec nb_entrees entrees"""
    # Version avec compréhension de liste pour découvrir de nouvelles choses.
    return [
        (random.randint(0, 100), "etudiant" + str(number))
        for number in range(1, nb_entrees + 1)
    ]


def analyse_performance_conversions():
    """Analyse la performance des deux fonctions de conversion"""

    for nb_etudiants in (1, 100, 10_000, 1_000_000):
        notes = init_notes(nb_etudiants)
        print("nb étudiants =", nb_etudiants)

        start_time = time.time()
        conversion.convertit_1(notes)
        end_time = time.time()
        print("  convertit_1 : {:.6f} secondes".format(end_time - start_time))

        start_time = time.time()
        conversion.convertit_2(notes)
        end_time = time.time()
        print("  convertit_2 : {:.6f} secondes".format(end_time - start_time))


if __name__ == "__main__":
    random.seed(42)  # Pour être certain d'avoir toujours les mêmes entrées
    analyse_performance_conversions()
```
</details>

## Exercices

- [Tableaux](/2-iterations/travaux-pratiques/09-sous-suite/exercices/01-tableaux/index.html)
- [Boucles for](/2-iterations/travaux-pratiques/05-convertisseur/exercices/01-boucles-for/index.html)
- [Le hasard fait bien les choses](/2-iterations/travaux-pratiques/06-images-pgm/exercices/01-le-hasard-fait-bien-les-choses/index.html)
- [Le temps qui passe ...](/2-iterations/travaux-pratiques/optionnels/04-perf-sdd/exercices/01-mesure-du-temps/index.html)
