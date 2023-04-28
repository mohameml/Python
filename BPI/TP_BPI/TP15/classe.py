#!/usr/bin/env python3

"""Un exemple de classe : cellule"""

class Cellule :
    

    def __init__(self, valeur, suivant):
        self.valeur= valeur
        self.suivant = suivant 

    def __str__(self):
        return 'cellule_(' + str(self.valeur) + ',' + str(self.suivant) + ')'

def main():
    """Test de notre classe Point"""

    # Création de deux cellules 
    cellule2 =Cellule(5, None)
    cellule1=Cellule(1, cellule2)
    

    # Affichage de la somme des valeures 
    
    somme1 = cellule1.valeur + cellule2.valeur
    print("Somme de valeures de",cellule1 , "et de la valeur2 de", cellule2, "=", somme1)

    # Les Cellules  sont modifiables.
    cellule1.valeur = 3
    somme1 = cellule1.valeur + cellule2.valeur
    print("Somme de valeures de",cellule1 , "et de la valeur2 de", cellule2, "=", somme1)

if __name__ == "__main__":
    main()
