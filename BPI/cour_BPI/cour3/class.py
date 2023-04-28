#!/usr/bin/env python3




class Voiture:


    def __init__(self,couleur,marqure,p_vitesse):
        self.couleur=couleur
        self.marque=marqure
        self.vitesse=p_vitesse
    
    def acceleration(self,p_vitesse):
        self.vitesse+=p_vitesse
    def frainer(self,p_vitesse):
        self.vitesse-=p_vitesse
        if self.vitesse < 0:
            self.vitesse  =0
    def __str__(self):
       str_repr = (f'Voiture :\n'
       f' couleur = {self.couleur }\n'
       f' marque = {self.marque}\n'
       f' vitesse = {self.vitesse}')
       return str_repr



voiture1=Voiture("blue","mar",100)

voiture2=Voiture("black","BMW",120)


