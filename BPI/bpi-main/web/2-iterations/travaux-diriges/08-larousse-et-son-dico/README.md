Ce TD a pour objectif d'introduire le type abstrait dictionnaire, et de voir comment utiliser la mise en œuvre de ce type abstrait en Python.
On **s'interdit d'utiliser des fonctions récursives** dans ce TD.

## Préambule : éléments de langage

### Question 1
!!! question " "
    Donner une définition du terme **dictionnaire**.

### Question 2
!!! question " "
    Donner une définition du terme **dict** ainsi qu'une ligne de code Python permettant de créer un `dict`.

### Correction globale
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Un dictionnaire est un type abstrait composé de deux opérations permettant d'associer une valeur à une clef et de récupérer la valeur associée à une clef.

Un `dict` est le nom donnée à la structure de donnée `table de hachage` dans le monde Python.
Cette structure de données met en œuvre le type abstrait dictionnaire.

Pour rappel, le document présenté en cours synthétisant les types abstraits et les structures de données rencontrés en BPI est [disponible ici](../../adt_sdd.pdf).

Voici comment utiliser un `dict` en Python :

```python
dico = {} # équivalent à dico = dict()
dico["bill"] = 42
dico["bob"] = 17
dico = {
    "bill" : 42,
    "bob" : 17
}
```
</details>



## Exercice 1 : conjecture de Syracuse

La conjecture de Syracuse est une conjecture mathématique célèbre qui considère la suite d'entiers définie par :

- u<sub>0</sub> quelconque
- si u<sub>i</sub> est pair alors u<sub>i+1</sub> = u<sub>i</sub>/2
- sinon u<sub>i+1</sub> = 3*u<sub>i</sub> + 1

La conjecture postule que pour toute valeur entière strictement positive de u<sub>0</sub>, la suite finit toujours par atteindre la valeur 1.

### Question 1
!!! question " "
    Écrire une fonction `calcule_prochain_syracuse` prenant en entrée u<sub>i</sub> et renvoyant u<sub>i+1</sub>

### Question 2
!!! question " "
    Écrire une fonction `calcule_nb_etapes_avant_1` prenant en entrée u<sub>0</sub> et renvoyant le nombre d'étapes nécessaires avant d'atteindre 1.
    La fonction ne **doit pas être récursive**.

### Question 3
!!! question " "
    À l'aide d'un dictionnaire, écrire une fonction `calcule_nb_etapes_avant_1_memoize` reprenant le code le `calcule_nb_etapes_avant_1` mais qui tire parti des résultats des appels précédents à la fonction.
    L'appel à la fonction `calcule_nb_etapes_avant_1_memoize` prenant en entrée u<sub>0</sub> devra ajouter **uniquement** la clef u<sub>0</sub> dans le dictionnaire.

### Correction globale
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
#!/usr/bin/env python3

"""Conjecture de Syracuse avec memoisation utilisant un dict."""
import time


def calcule_prochain_syracuse(valeur):
    """Renvoie la valeur suivante de la suite de Syracuse."""
    if valeur % 2 == 0:
        return valeur // 2
    return valeur * 3 + 1


def calcule_nb_etapes_avant_1(valeur_initiale):
    """Renvoie le nombre d'etapes pour arriver à 1 à partir de la valeur donnée."""
    valeur_courante = valeur_initiale
    etapes = 0
    while valeur_courante != 1:
        valeur_courante = calcule_prochain_syracuse(valeur_courante)
        etapes += 1
    return etapes


def calcule_nb_etapes_avant_1_memoize(valeur_initiale, deja_calcules):
    """Renvoie le nombre d'etapes pour arriver à 1 à partir de la valeur donnée.

    deja_calcules contient le nombre d'étapes des valeurs initiales que nous connaissons déjà.
    """
    valeur_courante = valeur_initiale
    etapes = 0
    while valeur_courante != 1:
        # Solution intuitive mais faisant 2 accès !
        # Première recherche dans le dico O(1) (cf cours algo second semestre)
        if valeur_courante in deja_calcules:
            etapes += deja_calcules[valeur_courante]  # Deuxième recherche identique
            break
        # À remplacer par le code ci-dessous quand on maîtrise Python
        # etapes_deja_calcule = deja_calcules.get(valeur_courante, None) # Une seule recherche
        # if etapes_deja_calcule
        #    etapes += etapes_deja_calcule
        #    break
        valeur_courante = calcule_prochain_syracuse(valeur_courante)
        etapes += 1
    deja_calcules[
        valeur_initiale
    ] = etapes  # O(1) en amorti (cf cours algo second semestre)
    return etapes


def main():
    """Tests pour u_0 de 20000 à 1."""

    temps_depart = time.time()
    for valeur_initiale in range(20000, 0, -1):
        calcule_nb_etapes_avant_1(valeur_initiale)
    print("sans memoize", time.time() - temps_depart, " secondes")

    temps_depart = time.time()
    memoize = dict()
    for valeur_initiale in range(20000, 0, -1):
        calcule_nb_etapes_avant_1_memoize(valeur_initiale, memoize)
    print("avec memoize", time.time() - temps_depart, " secondes")


if __name__ == "__main__":
    main()
