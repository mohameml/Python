#!/usr/bin/env python3
"""Papier caillou ciseaux"""

import random


def main():
    """point d'entrée du programme"""

    # START CORRECTION
    # Initialisation du générateur aléatoire avec
    # une graine constante d'une exécution à l'autre
    # pour toujours obtenir la même suite de nombres
    # aléatoires.
    random.seed(41)
    # END CORRECTION
    plays = ["paper", "rock", "scissors"]

    while True:

        player = input("paper, rock, scissors ?\n")
        # START CORRECTION
        # La fonction random.randint(a, b) renvoie un entier
        # aléatoire dans l'intervalle [a, b]
        # END CORRECTION
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
