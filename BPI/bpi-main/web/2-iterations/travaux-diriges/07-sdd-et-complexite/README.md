Ce TD à pour objectif d'illustrer l'importance du choix d'une structure de données sur la complexité des algorithmes associés.

On cherche ici à analyser un ensemble de données très volumineux.
On dispose d'un tableau de plus d'un million de tuples contenant chacun une note et le nom d'un étudiant.
Chaque note est un entier entre `0` et `100`.

L'objectif est de répondre aux questions suivantes :

- Comment sélectionner aléatoirement un étudiant ayant une certaine note ?
- Quelle est la note moyenne ?
- Combien d'étudiants ont au moins une certaine note ?
- Qui est le `nième` étudiant en partant du plus faible ?
- Quelle est la note médiane ?

## Exercice 1 : conversion des données

Afin de pouvoir répondre à toutes ces questions de manière efficace, on se propose de stocker les données dans un tableau dynamique `donnees`.
`donnees` est indicé entre `0` et `100` (donc de longueur 101) et chaque case `donnees[note]` contient elle-même un tableau de 2 cases :

- `donnees[note][0]` est le nombre total d'étudiants ayant une note strictement inférieure à `note` ;
- `donnees[note][1]` est un tableau dynamique des noms des étudiants dont la note est exactement `note`, trié par ordre alphabétique.

### Question 1
!!! question " "
    Représenter `donnees` de façon schématique sur papier puis écrire une fonction `conversion` qui convertit le grand tableau d'origine en `donnees`.


### Question 2
!!! question " "
    Quelle est la complexité temporelle de l'algorithme de conversion ?

###  Correction question 2
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
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
</details>



## Exercice 2 : analyse

Maintenant que notre structure de données est construite, nous pouvons réaliser les algorithmes d'analyse qui la parcourent.
Nous allons donc implémenter les opérations décrites dans l'introduction du TD en utilisant `donnees`. Pour chacune des analyses, nous indiquerons quelle est la **complexité temporelle** et quelle est la **complexité spatiale** dans le pire cas.

### Question 1
!!! question " "
    Écrire une fonction qui sélectionne aléatoirement un étudiant ayant une certaine note.

### Question 2
!!! question " "
    Écrire une fonction qui calcule la note moyenne.

### Question 3
!!! question " "
    Écrire une fonction qui calcule combien d'étudiants ont au moins une certaine note.

### Question 4
!!! question " "
    Écrire une fonction qui récupère le `nième` étudiant en partant du plus faible.

### Question 5
!!! question " "
    Écrire une fonction qui calcule la note médiane.
    Il faut noter que celle-ci n’est pas nécessairement unique si le nombre d’étudiants est pair.
    En effet la médiane est définie comme un nombre tel que la moitié de la population est en-dessous au sens large (inférieur ou égal) et la moitié de la population est au-dessus au sens large.
    Si le nombre d’étudiants est pair, il peut s'agir de n’importe quel nombre situé entre les notes des deux étudiants du milieu.
    Nous utiliserons la *plus petite* médiane.

### Correction globale
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
#!/usr/bin/env python3

"""Les fonctions d'analyse"""

import random
import conversion


def choisit_etudiant_aleatoirement(donnees, note):
    """Renvoie un étudiant aléatoire ayant la note donnée.

    Coût = O(1).
    """

    # Si on a pas d'étudiant, on renvoie None
    etudiants = donnees[note][1]
    if not etudiants:  # None et liste vide sont False
        return None

    # Sinon on en choisit un aléatoirement

    # On pourrait faire comme ça :
    # indice = random.randint(0, len(etudiants) - 1)
    # return etudiants[indice]

    # Mais on va choisir choice
    # car ici il est plus simple à utiliser
    return random.choice(etudiants)


def calcule_moyenne(donnees):
    """Calcule la moyenne.

    Coût = O(100).
    """

    total = 0
    nb_etudiants_total = donnees[100][0] + len(donnees[100][1])

    # La on fait du "nested tuple unpacking" en récupérant
    # directement note, _ (car on a pas besoin du compteur) et
    # noms.
    for note, (_, noms) in enumerate(donnees):
        total += note * len(noms)
    return total / nb_etudiants_total


