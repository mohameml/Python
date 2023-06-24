#!/usr/bin/env python3

" module de géneration des images au format : ppm "

import random

from collections import namedtuple



def genere_en_tete(largeur, hauteur):
    "cette fonction écrit l'entete de l'image ppm"
    print("P2")
    print(f"{largeur} {hauteur}")
    print("255")
    



def genere_cercle(centre , rayon, hauteur , largeur):
    "cette fonction génere une cercle : C(c,r) "
    
    for x in range(largeur ): 
        for y in range(hauteur) : 
            if est_dans_disque(x,y,centre.x,centre.y,rayon):
                print(str(random.randint(0,255)))
            else :
                print("255")


         
def genere_background(couleur_image :str , largeur , hauteur ):
    "donne une backgrounde de l'image ppm"
    
    for _ in range(largeur):
        for _  in range(hauteur):
            print(couleur(couleur_image))

    
    

def genere_segement(dep,arr ,largeur , hauteur ):
    " cette fonction génere un segement entre due Points : dep et arr "
    
    dx = dep.x - arr.x
    dy = dep.y - arr.y 
    D = 2*dy - dx 
    y = dep.y
    for x in range(dep.x,arr.x):
        pixel(x,y,largeur,hauteur,arr,dep)
        if D < 0 :
            D+=2*dy 
        else :
            y+=1 
            D+=2*(dy-dx) 

        

            
                
    
            






    


#------------------------ Etap2 du Module : fonctions supplémentaires

Point = namedtuple("Point","x y")

def est_dans_disque(x,y,centre_x,centre_y, r):
    "cette fonction return est ce que Point(x,y) est dans C(c,r)"

    return (x-centre_x)**2 + (y-centre_y)**2 < r**2 



def couleur(couleur):
    " fonction qui return le couleur "
    
    dict_couleur = {"blanc": "255", "noir": "0", "red": "255 0 0"}
    
    
    return dict_couleur[couleur]


def pixel(x,y_reel, largeur , hauteur ,arr, dep ):
    "écrit dans la position x et y "
    for x in range(largeur) :
        for y in range(hauteur) :
            if x in [dep.x+i for i in range(arr.x-dep.x)]:
                if y == y_reel :
                    print(str(random.randint(0,255)))