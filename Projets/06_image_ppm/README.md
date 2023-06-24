# Énoncé


##  I.Premiéres pas 


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


## II.Module PPM :

 Cette partie  consiste à développer un module simple de dessin permettant de tracer des cercles, des droites, des figures géométriques basiques 
 
(tels que des carrés, des triangles, des rectangles) et d'ajouter du texte à une image au format PPM (Portable Pixel Map)


### 1. génération de cercele :


l' algorithme  pour générer un cercle dans une image au format PPM  est simple :

    *  Définir les paramètres du cercle :

            Centre du cercle : (centre_x, centre_y)
            Rayon du cercle : r
            Couleur du disque 

    * Pour chaque pixel de l'image :

            Calculer la distance entre le pixel et le centre du cercle .
            distance = sqrt((x - x_centre)^2 + (y - y_centre)^2).

            Si la distance est inférieure ou égale au rayon du cercle :
                    Définir la couleur du pixel comme la couleur du cercle 
            Sinon: 
                    laisser la couleur du pixel inchangée.


### 2. génération de segement  (Algo de Bresenham):




L'algorithme de tracé de segment de Bresenham est un algorithme utilisé pour dessiner des segments de ligne à l'aide de coordonnées entières. Il est particulièrement efficace car il n'utilise que des opérations entières (pas de calculs flottants) et évite ainsi les erreurs d'arrondi.

L'algorithme de Bresenham fonctionne en tracant des pixels sur une grille en fonction d'une pente donnée (déterminée par les points de départ et d'arrivée du segment). L'algorithme décide quel pixel dessiner à chaque étape en fonction de l'erreur accumulée lors des étapes précédentes.

Voici les grandes étapes de l'algorithme de tracé de segment de Bresenham :

1. Prendre les coordonnées des points de départ (x1, y1) et d'arrivée (x2, y2) du segment.
2. Calculer la différence en x (dx = x2 - x1) et la différence en y (dy = y2 - y1).
3. Calculer l'incrément de x (step_x) en fonction de dx (1 si dx est positif, -1 sinon).
4. Calculer l'incrément de y (step_y) en fonction de dy (1 si dy est positif, -1 sinon).
5. Calculer l'erreur initiale (erreur_initiale) en utilisant la différence en x et en y.
6. Pour chaque pixel du segment :
   - Dessiner le pixel correspondant à (x, y).
   - Mettre à jour l'erreur_initiale.
   - Si l'erreur_initiale dépasse la moitié de la distance entre deux pixels adjacents, ajuster la position verticalement (y) et mettre à jour l'erreur_initiale en conséquence.
   - Déplacer horizontalement (x) selon step_x.
7. Répéter l'étape 6 jusqu'à ce que le dernier pixel du segment soit atteint.






pour plus des infos consulter le vidéo : [vidéo explique l'alog Bresenham ](https://youtu.be/Frl1cLwfs1U)



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
