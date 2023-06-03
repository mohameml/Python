## Énoncé


Dans ce premier mini-projet, on se propose d’écrire un programme simulant un mini Logo.
[Logo](http://fr.wikipedia.org/wiki/Logo_%28langage%29) est un langage de programmation vous permettant de contrôler une petite tortue représentant la pointe d’un crayon, dessinant une image lors de ses déplacements.

![logo de Logo](logo.jpg)

La tortue obéit à différentes commandes mais nous ne considérerons dans ce TP que les commandes suivantes :

- *avance*
- *tourne_droite*
- *tourne_gauche*
- *leve_crayon*
- *baisse_crayon*

Votre travail consiste à implémenter toutes les fonctions du module `logo.py` dont le squelette vous est [fourni ici](logo.py) et affiché ci dessous.
Comme vous le constatez, le module `logo.py` **utilise** le module `svg.py` que nous avons développé dans le TP précédent.
Si vous ne savez pas comment utiliser ce module, cela signifie que vous n'avez pas fait l'exercice à ce sujet lors de la séance précédente et que vous trouverez [ici](../../../02-module-svg-and-co/exercices/04-installation-d-un-module/README.md).

```python
"""Module tortue logo.

Ce module implémente les primitives graphiques basiques
d'une tortue logo.
"""

import svg


def avance(abscisse, ordonnee, direction, crayon_en_bas, distance):
    """Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un Point (défini dans notre module svg).
    """
    # TODO
    ...


def tourne_droite(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    # TODO
    ...


def tourne_gauche(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    # TODO
    ...
```

Nous vous fournissons le programme principal `test_logo.py` [ici](test_logo.py) et affiché ci dessous.
Une lecture attentive de ce programme de test vous permettra de **bien comprendre** ce que doit faire chacune des fonctions du module `logo.py`.

```python
#!/usr/bin/env python3

"""Programme pour tester le module logo."""

import logo
import svg


def main():
    """On crée un dessin a l'aide du module logo."""

    # On démarre notre image SVG
    print(svg.genere_balise_debut_image(100, 100))
    # En python on peut nommer les arguments quand on appelle une
    # fonction. Cela rend le code beaucoup plus lisible en général.
    print(
        svg.genere_balise_debut_groupe(
            couleur_ligne="black", couleur_remplissage="none", epaisseur_ligne=3
        )
    )

    # Notre tortue est représentée par 4 infos :
    abscisse = 0.0
    ordonnee = 0.0
    direction = 90.0  # angle du regard de la tortue en degrés
    # par rapport à l'horizontale, la tortue
    # regarde donc vers le haut.
    crayon_en_bas = False

    # On se déplace sans dessiner
    direction = logo.tourne_droite(direction, 180.0)
    # Ici on fait du tuple unpacking : on récupère d'un coup les 2 éléments du tuple.
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 50.0)
    direction = logo.tourne_gauche(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 50.0)
    direction = logo.tourne_gauche(direction, 90.0)

    # On va dessiner un premier truc
    crayon_en_bas = True
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On se déplace sans dessiner
    crayon_en_bas = False
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On dessine un deuxième truc
    crayon_en_bas = True
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)

    # On se déplace sans dessiner
    crayon_en_bas = False
    direction = logo.tourne_droite(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 20.0)
    direction = logo.tourne_gauche(direction, 90.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 10.0)

    # On dessine un troisième truc
    crayon_en_bas = True
    direction = logo.tourne_gauche(direction, 45.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 30.0)
    direction = logo.tourne_gauche(direction, 45.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 30.0)
    direction = logo.tourne_gauche(direction, 45.0)
    abscisse, ordonnee = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, 30.0)

    # On termine l'image SVG
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())


main()
```

Ce programme ne doit pas être modifier mais doit **obligatoirement être utilisé pour tester** votre module `logo.py`.
Comparez le résultat avec celui de vos camarades pour vous convaincre (ou non au contraire) que votre implémentation du module `logo.py` est correcte.

Pour dessiner des segments dans votre module `logo.py`, vous utiliserez la fonction suivante que vous devez rajouter à votre module `svg.py` :

```python
def genere_segment(dep, arr):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr.
    """
    # TODO
    ...
```

Il est assez facile de se tromper dans les calculs pour ce TP, n’hésitez pas à interpeller votre enseignant pour qu’il vous explique comment déboguer votre programme.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici la correction du module `logo.py` :

```python
"""Module tortue logo.

Ce module implémente les primitives graphiques basiques
d'une tortue logo.
"""

from math import cos, sin, pi

import svg


def avance(abscisse, ordonnee, direction, crayon_en_bas, distance):
    """Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un Point (défini dans notre module svg).
    """
    # Il faut que l'on fasse un peu de trigonométrie.
    # On avance suivant un vecteur donné par la direction.
    # Attention : comme la doc nous le rappelle cos et sin
    # prennent des angles en radians.
    vecteur = (cos(direction * pi / 180), sin(direction * pi / 180))
    nouvelle_abscisse = abscisse + vecteur[0] * distance
    nouvelle_ordonnee = ordonnee - vecteur[1] * distance
    nouveau_point = svg.Point(nouvelle_abscisse, nouvelle_ordonnee)
    # On dessine maintenant
    if crayon_en_bas:
        segment_svg = svg.genere_segment(svg.Point(abscisse, ordonnee), nouveau_point)
        print(segment_svg)

    return nouveau_point


def tourne_droite(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return direction - angle


def tourne_gauche(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return direction + angle
```

Voici la correction de la fonction `genere_segmnent` :
```python
def genere_segment(dep, arr):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr.
    """
    return f'<line x1="{dep.x}" x2="{arr.x}" y1="{dep.y}" y2="{arr.y}" />'
```
</details>
## Exercices

- [Unix is love](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/01-unixislove/index.html)
- [Monsieur propre](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/02-monsieur-propre/index.html)
- [0+0](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/04-somme/index.html)
- [Par où on rentre ?](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/05-par-ou-on-rentre/index.html)
- [Premier module](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/06-modules/index.html)
- [Structures](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/08-type-structure/index.html)
- [Création de fichiers](/1-bases/travaux-pratiques/02-module-svg-and-co/exercices/01-ecriture-fichier/index.html)
