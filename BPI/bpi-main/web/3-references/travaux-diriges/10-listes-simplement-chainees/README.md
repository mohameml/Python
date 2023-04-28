L'objectif de ce TD est de réaliser une structure de données liste chaînée en Python afin de :

- se familiariser avec cette structure de données et notamment aux coûts des opérations associées ;
- s'exercer à la création de classes et à leur utilisation ;
- manipuler des variables, des références et des instances.

## Exercice 1 : création de la structure de données

Pour créer une liste simplement chaînée, nous allons utiliser les deux classes suivantes :

```python
class Cellule:
    """Une cellule d'une liste simplement chaînée.

    Possède une référence vers la valeur et
    une référence vers la cellule suivante.
    """
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

class ListeSimplementChainee:
    """Une liste simplement chaînée.

    Possède une référence vers la tête de liste.
    """
    def __init__(self):
        self.tete = None
```

### Question 1
!!! question " "
    En utilisant les classes ci-dessus, créer la liste simplement chaînée `l` suivante : `1 --> 2 --> 3 --> 42`

###  Correction question 1
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
def cree_liste():
    """Création d'une liste simplement chaînée."""

    # Création et chaînage des cellules
    cell42 = Cellule(42, None)
    cell3 = Cellule(3, cell42)
    cell2 = Cellule(2, cell3)
    cell1 = Cellule(1, cell2)

    # En une ligne ça donnerait ça
    # cell1 = Cellule(1, Cellule(2, Cellule(3, Cellule(42, None))))

    # Création de la liste simplement chaînée
    l = ListeSimplementChainee()
    l.tete = cell1
```
</details>

### Question 2
!!! question " "
    Dessiner la zone mémoire correspondant à `l`

###  Correction question 2
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
![mémoire](liste_chainee.svg)
</details>

### Question 3
!!! question " "
    Comment accéder à la valeur 3 à partir de `l` ?

###  Correction question 3
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
`l.tete.suivant.suivant.valeur`

Correction vidéo pour l'ensemble de l'exercice :

<iframe src="https://videos.univ-grenoble-alpes.fr/video/12991-ensimag-bpi-td10-correction-exercice-1/?is_iframe=true" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>
</details>


## Exercice 2 : opérations de base

Nous allons maintenant créer des fonctions manipulant une `ListeSimplementChainee` et réalisant des opérations de base du type de donnée abstrait (ADT) *séquence de taille variable* tel que [nous l'avons défini en cours](../../../2-iterations/adt_sdd.pdf).


### Question 1
!!! question " "
    Écrire une fonction permettant d'ajouter une valeur en tête de la liste simplement chaînée.

###  Correction question 1
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tête de liste."""
    liste_chainee.tete = Cellule(valeur, liste_chainee.tete)
```
</details>

### Question 2
!!! question " "
    Comment fait-on pour ajouter une valeur en tête d'une `list` Python, c'est à dire d'un tableau dynamique ?
    Quelle est la différence fondamentale avec l'ajout en tête dans une liste simplement chaînée ?

