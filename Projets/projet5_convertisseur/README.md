## Énoncé

On considère dans cet exercice des ensembles de 1000 points dans le plan.
Chaque ensemble est stocké dans un fichier et chaque point est stocké sur deux lignes de ce fichier (une coordonnée par ligne).
On vous fournit trois fichiers de points : [p1.txt](p1.txt) [p2.txt](p2.txt) [p3.txt](p3.txt).

On cherche à programmer un convertisseur dans un fichier `convertisseur.py` réalisant une conversion d’un fichier de points en un fichier `SVG` représentant une image de dimension 640x480.

On utilisera des redirections pour réaliser les entrées sorties. Pour rappel, quand on lance un programme dans un terminal, le système d’exploitation lui affecte par défaut une entrée standard, c’est-à-dire un périphérique ou un fichier à partir duquel lire des données en entrée. Cette entrée standard est positionnée par défaut sur le clavier, mais on peut la modifier à l’aide d’une redirection grâce au caractère `<`. Ainsi, quand on lance dans un terminal :

```console
[selvama@ensipc215]$ ./convertisseur.py < p1.txt
```

le programme `convertisseur.py` démarre en considérant que `p1.txt` est son entrée standard.
Autrement dit, `convertisseur.py` lira ses entrées directement depuis le contenu du fichier `p1.txt` et non plus sur le clavier.

Dans cet exercice, on utilisera à la fois la redirection d’entrée et de sortie, pour faire en sorte que les affichages produits par votre programme soient sauvegardés dans un fichier `SVG` :

```console
[selvama@ensipc215]$ ./convertisseur.py < p1.txt > p1.svg
```

On ne manipulera donc pas directement de fichiers en Python ici, il suffira d’utiliser `print()` pour écrire sur la sortie standard et `input()` pour lire depuis l’entrée standard.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici le code d'une correction possible :
```python
#!/usr/bin/env python3
"""Convertisseur de fichier texte de 1000 points vers SVG"""
import svg


def convertit():
    """Version avec 2 appels à input"""
    print(svg.genere_balise_debut_image(640, 480))
    print(svg.genere_balise_debut_groupe("black", "white", 2))
    for _ in range(1000):
        abscisse = int(input())
        ordonnee = int(input())
        point = svg.Point(abscisse, ordonnee)
        chaine_svg = svg.genere_cercle(point, 1)
        print(chaine_svg)
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())
```
</details>

## Exercices

- [Boucles for](/2-iterations/travaux-pratiques/05-convertisseur/exercices/01-boucles-for/index.html)