def compte_nb_etudiants_dessus(donnees, note):
    """Renvoie le nombre d'étudiants ayant une note au dessus de note.

    Coût = O(1)
    """

    # Le nombre total d'étudiants
    nb_etudiants_total = donnees[100][0] + len(donnees[100][1])

    # On fait juste une petite soustraction
    nb_etudiants_dessus = nb_etudiants_total - donnees[note][0]
    return nb_etudiants_dessus


def recupere_nieme_etudiant_1(donnees, n):
    """Première version naive, O(100)"""

    # Si il n'y a pas n étudiants dans donnees
    nb_etudiants_total = donnees[100][0] + len(donnees[100][1])
    if nb_etudiants_total < n:
        return None

    nb_etudiants = 0
    note = 0
    while nb_etudiants < n:
        etudiants = donnees[note][1]
        nb_etudiants += len(etudiants)
        note += 1
    indice = len(etudiants) - (nb_etudiants - n) - 1
    return etudiants[indice]


def recupere_note_rang(donnees, rang):
    """
    Renvoie la note contenant le rang donné.

    Procède par dichotomie sur la portee de la recherche.
    O(log2(100)).
    """

    indice_min = 0
    indice_max = 100
    indice = (indice_max - indice_min) // 2
    compte, etudiants = donnees[indice]

    # Tant qu'on est pas au bon endroit
    while compte >= rang or compte + len(etudiants) < rang:
        # Doit-on aller à gauche ?
        if compte >= rang:
            indice_max = indice - 1
        # Sinon à droite
        else:
            indice_min = indice + 1
        indice = (indice_min + indice_max) // 2
        compte, etudiants = donnees[indice]

    return indice


def recupere_nieme_etudiant_2(donnees, n):
    """Version dichotomique, O(log2(100))"""

    indice = recupere_note_rang(donnees, n)
    compte = donnees[indice][0]
    etudiants = donnees[indice][1]
    indice_etudiant = n - compte - 1
    return etudiants[indice_etudiant]


def calcule_mediane(donnees):
    """
    Renvoie la mediane.

    Mediane est la plus petite* note n telle que :

    - la moitié des étudiants ont une note inférieure ou égale à n ;
    - la moitié ont une note supérieure ou égale à n.

    Si n = 2k + 1, c'est la note de l'étudiant de rang k + 1.
    Si n = 2k, c'est la note de l'étudiant de rang k.
    """

    # Le nombre total d'étudiants
    nb_etudiants_total = donnees[100][0] + len(donnees[100][1])

    rang = (nb_etudiants_total + 1) // 2
    return recupere_note_rang(donnees, rang)


def init_etudiants():
    """Initialise un tableau bidon d'étudiants"""

    etudiants = [
        (5, "arthur"),
        (5, "jean"),
        (5, "francois"),
        (5, "fred"),
        (5, "jerome"),
        (8, "sophie"),
        (12, "alban"),
        (15, "alexia"),
        (17, "céline"),
    ]
    return etudiants


def main():
    """Quelques tests mais sur un tableau tres petit"""

    # Init et conversion
    etudiants = init_etudiants()
    print(etudiants)
    donnees = conversion.convertit_2(etudiants)
    donnees_test = conversion.convertit_1(etudiants)
    assert donnees == donnees_test

    print("au moins 12:", compte_nb_etudiants_dessus(donnees, 12))
    print("aleatoire 5:", choisit_etudiant_aleatoirement(donnees, 5))
    print("moyenne:", calcule_moyenne(donnees))

    print("1er:", recupere_nieme_etudiant_1(donnees, 1))
    print("1er:", recupere_nieme_etudiant_2(donnees, 1))
    print("2nd:", recupere_nieme_etudiant_1(donnees, 2))
    print("2nd:", recupere_nieme_etudiant_2(donnees, 2))
    print("3eme:", recupere_nieme_etudiant_1(donnees, 3))
    print("3eme:", recupere_nieme_etudiant_2(donnees, 3))
    print("4eme:", recupere_nieme_etudiant_1(donnees, 4))
    print("4eme:", recupere_nieme_etudiant_2(donnees, 4))
    print("5eme:", recupere_nieme_etudiant_1(donnees, 5))
    print("5eme:", recupere_nieme_etudiant_2(donnees, 5))
    print("6eme:", recupere_nieme_etudiant_1(donnees, 6))
    print("6eme:", recupere_nieme_etudiant_2(donnees, 6))
    print("7eme:", recupere_nieme_etudiant_1(donnees, 7))
    print("7eme:", recupere_nieme_etudiant_2(donnees, 7))
    print("8eme:", recupere_nieme_etudiant_1(donnees, 8))
    print("8eme:", recupere_nieme_etudiant_2(donnees, 8))
    print("9eme:", recupere_nieme_etudiant_1(donnees, 9))
    print("9eme:", recupere_nieme_etudiant_2(donnees, 9))
    print("plus petite mediane:", calcule_mediane(donnees))


