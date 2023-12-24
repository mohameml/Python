#!/usr/bin/env python3
"""
calculer les tailles de tous les composants connectés.
trier et afficher.
"""

from timeit import timeit
from sys import argv

from geo.point import Point






def load_instance(filename):
    """
    charge le fichier .pts.
     renvoie la limite de distance et les points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points





def comm_connexe(sommet,points,distance):
    
    col={s:"blanc" for s in points}
    col[sommet]="gris"
    pile=[sommet]
    
    
    while pile :
        
        # on prend la  tete de la pile
        u=pile[-1]
        # on cherche les enfants non parcouris 
        R=[y for y in points if col[y]=="blanc"  and  u.distance_to(y) < distance ]
        
        if R :
             v=R[0] # on prend le premiere sommet de R 
             col[v]="gris" # on le marque comme visite 
             pile.append(v) # on l'empile v dans la pile 
        
        else :
            pile.pop()

            
    return  [s for s in points if col[s]=="gris"]      
    


def print_components_sizes( distance, vocabulaire):
    
    " affichage des tailles triees de chaque composante "

    
    # Les composantes connexes :
    tailles=[]

    
    col={v:"blanc" for v in vocabulaire}
    for point in vocabulaire :

        if col[point]!="noir" :
            com=comm_connexe(point,vocabulaire,distance)
            tailles.append(len(com))
          
        for s in com :
            col[s]="noir"

    # affichage final
    tailles.sort(reverse=True)
    print(tailles)
                
                    





            

def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)



main()


    

