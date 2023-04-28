## Énoncé

En programmation, il est parfois utile de générer des nombres aléatoires.
Dans tous les langages de programmation, vous trouverez donc un moyen de générer des nombres aléatoires, souvent au travers de fonctions standards.

En Python, c'est le module `random` qui fournit tout le nécessaire pour générer des nombres aléatoires.

1. Commencez par jouer un peu avec ce module dans l'interpréteur interactif Python que vous lancerez en tapant simplement la commande `python` dans un terminal. Importez d'abord le module `random` en saisissant la ligne :
```python
import random
```
puis lisez l'aide en ligne des fonctions `random.randint` et `random.choice` (`help(random.randint)` pour `randint`).

2. Toujours dans l'interpréteur interactif, créez une `list` de quatre entiers aléatoires de valeur comprise entre 0 et 10, en utilisant la fonction `random.randint()`.

3. Utilisez ensuite la fonction `random.choice` pour choisir aléatoirement une valeur parmi les quatre de la `list`. Appelez plusieurs fois cette fonction pour constater qu'elle ne renvoie pas toujours la même valeur.

4. Les nombres aléatoires sont générés à partir d'une constante, la _graine_. Par défaut, cette graine change à chaque nouvelle exécution du programme, simulant ainsi un comportement aléatoire. Il est possible de définir la même graine pour toutes les exécutions d'un programme en appelant la fonction `random.seed()`. Le programme suivant utilise le générateur de nombres aléatoires pour simuler le comportement d'une IA qui joue à "Pierre, feuille, ciseaux". Pour cet exercice, vous devez commencer par analyser le code suivant et le comprendre. Ensuite, à l'aide de la fonction `random.seed`, modifiez ce programme pour être certain de toujours gagner les `X` premiers coups du jeu, avec `X` dépendant de votre capacité mémoire à vous, utilisateur humain. Autrement dit, faîtes en sorte que l'ordinateur joue la même séquence de coups à chaque exécution du programme.

```python
#!/usr/bin/env python3
"""Papier caillou ciseaux"""

import random


def main():
    """point d'entrée du programme"""

    plays = ["paper", "rock", "scissors"]

    while True:

        player = input("paper, rock, scissors ?\n")
        computer = plays[random.randint(0, 2)]

        if player == computer:
            print("Égalité!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("Invalid play. Check your spelling please !")


if __name__ == "__main__":
    main()
```

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
# dans l'interpréteur Python :
>>> import random
>>> sequence = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
>>> sequence
[9, 8, 6, 0]
>>> random.choice(sequence)
8
>>> random.choice(sequence)
0
>>> random.choice(sequence)
8
>>> random.choice(sequence)
9
```

`le_hasard_fait_bien_les_choses.py` :

```python
#!/usr/bin/env python3
"""Papier caillou ciseaux"""

import random


def main():
    """point d'entrée du programme"""

    # Initialisation du générateur aléatoire avec
    # une graine constante d'une exécution à l'autre
    # pour toujours obtenir la même suite de nombres
    # aléatoires.
    random.seed(41)
    plays = ["paper", "rock", "scissors"]

    while True:

        player = input("paper, rock, scissors ?\n")
        # La fonction random.randint(a, b) renvoie un entier
        # aléatoire dans l'intervalle [a, b]
        computer = plays[random.randint(0, 2)]

        if player == computer:
            print("Égalité!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("Invalid play. Check your spelling please !")


if __name__ == "__main__":
    main()
```
</details>
