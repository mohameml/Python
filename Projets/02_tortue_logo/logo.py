#!/usr/bin/env python3

"""
Module tortue logo.

Ce module implémente les primitives graphiques basiques
d'une tortue logo.

"""
from math import sin , cos , pi
import svg



def avance(abscisse, ordonnee, direction, crayon_en_bas, distance):
    """
    Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un Point (défini dans notre module svg).
    
    """
    
    # On definit le point qui correspond a la nouvelle position 
    # On peut trouver les corrdonnes de la nouvelle position par une formule mathématique simple 
    

        
    nouvelle_position = svg.Point(distance*cos(direction*pi/180)+abscisse, ordonnee-distance*sin(direction*pi/180)) 
    
    
    
    
    if crayon_en_bas :
        print(svg.genere_segment(svg.Point(abscisse,ordonnee),nouvelle_position))
    
    return nouvelle_position
    


def tourne_droite(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return direction-angle


def tourne_gauche(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    return direction+angle