if __name__ == "__main__":
    main()
```
</details>



## Exercice 3 : analyse++ (pour aller plus loin)

### Question 1
!!! question " "
    Écrire une fonction qui calcule la note médiane en choisissant la *médiane moyenne* plutôt que la plus petite médiane si le nombre d'étudiants est pair.

### Question 2
!!! question " "
    Modifier la fonction qui calcule la note moyenne afin de minimiser le nombre de multiplications.

### Correction globale
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
#!/usr/bin/env python3

"""Les fonctions d'analyse++"""

import conversion
import analyse


def calcule_moyenne_optimise(donnees):
    """Le coût est toujours O(100) = O(1).

    Par contre, on fait moins de multiplications :)

    Soit nd(i) (note dessous) le nombre d'étudiants avec une note < i pour 0 ≤ i ≤ 101
    Soit ne(i) (note égale) le nombre d'étudiants avec une note = i pour 0 ≤ i ≤ 101
    Alors :
      ne(i) = nd(i+1) - nd(i)
    La somme de toutes les notes est donc :
      somme_notes = ∑ pour i = 0 à 100 de i * ne(i)
                  = ∑ pour i = 0 à 100 de i * (nd(i+1) - nd(i))
                  = ∑ pour i = 0 à 100 de i * nd(i+1) - ∑ pour i = 0 à 100 de i * nd(i))
                  =               0*nd(1) + 1*nd(2) + ... +  99*nd(100) + 100*nd(101)
                      - 0*nd(0) - 1*nd(1) - 2*nd(2) - ... - 100*nd(100)
                  =             -   nd(1) -   nd(2) - ... -     nd(100) + 100*nd(101)
                  = 100*nd(101) - ∑ pour i = 0 à 100 de nd(i)
    """

    # Le nombre total d'étudiants
    nb_etudiants_total = donnees[100][0] + len(donnees[100][1])

    # Somme nd(i)
    somme_nds = 0
    for nd, _ in donnees:
        somme_nds += nd

    # La moyenne
    somme_notes = 100 * nb_etudiants_total - somme_nds
    return somme_notes / nb_etudiants_total


def calcule_mediane_moyenne(donnees):
    """Renvoie la mediane moyenne.

    Si n = 2k + 1, c'est la note de l'étudiant de rang k + 1.
    Si n = 2k, c'est la moyenne de l'étudiant de rang k et de l'étudiant de rang k+1
    """

    # Le nombre total d'étudiants
    nb_etudiants_total = donnees[100][0] + len(donnees[100][1])

    # Nombre d'étudiants impair
    rang = (nb_etudiants_total + 1) // 2
    if nb_etudiants_total % 2 == 1:
        return analyse.recupere_note_rang(donnees, rang)
    # Nombre d'étudiants pair
    note_k = analyse.recupere_note_rang(donnees, rang)
    note_k_plus_1 = analyse.recupere_note_rang(donnees, rang + 1)
    return (note_k + note_k_plus_1) / 2


def test():
    """Quelques tests mais sur un tableau tres petit"""

    # Init et conversion
    etudiants = analyse.init_etudiants()
    print(etudiants)
    donnees = conversion.convertit_2(etudiants)

    # Nouveau calcul de la médiane
    print("plus petite mediane:", analyse.calcule_mediane(donnees))
    print("mediane moyenne :", calcule_mediane_moyenne(donnees))

    # Nouveau calcul de la moyenne
    print("moyenne:", analyse.calcule_moyenne(donnees))
    print("moyenne (avec calcul optimisé):", calcule_moyenne_optimise(donnees))


if __name__ == "__main__":
    test()
```
</details>


