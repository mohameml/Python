## Énoncé

L’objectif de cet exercice est d’implémenter une interface en mode texte pour le jeu *lights out* [page Wikipedia du jeu](https://en.wikipedia.org/wiki/Lights_Out_(game)).

Le principe du jeu est le suivant.
On se place sur un plateau de jeu rectangulaire de longueur `L` et de hauteur `H`, possédant `N = L x H` cases.
Ces cases peuvent être soit éteintes, soit allumées.
On a la règle d’évolution suivante : lorsqu'on choisit une case, celle-ci change d’état ainsi que ses quatre voisines dans les directions sud, est, nord, ouest, du moins celles qui existent dans les limites du plateau.
Les cellules du coin n'ont que deux voisines, et celles de la bordure sauf les coins en ont trois.
Le jeu consiste à trouver sur quelles cases appuyer pour finir en ayant toutes les cases éteintes, étant donnée une situation de départ inscrite dans un fichier texte.
Vous trouverez  sur [cette vidéo](tout_eteint.webm) un exemple de jeu.

Votre programme devra lire l'état initial du jeu depuis un fichier texte.
Ce fichier contient `H` lignes de `L` caractères.
Un caractère est soit `.` pour indiquer une case allumée, soit `_` pour indiquer une case éteinte.
Vous pouvez télécharger des états initiaux de [différents niveaux ici](niveaux.tgz).

Côté interface graphique, nous vous conseillons dans un premier temps de partir sur quelque chose de simple, en associant par exemple un caractère à une case allumée et un caractère à une case éteinte, comme pour les fichiers d'entrée, comme ceci :

```
+----+
|..o.|
|....|
|o...|
|..oo|
+----+
```

Ici, les positions A3, C1, D3 et D4 sont allumées, les autres sont éteintes. Et oui, ici, les caractères utilisés ne sont pas les mêmes que ceux qui se trouvent dans les fichiers de `niveaux.tgz`, mais en vrai, osef, comme on dit.

Une fois que votre programme fonctionne à l'aide de cette interface sommaire, vous pourrez étendre votre implémentation pour permettre l'association de plusieurs caractères à une case du plateau, comme sur la capture d'écran du jeu ci-dessous :

![capture écran jeu](tout_eteint.png)

Le caractère unicode utilisé pour afficher un carré blanc ici est `\u2588`. N'hésitez pas à l'utiliser dans votre implémentation si vous voulez avoir un rendu ressemblant à ce qui est montré dans la correction.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici le code d'une correction possible :
```python
#!/usr/bin/env python3
"""Jeu du tout éteint"""
import sys


def print_line(line):
    """Prints a line"""
    for charac in line:
        for _ in range(5):
            if charac == ".":
                print("\u2588", end="")
            else:
                print(" ", end="")
    print("|")


def print_game(state):
    """Print the game"""
    print("\033c")
    print("     1    2    3    4    5   ")
    print("  +-------------------------+")
    line_no = 0
    for line in state:

        # First line
        print("  |", end="")
        print_line(line)

        # Second line
        print(chr(line_no + 65), end="")
        print(" |", end="")
        print_line(line)

        # Third line
        print("  |", end="")
        print_line(line)

        line_no += 1
    print("  +-------------------------+")
    print()


def finished(state):
    """Check if finished"""
    for line in state:
        for charac in line:
            if charac != "_":
                return False
    return True


def touch(line_1, col_1, line_2, col_2):
    """Check if touch"""

    # same
    if line_2 == line_1 and col_2 == col_1:
        return True

    # above
    if line_2 == line_1 - 1 and col_2 == col_1:
        return True

    # below
    if line_2 == line_1 + 1 and col_2 == col_1:
        return True

    # left
    if line_2 == line_1 and col_2 == col_1 - 1:
        return True

    # right
    if line_2 == line_1 and col_2 == col_1 + 1:
        return True

    return False


def play(state, played):
    """Play a user turn"""
    played_line_no = ord(played[0]) - ord("A")
    played_col_no = int(played[1]) - 1
    for line_no, line in enumerate(state):
        for col_no, charac in enumerate(line):
            if touch(line_no, col_no, played_line_no, played_col_no):
                if charac == "_":
                    state[line_no][col_no] = "."
                else:
                    state[line_no][col_no] = "_"


def main():
    """Point d'entree du programme"""

    # Parse arguments
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "filename")
        sys.exit()

    # Parse file to get initial state
    state = []
    with open(sys.argv[1]) as level_file:
        for line in level_file:
            characs = []
            for charac in line.strip():
                characs.append(charac)
            state.append(characs)

    # Play the game
    print_game(state)
    play_count = 0
    while not finished(state):
        print("Choisissez une case à jouer:")
        played = input()
        play_count += 1
        play(state, played)
        print_game(state)
    print("Felicitations, vous avez gagné en", play_count, "coup(s)")


if __name__ == "__main__":
    main()
```
</details>

## Exercices

- [Le juste prix](/2-iterations/travaux-pratiques/10-tout-eteint/exercices/01-le-juste-prix/index.html)
- [Tableaux](/2-iterations/travaux-pratiques/09-sous-suite/exercices/01-tableaux/index.html)
- [Boucles for](/2-iterations/travaux-pratiques/05-convertisseur/exercices/01-boucles-for/index.html)
- [Ligne de commandes et arguments](/2-iterations/travaux-pratiques/07-kaleidoscope/exercices/01-parametres-main/index.html)
- [Lecture de fichier](/2-iterations/travaux-pratiques/09-sous-suite/exercices/02-lecture-fichier/index.html)
