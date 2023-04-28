## Objectif

L'objectif de cet exercice est de créer un module Python `SVG` que vous utiliserez **tout au long du semestre**.
Il est donc nécessaire de prendre le temps de bien le faire et de bien le comprendre.

## Étape 1 : comprendre ce qu'est une image `SVG`

[Scalable Vector Graphics (SVG)](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics) est un format de données textuelles basé sur `XML` permettant de décrire des images vectorielles.
Une image au format `SVG` n'est donc rien d'autre qu'un fichier contenant du texte conforme au format de données `SVG`.
On peut donc assez facilement, si l'on connaît les bases du format,  créer une image `SVG` en utilisant notre éditeur de texte favori.

Ouvrez donc votre éditeur de texte préféré et créez un fichier `ma-premiere-image.svg` avec le contenu suivant :

```svg
<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='360' height='340'>
     <g stroke='black' stroke-width='2' fill='pink'>
        <circle cx='100' cy='20' r='10'/>
        <circle cx='260' cy='20' r='10'/>
        <circle cx='20' cy='120' r='10'/>
        <circle cx='180' cy='120' r='10'/>
        <circle cx='340' cy='120' r='10'/>
        <circle cx='100' cy='220' r='10'/>
        <circle cx='260' cy='220' r='10'/>
        <circle cx='180' cy='320' r='10'/>
     </g>
</svg>
```

Ouvrez ensuite ce même ce fichier avec un visualisateur d'image, par exemple `eog` :

```console
[selvama@ensipc215]$ eog ma-premiere-image.svg
```

Félicitations, vous avez créé votre première image `SVG` qui doit ressembler à l'image suivante:

![Ma première image `SVG` ^^](./ma-premiere-image.svg "")