```
</details>



## Exercice 2 : fonctions injectives

On considère une fonction mathématique dont les résultats sont stockés dans un dictionnaire.
Chaque élément du dictionnaire contient une valeur d'entrée de la fonction et la valeur de sortie associée.
On suppose que le dictionnaire associe une valeur de sortie à chaque entrée possible.

### Question 1
!!! question " "
    Écrire une fonction `est_injective(fonction_dict)` qui vérifie si la fonction représentée par le dictionnaire `fonction_dict` est injective ou non.

###  Correction question 1
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
#!/usr/bin/env python3

"""Exercice sur les fonctions injectives"""


def est_injective(fonction):
    """Version simple qui utilise un autre dictionnaire."""
    valeurs_vues = {}
    for (
        valeur
    ) in fonction.values():  # Autant d'itérations que d'entrées dans le dico fonction
        if valeur in valeurs_vues:  # O(1)
            return False
        valeurs_vues[valeur] = True
    return True


def test():
    """Teste la fonction ci-dessus"""

    fonction_injective = {}
    for i in range(20):
        fonction_injective[i] = i + 1

    fonction_non_injective = dict(fonction_injective)
    fonction_non_injective[7] = 7

    print(est_injective(fonction_injective))
    print(est_injective(fonction_non_injective))


if __name__ == "__main__":
    test()
```
</details>



## Exercice 3 : comment faire mieux ? (pour aller plus loin)

### Question 1
!!! question " "
    Modifier la version avec memoisation de Syracuse pour stocker également tous les résultats intermédiaires.

###  Correction question 1
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
#!/usr/bin/env python3

"""Conjecture de Syracuse avec memoisation++ utilisant un dict."""

import time
import syracuse


def calcule_nb_etapes_avant_1_memoize_optim(valeur_initiale, deja_calcules):
    """On mémorise dans deja_calcules toutes les valeurs intermédiaires en plus du final."""
    valeur_courante = valeur_initiale
    etapes = 0
    valeurs_vues = []
    while valeur_courante != 1:
        # Solution intuitive mais faisant 2 accès !
        if valeur_courante in deja_calcules:
            etapes += deja_calcules[valeur_courante]
            break
        # À remplacer par le code ci-dessous quand on maîtrise Python
        # etapes_deja_calcule = deja_calcules.get(valeur_courante, None) # Une seule recherche
        # if etapes_deja_calcule
        #    etapes += etapes_deja_calcule
        #    break
        valeurs_vues.append(valeur_courante)
        valeur_courante = syracuse.calcule_prochain_syracuse(valeur_courante)
        etapes += 1
    res = etapes
    for val in valeurs_vues:
        deja_calcules[val] = etapes
        etapes -= 1
    return res


def main():
    """Tests pour u_0 de 20000 à 1."""

    temps_depart = time.time()
    memoize = dict()
    for valeur_initiale in range(20000, 0, -1):
        syracuse.calcule_nb_etapes_avant_1_memoize(valeur_initiale, memoize)
    print("avec memoize", time.time() - temps_depart, " secondes")

    temps_depart = time.time()
    memoize = dict()
    for valeur_initiale in range(20000, 0, -1):
        calcule_nb_etapes_avant_1_memoize_optim(valeur_initiale, memoize)
    print("avec memoize V2", time.time() - temps_depart, " secondes")


if __name__ == "__main__":
    main()
```
</details>

### Question 2
!!! question " "
    Modifier la fonction `est_injective` pour utiliser un `set` Python.

###  Correction question 2
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Un `set` est une table de hachage avec uniquement des clefs.

```python
#!/usr/bin/env python3

"""Exercice sur les fonctions injectives plus plus"""

import timeit
import fonctions_injectives


def est_injective_set(fonction):
    """Version qui utilise un set et teste la présence à chaque fois."""
    valeurs_vues = set()
    for (
        valeur
    ) in fonction.values():  # Autant d'itérations que d'entrées dans le dico fonction
        if valeur in valeurs_vues:  # Gratuit (O(1) en moyenne)
            return False
        valeurs_vues.add(valeur)
    return True


def est_injective_set_pythonique(fonction):
    """En une ligne ça donne ça.

    C'est cool Python non ? Oui mais ...
    Il y a toujours un mais.

    Ici on construit toujours tout le set, alors que dans la
    solution ci-dessus on s'arrête dès qu'on a deux fois le même
    élément.
    """
    return len(fonction) == len(set(fonction.values()))


def test():
    """Teste la fonction ci-dessus"""

    fonction_injective = {}
    for i in range(200_000):
        fonction_injective[i] = i + 1

    fonction_non_injective = dict(fonction_injective)
    fonction_non_injective[7] = 7

    print("Mesure de performance pour une fonction injective de taille 200000")
    time = timeit.timeit(
        lambda: fonctions_injectives.est_injective(fonction_injective), number=1
    )
    print(f"  version avec dict           = {time:.8f}")
    time = timeit.timeit(lambda: est_injective_set(fonction_injective), number=1)
    print(f"  version avec set            = {time:.8f}")
    time = timeit.timeit(
        lambda: est_injective_set_pythonique(fonction_injective), number=1
    )
    print(f"  version avec set pythonique = {time:.8f}")

    print("Mesure de performance pour une fonction non injective de taille 200000")
    time = timeit.timeit(
        lambda: fonctions_injectives.est_injective(fonction_non_injective), number=1
    )
    print(f"  version avec dict           = {time:.8f}")
    time = timeit.timeit(lambda: est_injective_set(fonction_non_injective), number=1)
    print(f"  version avec set            = {time:.8f}")
    time = timeit.timeit(
        lambda: est_injective_set_pythonique(fonction_non_injective), number=1
    )
    print(f"  version avec set pythonique = {time:.8f}")


if __name__ == "__main__":
    test()
```
</details>


## Exercice 4 : soyons fous (pour aller encore plus loin)

### Question 1
!!! question " "
    Démontrer ou invalider la conjecture de Syracuse.

###  Correction question 1
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Une idée ?
</details>
