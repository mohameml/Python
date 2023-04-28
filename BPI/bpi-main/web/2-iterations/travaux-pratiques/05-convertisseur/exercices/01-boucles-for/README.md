## Énoncé

Contrairement à une boucle *tant que* qui s'arrête sur une condition, une boucle *pour* en Python permet de parcourir un ensemble d'éléments.
Bien que ce type de boucle soit tout à fait intuitif, de nombreuses opérations ont lieu dans notre dos dès lors que l'on l'utilise la construction `for X in Y` en Python.

Ce sont ces opérations cachées qui nous permettent de parcourir à l'aide d'une simple boucle `for` :

- un ensemble de nombres, c'est à dire un `range`, pour obtenir les nombres un à un ;
- une chaîne de caractères pour obtenir les caractères un à un ;
- un tuple pour obtenir les éléments qui le composent un à un ;
- une `list` pour obtenir les éléments qui la composent un à un ;
- un fichier ouvert avec `open` pour obtenir les lignes qu'il contient une par une.

Nous ne rentrerons pas dans le détail des opérations cachées pour le moment.
L'objectif de cet exercice est simplement d'utiliser des boucles `for`.

Écrivez un programme `for.py` affichant un à un les éléments (caractère ou nombre), avec retour à la ligne après chaque élément, contenus dans les variables ci-dessous. Vous utiliserez une boucle, contenant éventuellement une ou deux sous boucle, pour chaque variable.

```python
une_chaine = "123"
une_list = [1, 2, 3]
un_tuple = (1, 2, 3)
un_intervalle = range(1, 4)
une_list_2D = ["toto", range(3), ["t", "o", "t", "o"]]
un_tuple_2D = ([1, 2, 3], [4, 5, 6])
une_liste_3D = [[[1, 2], [3, 4]], [[5, 6]]]
```

Factorisez ensuite votre code en créant 3 fonctions :

- une fonction pour afficher tous les éléments d'une variable à "une dimension" ;
- une fonction pour afficher tous les éléments d'une variable à "deux dimension" ;
- une fonction pour afficher tous les éléments d'une variable à "trois dimensions" ;

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

`for.py` :

```python
#!/usr/bin/env python3
"""exemples d'utilisation de boucle for"""

# Les variables que l'on souhaite parcourir
une_chaine = "123"
une_list = [1, 2, 3]
un_tuple = (1, 2, 3)
un_intervalle = range(1, 4)
une_list_2D = ["toto", range(3), ["t", "o", "t", "o"]]
un_tuple_2D = ([1, 2, 3], [4, 5, 6])
une_liste_3D = [[[1, 2], [3, 4]], [[5, 6]]]

# Variables à une dimension --> une seule boucle
print("éléments de une_chaine :")
for car in une_chaine:
    print(f"  {car}")

print("éléments de une_list :")
for nb in une_list:
    print(f"  {nb}")

print("éléments de un_tuple :")
for nb in un_tuple:
    print(f"  {nb}")

print("éléments de un_intervalle :")
for nb in un_intervalle:
    print(f"  {nb}")

# Variables à deux dimensions --> deux boucles
print("éléments de une_list_2D :")
for sous_ensemble in une_list_2D:
    for element in sous_ensemble:
        print(f"  {element}")  # l'appel à str est nécessaire, pourquoi ?

print("éléments de un_tuple_2D :")
for sous_ensemble in un_tuple_2D:
    for element in sous_ensemble:
        print(f"  {element}")

# Variable à trois dimensions --> trois boucles
print("éléments de une_liste_3D :")
for sous_ensemble in une_liste_3D:
    for sous_sous_ensemble in sous_ensemble:
        for element in sous_sous_ensemble:
            print(f"  {element}")

# Pour factoriser notre code, grace au typage dynamique
# du langage Python, nous pourrions définir des fonctions
# de parcours de dimension donnée


def parcourt_une_dimension(a_parcourir):
    """Parcourt une variable de dimension 1"""
    for elem in a_parcourir:
        print(f"  {elem}")


def parcourt_deux_dimensions(a_parcourir):
    """Parcourt une variable de dimension 2"""
    for sous_ens in a_parcourir:
        for elem in sous_ens:
            print(f"  {elem}")


def parcourt_trois_dimensions(a_parcourir):
    """Parcourt une variable de dimension 3"""
    for sous_ens in a_parcourir:
        for sous_sous_ens in sous_ens:
            for elem in sous_sous_ens:
                print(f"  {elem}")


# Et ensuite utiliser ces fonctions pour afficher à nouveau
# nos variables

# Variables à une dimension --> une seule boucle
print("éléments de une_chaine :")
parcourt_une_dimension(une_chaine)
print("éléments de une_list :")
parcourt_une_dimension(une_list)
print("éléments de un_tuple :")
parcourt_une_dimension(un_tuple)
print("éléments de un_intervalle :")
parcourt_une_dimension(un_intervalle)

# Variables à deux dimensions --> deux boucles
print("éléments de une_list_2D :")
parcourt_deux_dimensions(une_list_2D)
print("éléments de un_tuple_2D :")
parcourt_deux_dimensions(un_tuple_2D)

# Variables à trois dimensions --> trois boucles
print("éléments de une_liste_3D :")
parcourt_trois_dimensions(une_liste_3D)
```
</details>
