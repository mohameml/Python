## Énoncé

On se propose maintenant de travailler avec le format d'image `PGM`, qui est un format texte.
Le format est très simple. Une image `PGM` contient les informations suivantes :

- une premiere ligne contenant la chaine `P2` ;
- une seconde ligne contenant deux entiers (largeur et hauteur de l’image), séparés par un espace ;
- une troisième ligne contenant `255` ;
- ensuite "hauteur" lignes contenant "largeur" entiers strictement inférieurs à 256, séparés par des espaces définissant le niveau de gris de chaque pixel.

Pour plus d'information vous pouvez consulter [la page wikipédia du format](https://fr.wikipedia.org/wiki/Portable_pixmap).

Vous devez générez un fichier `PGM` par une série d’écritures sur la sortie standard, une redirection permettant ensuite la création du fichier d’image.
Le programme fonctionne de la maniere suivante  :

- on demande à l'utilisateur de donner les dimensions de l'image ;
- on affiche l'en-tête du fichier (les trois premières lignes) ;
- on tire aléatoirement les coordonnées de deux disques (centre et rayon) **complétement** localisés dans l’image ;
- on itère enfin sur tous les pixels, affichant leurs valeurs ligne par ligne :
  - un pixel en dehors des deux disques est blanc, c'est à dire de valeur 255 ;
  - un pixel à l'intérieur de l'un ou l'autre des deux disques est plus ou moins noir, c'est à dire d'une valeur aléatoire entre 0 et 255.

Voici un exemple de résultat :

![exemple de resultat](exemple.png)

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici le code d'une correction possible :
```python
#!/usr/bin/env python3
"""Mini projet Images PGM"""
from random import randint, seed
from collections import namedtuple

from svg import Point

# Définition d'un disque : un point et un rayon
Disque = namedtuple("Disque", "centre rayon")


def contient(disque, point):
    """Fonction qui determine si un point est contenu dans un disque"""
    difference_abscisses = point.x - disque.centre.x
    difference_ordonnees = point.y - disque.centre.y
    distance_carree = (
        difference_abscisses * difference_abscisses
        + difference_ordonnees * difference_ordonnees
    )
    return distance_carree <= disque.rayon * disque.rayon


def tire_disque(largeur, hauteur):
    """Tire aléatoirement un disque complètement inclus dans une image de la taille donnée"""

    # On veut un cercle avec un rayon minimum de 20% de la
    # plus petite dimension de l'image.
    rayon_min = min(largeur * 0.2, hauteur * 0.2)

    # On tire le centre
    centre = Point(
        randint(rayon_min, largeur - rayon_min), randint(rayon_min, hauteur - rayon_min)
    )

    # On tire ensuite le rayon
    rayon_max = min(largeur - centre.x, centre.x, hauteur - centre.y, centre.y)
    rayon = randint(rayon_min, rayon_max)

    return Disque(centre, rayon)


def affiche_entete(largeur, hauteur):
    """Affichage de l'entête pgm sur stdout"""
    print("P2")
    print(f"{largeur} {hauteur}")
    print("255")


def affiche_pixels(disque1, disque2, largeur, hauteur):
    """Calcul des pixels aléatoires et affichage sur stdout"""
    for ligne in range(hauteur):
        for colonne in range(largeur):
            point = Point(colonne, ligne)
            if contient(disque1, point) or contient(disque2, point):
                print(randint(0, 255))
            else:
                print(255)


def main():
    """Point d'entrée du programme"""
    # À décommenter pour de l'aléatoire "controlé"
    # seed(41)

    # On demande à l'utilisateur la taille de l'image
    larg = int(input())
    haut = int(input())

    # On tire deux disque aléatoires
    d1 = tire_disque(larg, haut)
    d2 = tire_disque(larg, haut)

    # On affiche l'image
    affiche_entete(larg, haut)
    affiche_pixels(d1, d2, larg, haut)


if __name__ == "__main__":
    main()
```
</details>

## Exercices

- [Boucles for](/2-iterations/travaux-pratiques/05-convertisseur/exercices/01-boucles-for/index.html)
- [Le hasard fait bien les choses](/2-iterations/travaux-pratiques/06-images-pgm/exercices/01-le-hasard-fait-bien-les-choses/index.html)
