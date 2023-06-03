## Énoncé

En se rappelant qu’un arbre est juste une branche sur laquelle poussent d’autres branches, créez une générateur d’arbres en `SVG`.
Voici un exemple de résultat:

![fractale.svg](fractale.svg)

### Quelques indications

On vous recommande de bien découper votre code en fonctions.

Vous pouvez par exemple écrire des fonctions de manipulations des points : addition, soustraction, multiplication par un scalaire, calcul d'une distance entre deux points, rotation autour d'un angle, etc.

On rappelle à ce propos la formule permettant de calculer la rotation d'un point (x, y) par un angle α :

`x' = x × cos(α) - y × sin(α)`

`y' = x × sin(α) + y × cos(α)`

Pour la fonction récursive permettant de dessiner les branches :
* on dessine des branches de moins en moins longues jusqu'à atteindre une taille minimale limite : ça sera le cas de base de la récursivité ;
* on tirera aléatoirement tous les paramètres des sous-branches partant de la branche courante : nombre de sous-branches, côtés d'où elles partent, angles par rapport à la branche initiale, etc.

Il n'y a pas de solution fixe attendue : laissez libre cours à votre créativité !

### Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici le programme utilisé pour générer l'image ci-dessus.
Il faut bien penser à découper notre code en fonctions.

```python
#!/usr/bin/env python3

"""Fractales : arbres, un exo sympa pour la recursion."""

from random import random, randint, choice
from math import pi, cos, sin, sqrt

import svg


def sub(point1, point2):
    """Renvoie un nouveau point égale à point1 - point2."""
    return svg.Point(point1.x - point2.x, point1.y - point2.y)


def add(point1, point2):
    """Renvoie un nouveau point égale à point1 + point2."""
    return svg.Point(point1.x + point2.x, point1.y + point2.y)


def mul(point, scalaire):
    """Renvoie un nouveau point égale à point * scalaire."""
    return svg.Point(point.x * scalaire, point.y * scalaire)


def distance_a(point1, point2):
    """Renvoie la distance entre point1 et point2"""
    x_diff = point1.x - point2.x
    y_diff = point1.y - point2.y
    return sqrt(x_diff * x_diff + y_diff * y_diff)


def rotation(point, angle):
    """Tourne point autour de l'origine de l'angle donné en radians."""
    cosinus, sinus = cos(angle), sin(angle)
    return svg.Point(
        cosinus * point.x - sinus * point.y, sinus * point.x + cosinus * point.y
    )


def dessine_branche(depart, arrivee, limite):
    """Dessine la branche entre les deux points donnés.

    Cette fonction S'appelle récursivement jusqu'à ce que
    la taille de la branche soit inférieure à la limite.
    """

    # On s'arrête quand la branche est en dessous de la
    # taille limite
    taille_branche = distance_a(depart, arrivee)
    if taille_branche < limite:
        return

    # On dessine la branche
    print(svg.genere_segment(depart, arrivee))

    # On tire entre 2 et 4 sous branches au hasard
    for _ in range(randint(2, 4)):

        cote = choice((1, -1))  # à gauche ou à droite ?
        alpha = random() / 3  # dans le tiers du haut
        nouveau_depart = add(mul(depart, alpha), mul(arrivee, (1 - alpha)))
        taille = random()  # taille quelconque mais <= 1 * taille courante
        nouvelle_arrivee_relative_to_orig = mul(sub(arrivee, depart), taille)
        nouvelle_arrivee_relative_to_orig_rot = rotation(
            nouvelle_arrivee_relative_to_orig, cote * pi / 4 * random()
        )
        nouvelle_arrivee = add(nouveau_depart, nouvelle_arrivee_relative_to_orig_rot)
        dessine_branche(nouveau_depart, nouvelle_arrivee, limite)


def dessine_arbre():
    """Génère un arbre au format SVG sur la sortie standard."""
    print(svg.genere_balise_debut_image(800, 600))
    print(svg.genere_balise_debut_groupe("black", "black", 1))
    print(svg.genere_rectangle(svg.Point(0, 0), 800, 600))
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_debut_groupe("white", "none", 1))
    dessine_branche(svg.Point(400, 550), svg.Point(400, 350), 5)
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())


if __name__ == "__main__":
    dessine_arbre()
```
</details>
## Exercices

- [Incrémente](/4-recursivite/travaux-pratiques/19-fractales/exercices/01-incremente/index.html)
- [Stack overflow](/4-recursivite/travaux-pratiques/19-fractales/exercices/02-stackoverflow/index.html)
