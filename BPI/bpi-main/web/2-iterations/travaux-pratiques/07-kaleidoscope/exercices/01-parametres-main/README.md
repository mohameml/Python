## Énoncé

Certains programmes ont besoin de recevoir un argument dès leur lancement pour pouvoir être utiles.
Par exemple, un visualisateur d'image tel que `eog` serait complètement inutile s'il ne recevait pas en argument le chemin d'un fichier contenant une image.

Dans un terminal, on lance donc `eog` de la manière suivante :

```console
[selvama@ensipc215]$ eog /home/manu/images/ma-premiere-image.svg
```

Dans cet exemple, on donne donc le chemin `/home/manu/images/ma-premiere-image.svg` en argument au programme `eog`.

Quelque soit le langage de programmation utilisé par les développeurs de l'application `eog`, ces derniers ont utilisé un mécanisme offert par le langage pour que le programme puisse recevoir un argument depuis le monde extérieur à son lancement.

En Python, c'est le module `sys` qui fournit cette fonctionnalité au travers de la variable `sys.argv`.
Le contenu de cette variable est automatiquement rempli par l'interpréteur avec tous les arguments donnés sur la ligne de commandes au moment du lancement du programme.

Écrivez un programme `affiche_arguments.py` qui affiche sur la sortie standard tous les arguments qui lui sont donnés au lancement comme illustré ci-dessous.
Si l'utilisateur lance le programme sans argument, un message indiquant comment lancer le programme doit d'afficher.

```console
[selvama@ensipc215]$ ./affiche_arguments.py en BPI on aime le nombre 41
./affiche_arguments
en
BPI
on
aime
le
nombre
41

[selvama@ensipc215]$ ./affiche_arguments.py
Usage : ./affiche_arguments.py  arg1 arg2 ... argN
```

Que remarquez-vous de particulier à propos des arguments affichés ?

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

`affiche_arguments.py` :

```python
#!/usr/bin/env python3
""" Un programme qui illustre la notion d'arguments du programme principal """


# On importe sys pour pouvoir accéder à sys.argv, qui
# est une `list` de mots, chaque mot représentant
# un argument sur la ligne de commandes, sous la forme
# d'une chaîne de caractères.
import sys

# Si on ne donne pas d'arguments sur la ligne de commandes,
# ce programme n'est pas très utile !
# Du coup on regarde la longueur de la `list`.
# Dans notre cas, elle doit être supérieure à 1 : en effet
# sys.argv[0] contient toujours le programme lui-même, tel
# qu'il a été lancé dans le terminal.
if len(sys.argv) == 1:
    # Pratique pour afficher le nom du programme quel qu'il soit !
    print("Usage :", sys.argv[0], " arg1 arg2 ... argN")
else:
    # C'est fastoche, on a juste à parcourir sys.argv !
    for arg in sys.argv:
        print(arg)

```
</details>