###  Correction question 2
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
L'ajout en tête dans un tableau dynamique nécessite de déplacer tous les éléments d'un cran vers la droite comme [nous l'avons vu en cours](../../../2-iterations/2-iterations.pdf).
Le coût de cette opération est donc **dépendant du nombre d'éléments** dans le tableau dynamique.

Pour une liste simplement chaînée, l'ajout en tête consiste simplement à créer une nouvelle cellule dont le suivant est la tête puis à définir cette nouvelle cellule comme la tête.
Le coût est donc **indépendant du nombres d'éléments** dans la liste simplement chaînée.
</details>

### Question 3
!!! question " "
    Écrire une fonction permettant de rechercher la première cellule contenant une valeur donnée.

###  Correction question 3
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
def recherche(liste_chainee, valeur):
    """Renvoie la première cellule ayant la valeur donnée ou None."""
    cell = liste_chainee.tete
    while cell is not None:
        if cell.valeur == valeur:
            return cell
        cell = cell.suivant
    return None
```
</details>

### Question 4
!!! question " "
    Quelle est la différence avec la recherche dans une `list` Python, c'est à dire un tableau dynamique ?

###  Correction question 4
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Il n'y a pas de différence fondamentale, car pour les deux structures de données il faut parcourir les éléments jusqu'à trouver (ou non) la valeur recherchée.
</details>

### Question 5
!!! question " "
    Écrire une fonction permettant d'ajouter une valeur à la fin de la liste simplement chaînée.

###  Correction question 5
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
def ajoute_en_fin(liste_chainee, valeur):
    """Ajoute une cellule en fin de liste."""

    # Création de la nouvelle cellule
    nouveau_dernier = Cellule(valeur, None)

    # Si la liste était vide, la nouvelle cellule devient la tête
    if liste_chainee.tete is None:
        liste_chainee.tete = nouveau_dernier

    # Sinon la liste n'était pas vide, il nous faut la dernière cellule
    # pour se raccrocher dessus.
    else:

        # On cherche la dernière cellule
        dernier = liste_chainee.tete
        while dernier.suivant is not None:
            dernier = dernier.suivant

        # On se raccroche à la dernière cellule
        dernier.suivant = nouveau_dernier
```
</details>

### Question 6
!!! question " "
    Comment fait-on pour ajouter une valeur à la fin d'une `list` Python, c'est à dire d'un tableau dynamique ?
    Quelle est la différence fondamentale avec l'ajout à la fin dans une liste simplement chaînée ?
    Comment pourrait-on faire pour améliorer notre liste simplement chaînée ?

###  Correction question 6
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
L'ajout à la fin dans un tableau dynamique consiste simplement à rajouter l'élément dans la première case libre comme [nous l'avons vu en cours](../../../2-iterations/2-iterations.pdf).
Dans certain cas, on l'imagine bien, il faudra agrandir le tableau.
Néanmoins le coût amorti dont nous parlerons au second semestre dans le cours d'algorithme et structure de données, c'est à dire le coût moyen sur plusieurs opérations d'ajout, **ne dépend pas du nombre d'éléments** dans le tableau dynamique.

Pour notre liste simplement chaînée dans laquelle nous avons seulement une référence vers la tête, l'ajout en fin nécessite de parcourir toute la liste pour trouver la dernière cellule sur laquelle la nouvelle cellule sera "raccrochée".
Le coût est donc **dépendant du nombres d'éléments** dans la liste simplement chaînée.

Si nous avions dans notre classe liste simplement chaînée une référence vers le dernier élément en plus de la référence vers la tête (comme nous le ferons en TP), alors l'insertion en fin serait **indépendante du nombres d'éléments**.
</details>

### Question 7
!!! question " "
    Écrire une fonction permettant de supprimer la première cellule contenant une valeur donnée.

###  Correction question 7
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
def supprime(liste_chainee, valeur):
    """Supprime la première cellule ayant la valeur donnée ou ne fait rien."""

    # On cherche la cellule à supprimer
    prec = None
    cell = liste_chainee.tete
    while cell is not None and cell.valeur != valeur:
        prec = cell
        cell = cell.suivant

    # Si on a trouvé, on supprime
    if cell is not None:

        # Suppression de la tête
        if prec is None:
            liste_chainee.tete = cell.suivant

        # Sinon
        else:
            prec.suivant = cell.suivant
```
</details>

### Question 8
!!! question " "
    Sans écrire le code, s'interroger sur la différence entre une suppression en tête dans une liste chaînée et dans une `list` Python, donc un tableau dynamique.
    Qu'en est-il pour une suppression à la fin ?

###  Correction question 8
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Pour la suppression en tête, celle-ci est gratuite pour une liste simplement chaînée car il suffit de changer la tête.
Par contre elle est coûteuse pour un tableau dynamique car il faut déplacer tous les éléments d'un cran vers la gauche.

Pour la suppression en fin, elle est coûteuse pour une liste simplement chaînée (même si on rajoute une référence vers la fin) car il faut retrouver l'avant dernier élément.
Par contre elle est gratuite pour un tableau dynamique car il suffit de supprimer l'élément dans la dernière case du tableau.

Les choses importantes à retenir de cet exercice sont les suivantes :

- l'insertion en tête d'une liste simplement chaînée est gratuite ;
- l'ajout à la fin d'une liste simplement chaînée coûte un parcours complet (sauf si on rajoute une référence vers la fin, ce qu'on fera en TP) ;
- le coût de la recherche est le même dans une liste simplement chaînée que dans un tableau dynamique, c'est à dire que dans une `list` Python ;
- avec une liste simplement chaînée on peut réaliser toutes les opérations fournies par la `list` Python, donc un tableau dynamique, mais les coûts sont différents ;
- la suppression en tête est gratuite pour une liste simplement chaînée et coûteuse pour un tableau dynamique car il faut déplacer tous les élements d'un cran vers la gauche ;
- la suppression en fin est coûteuse pour une liste simplement chaînée (même si on rajoute une référence vers la fin) et gratuite pour un tableau dynamique.

Correction vidéo pour l'ensemble de l'exercice :

<iframe src="https://videos.univ-grenoble-alpes.fr/video/13007-ensimag-bpi-td10-correction-exercice-2/?is_iframe=true" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

</details>


## Exercice 3 : c'est renversant (pour aller plus loin)

### Question 1
!!! question " "
    Écrire une fonction qui renverse une liste simplement chaînée. Par exemple, `1 --> 2 --> 3 --> 42` devient `42 --> 3 --> 2 --> 1`.


###  Correction question 1
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
#!/usr/bin/env python3

"""Opérations de base sur les listes simplement chaînées"""

import traceur
from liste_chainee import ListeSimplementChainee, Cellule
from liste_chainee_ops import ajoute_en_tete

@traceur.trace()
def renverse(liste_chainee):
    """Renverse la liste chaînée donnée en argument"""

    # On renverse tout le monde
    prec = None
    cell = liste_chainee.tete
    while cell is not None:
        suivant = cell.suivant
        cell.suivant = prec
        prec = cell
        cell = suivant

    # Ne pas perdre la tête
    liste_chainee.tete = prec

    return liste_chainee # Pour avoir la trace visuelle

def teste_renverse():
    """Teste le renversement"""
    l = ListeSimplementChainee()
    renverse(l) # teste sur une liste vide
    ajoute_en_tete(l, 42)
    renverse(l) # teste sur une liste singleton
    ajoute_en_tete(l, 3)
    ajoute_en_tete(l, 2)
    ajoute_en_tete(l, 1)
    renverse(l) # teste sur une liste générale

if __name__ == "__main__":
    teste_renverse()
```
</details>