!!! note "Qu'est-ce que je viens d'écrire, là ?"

    Le format `SVG` s'appuie sur du texte structuré par une hiérarchie de _balises_.
    Une balise est un mot-clé permettant de décrire un ou plusieurs éléments de l'image finale.
    Comme en HTML ou en XML, le texte est structuré sous la forme d'un enchainement de
    balises ouvrantes et fermantes, formatées toujours de la même façon :

    - `<keyword option1='something' option2='somethingelse' ... optionN='anotherthing'>` pour les balises ouvrantes, où `keyword` indique quel élément de l'image est décrit par cette balise ;
    - `</keyword>` pour les balises fermantes.

    On distingue dans le fichier `SVG` ci-dessus l'utilisation de trois balises différentes :

    - `<svg>` qui définit une image au format `SVG`, avec ses dimensions et la version du standard `SVG` utilisée ;
    - `<circle>` qui décrit un cercle, avec les coordonnées de son centre et la taille de son rayon, en pixels ;
    - `<g>` qui permet de regrouper des éléments de l'image. Cette balise est utile pour factoriser des options qu'on aurait sinon du passer à chaque élément de l'image. Par exemple, ici, on n'indique pas quelle couleur de trait ou de remplissage utiliser pour dessiner les 8 cercles de l'image. On place ces cercles _à l'intérieur_ d'un groupe (entre les balises `<g>` et `</g>`), sur lequel on a positionné les attributs de couleur et d'épaisseur de trait, ainsi que la couleur de remplissage.

    On remarque aussi qu'il existe une notation contractée pour certaines balises :

    - `<keyword option=... />`

    La présence du `/` juste avant le dernier chevron fait office de balise fermante.

    Pour en savoir plus sur ces balises, et sur le format `SVG` en général :
    [https://www.w3schools.com/graphics/svg_intro.asp](https://www.w3schools.com/graphics/svg_intro.asp)

## Étape 2 : implémentez votre module Python `svg.py`

Vous devez maintenant implémenter un module Python que vous nommerez `svg.py`, aidant à la génération d'images `SVG`.

Le squelette du module, a compléter, est [disponible ici](svg.py).
Dans ce TP nous implémenterons seulement les cinq premières fonctions du fichier, c'est à dire celles qui sont affichées ci-dessous.
Les autres fonctions seront implémentées au fur et à mesure des prochains TP quand nous en auront besoin.
Parmi les cinq fonctions à implémenter ici, vous pouvez commencer par l'implémentation des fonctions `genere_balise_fin_image` et `genere_balise_fin_groupe` qui sont les plus simples car elles ne nécessitent pas l'utilisation de `f-strings`.

```python
"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

from collections import namedtuple

# Definition de la structure Point composée de deux attributs x et y
Point = namedtuple("Point", "x y")

# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaîne de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l'origine est en haut à gauche et l'axe des Y est orienté vers le
    bas.
    """
    # TODO
    ...


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_image():
    """
    Retourne la chaîne de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l'image, juste avant la fin du fichier.
    """
    # TODO
    ...


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrante
    définissant un groupe d'éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l'image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d'épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    # TODO
    ...


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_groupe():
    """
    Retourne la chaîne de caractères correspondant à la balise fermante pour un
    groupe d'éléments.
    """
    # TODO
    ...


# À implémenter dans 'TP2. Module SVG'
def genere_cercle(centre, rayon):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
    """
    # TODO
    ...
```

## Étape 3 : testez votre module Python `svg.py`

Il faut maintenant **tester** votre module.
Pour cela, créez un fichier `test_svg.py` qui importe votre module et l'utilise pour dessiner les cercles de vos rêves.

Si votre environnement de développement supporte les redirections, alors votre programme de test pourra simplement afficher le contenu de l'image `SVG` sur la sortie standard.
Celle-ci sera ensuite redirigée dans un fichier au moment de l'exécution à l'aide d'une redirection.

Si votre environnement de développement ne supporte les redirections, alors votre programme de test devra **directement** écrire le contenu de l'image `SVG` dans un fichier.
Pour cela vous utiliserez les fonctions `open`, `print` et la méthode `close` du type `str` vues dans [l'exercice précédent](../01-ecriture-fichier/README.md).

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici le code de correction du module `svg.py` :

```python
"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

from collections import namedtuple

# Definition de la structure Point composée de deux attributs x et y
Point = namedtuple("Point", "x y")

# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaîne de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.

    Remarque : l'origine est en haut à gauche et l'axe des Y est orienté vers le
    bas.
    """
    # Les parenthèses sont utilisées ici uniquement pour permettre
    # de "couper" la f-string en deux ligne afin de ne pas avoir
    # une ligne trop longue. Il existe d'autres moyen de faire,
    # mais l'utilisation de parenthèses est celui recommandé par
    # le guide de style officiel python.
    #
    # On notera également que la chaîne de caractère renvoyée
    # contient des guillemets doubles. Pour que celles-ci ne
    # soient pas considérées comme la fin de la f-string, on
    # utilise des guillemets simples pour délimiter cette
    # dernière.
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
        f'width="{largeur}" height="{hauteur}">'
    )


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_image():
    """
    Retourne la chaîne de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l'image, juste avant la fin du fichier.
    """
    return "</svg>"


# À implémenter dans 'TP2. Module SVG'
def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    Retourne la chaîne de caractères correspondant à une balise ouvrante
    définissant un groupe d'éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l'image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d'épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    return (
        f'<g stroke="{couleur_ligne}" fill="{couleur_remplissage}" '
        f'stroke-width="{epaisseur_ligne}">'
    )


# À implémenter dans 'TP2. Module SVG'
def genere_balise_fin_groupe():
    """
    Retourne la chaîne de caractères correspondant à la balise fermante pour un
    groupe d'éléments.
    """
    return "</g>"


# À implémenter dans 'TP2. Module SVG'
def genere_cercle(centre, rayon):
    """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
    """
    return f'<circle cx="{centre.x}" cy="{centre.y}" r="{rayon}" />'
```

Voici un exemple d'utilisation du module `svg.py` :

```python
#!/usr/bin/env python3
"""Un programme pour tester notre module svg"""

# On importe le module sys pour accéder à la sortie standard
import sys

# On importe tout le contenu du module svg
import svg

def teste_module_svg():
    """Fonction de test du module svg."""
    # Création de trois points
    c1 = svg.Point(10, 10)
    c2 = svg.Point(100, 100)
    c3 = svg.Point(180, 50)

    # On utilise un booléen pour choisir entre print
    # sur la sortie standard ou dans un fichier.
    # Il suffit donc de changer cette variable pour
    # contrôler la sortie du programme de test.
    SORTIE_STANDARD = True

    # On choisit où est-ce que l'on va faire nos prints
    if SORTIE_STANDARD:
        out = sys.stdout
    else:
        out = open("mon_image.svg", "w")

    # Print d'une image SVG avec 3 cercles sur la sortie standard ou dans
    # un fichier.
    # Pour pouvoir visualiser l'image il faudra donc utiliser une redirection
    # si l'on utilise la sortie standard :
    #   ./test_svg.py > mes-cercles.svg
    # Une fois l'image SVG enregistrée dans un fichier texte, on peut la
    # visualiser à l'aide de n'importe quel programme supportant ce format
    # d'image :
    #   eog mon-triangle.svg
    #   firefox mon-triangle.svg
    #   double-clic sur le fichier dans un explorateur de fichiers
    print(svg.genere_balise_debut_image(200, 200), file=out)
    print(svg.genere_balise_debut_groupe("black", "red", 5), file=out)
    print(svg.genere_cercle(c1, 30), file=out)
    print(svg.genere_balise_fin_groupe(), file=out)
    print(svg.genere_balise_debut_groupe("red", "black", 5), file=out)
    print(svg.genere_cercle(c2, 60), file=out)
    print(svg.genere_cercle(c3, 10), file=out)
    print(svg.genere_balise_fin_groupe(), file=out)
    print(svg.genere_balise_fin_image(), file=out)

    # On ferme le fichier si il a été créé
    if not SORTIE_STANDARD:
        out.close()

teste_module_svg()
```

En supplément de la correction textuelle ci-dessus, une correction plus détaillée en vidéo est disponible :

<iframe src="https://videos.univ-grenoble-alpes.fr/video/12513-ensimag-bpi-correction-de-lexercice-module-svg/?is_iframe=true" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

</details>

