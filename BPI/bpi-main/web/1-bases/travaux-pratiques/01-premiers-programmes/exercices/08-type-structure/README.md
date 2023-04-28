## Énoncé

L'objectif de cet exercice est de comprendre comment créer ses propres structures de données.
En python, il existe différentes façons d'atteindre cet objectif.
Dans le cadre du cours BPI, nous utiliserons la fonction `namedtuple` disponible dans le module `collections`.

Créez un programme `geom.py` définissant une structure `Point` ainsi qu'une structure `Triangle` en utilisant la fonction `namedtuple`.

- La structure `Point` sera composée des attributs `x` et `y`, définissant les coordonnées du point dans un espace à deux dimensions ;
- La structure `Triangle` sera composée de trois `Point`, sous la forme d'attributs nommés `p1`, `p2` et `p3`.

Implémentez également la fonction suivante dans votre programme :

```python
def affiche_triangle(triangle):
    """ Affiche les trois points de triangle sur la sortie standard """
    # TODO
    ...
```

**Testez** l'utilisation de vos nouvelles structures en créant des points ainsi qu'un triangle puis en affichant ce dernier.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
`geom.py` :

```python
#!/usr/bin/env python3

"""
Un programme pour illustrer la notion de "structure" en python.

Nous n'utilisons pas de classe volontairement ici alors que celles-ci
pourraient également être utilisées. En effet, python est un langage
impératif qui supporte la programmation orientée objet mais l'objectif
de ce cours concerne seulement l'impératif.
"""

# On importe seulement la fonction namedtuple depuis le module collections
from collections import namedtuple

def affiche_triangle(triangle):
    """affiche les trois points de triangle sur la sortie standard"""
    print("triangle = (" + str(triangle.p1.x) + "," + str(triangle.p1.y) + ") ("
          + str(triangle.p2.x) + "," + str(triangle.p2.y) + ") ("
          + str(triangle.p3.x) + "," + str(triangle.p3.y) + ")")


def test_creation_affichage_triangle():
    """fonction de test: création et affichage"""
    # Definition de la structure Point composée de deux attributs x et y
    Point = namedtuple("Point", "x y")

    # Definition de la structure Triangle composée de trois attributs p1, p2 et p3
    Triangle = namedtuple("Triangle", "p1 p2 p3")

    # Création de trois points
    point1 = Point(50, 0)
    point2 = Point(0, 50)
    point3 = Point(50, 50)

    # Création et affichage d'un triangle
    tri = Triangle(point1, point2, point3)
    affiche_triangle(tri)

test_creation_affichage_triangle()
```
</details>
