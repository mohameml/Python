#!/usr/bin/env python3
"""
ceci est une intoduction de la module pygamee pour creér de jeux 2D en python
"""

"""
tout d'abord pour creér de jeux en python il falloir toujrs 5 étapes necessaires :
1. Initialisation de pygame
2. Appel des modules nécessaires
3. L'affichage
4. Boucle infinie
5. Fermeture du programme


"""

# 1.Initialisation de pygame
from pygame.locals import *
import pygame
pygame.init()


fenetre = pygame.display.set_mode((200, 200))
