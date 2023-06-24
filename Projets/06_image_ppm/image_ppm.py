#!/usr/bin/env python3

""" 
ceci est un projet pour apprendr le format ppm 
I. Premire pas : Dans un peremier tas On tarvaille sur exeple simple 
II . Constrcution de lignes 
III. Coonstrcution des figures  

"""

import random
import sys 


def est_dans_disque(x,y,centre_x,centre_y, r):
    "cette fonction return est ce que Point(x,y) est dans C(c,r)"
    
    
    
    return (x-centre_x)**2 + (y-centre_y)**2 < r**2 


def premires_pas():
    
    
    # On demande à l'utilisateur de donner les dimensions de l'image 
    
    print("Entrez la largeur de l'image : ", file = sys.stderr , end="")
    largeur = int(input())
    print("Entrez la hauteur  de l'image : ", file = sys.stderr , end="")
    hauteur = int(input())
    
    # On génere l'image au format ppm
    print("P2")
    print(f'{largeur} {hauteur}')
    print("255")
    
    # On tire les coordonnées de deux disques :
    
    # 1ere cercle :
    
    x1 = random.randint(largeur*0.3,largeur*0.5)
    y1 = random.randint(hauteur*0.3,hauteur*0.5)
    taille_possible_1 = min(x1,largeur-x1,hauteur, hauteur-y1)
    r1 = random.randint(0,taille_possible_1)

    # 2 éme Cercle :
    
    x2 = random.randint(largeur*0.3,largeur*0.5)
    y2 = random.randint(hauteur*0.3,hauteur*0.5)
    taille_possible_2 = min(x2,largeur-x2,hauteur, hauteur-y2)
    r2 = random.randint(0,taille_possible_2)

    
    # Tracage des deux disque 
    
    for x in range(largeur):
        for y in range(hauteur) :
            
            if est_dans_disque(x,y,x1,y1,r1) or est_dans_disque(x,y,x2,y2,r2):
                print(str(random.randint(0,255)))
            else :
                print("255")
    
    
    
premires_pas()