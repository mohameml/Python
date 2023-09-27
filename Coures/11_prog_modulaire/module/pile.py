#!/usr/bin/env python3

"""
Module pile 
"""

class Pile :

    def __init__(self, contenu ) :
        self.contenu = contenu 

    def est_vide(self):
        return len(self.contenu)==0
    
    def length(self):
        return len(self.contenu)
    
    def empiler(self , elem):
        self.contenu.append(elem)

    def dépiler(self):
        if len(self.contenu)==0 :
            raise IndexError("On ne peut pas depiler une pile vide : fou !!!!")
        return self.contenu.pop()



    def consulter(self):
        "return l'élem placé au soment de la pile "
        if self.taille()==0 :
            raise f"il y'a un errure votre pile est vide "
        
        return self.contenu[-1]
    
    def __str__(self) -> str:
        return f"{self.contenu}"
    
    def extend(self,l:list):
        for e in l :
            self.empiler(e)

        



        



        