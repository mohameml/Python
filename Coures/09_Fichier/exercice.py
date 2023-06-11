#!/usr/bin/env python3
""" 
Exercice spirale :
* Objcetif : visualiser un spirale avec python 
"""
import math
import matplotlib.pyplot as plt 


def cord_cercle(rayon, angle):
    """ 
    cette fonction calcule les coordonnées cartésiennes d'un point
    sur un cercle .
    
    """
    
    return (rayon*(math.cos(angle)),rayon*(math.sin(angle)))


def cord_spirale(fichier):
    """ 
    * calucle les coordonnées cartésiennes qui decrivent la spirale 
        - On varie l'angle : angle entre [0,4pi]
        -  a chaque tour On incrémente le rayon par 0.1 (rayon_init = 0.5 )
    
    """
    r = 0.5
    angle = 0

    while angle < 10*math.pi:
        point = cord_cercle(r,angle)
        print(f'{point[0]} {point[1]}', file=fichier)
        r+=0.1
        angle+=0.1
        

def affichage(fichier):
    "l'affichage de spirale "
    
    # On initialis ele duex liste 
    x=[]
    y=[]
    
    with open(fichier,"r") as file_r :
        for ligne in file_r : 
            point = ligne.replace("\n","")
            point = point.split(" ")
            x.append(float(point[0]))
            y.append(float(point[1]))
            
    plt.figure(figsize=(8,8))
    mini=min(x+y)*1.2
    maxi=max(x+y)*1.2
    plt.xlim(mini,maxi)
    plt.ylim(mini,maxi)
    plt.plot(x,y)
    plt.savefig("spirale.png")
    
                
    
def main():
    " fonction principale "
    
    with open("spirale.dot","w") as file_w :
        cord_spirale(file_w)
        
    # l'affichage 
    affichage("spirale.dot")
    
    
    
if __name__=="__main__":
    main()