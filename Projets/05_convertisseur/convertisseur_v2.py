#!/usr/bin/env python3

" ceci est un convertisseur "
import svg
import sys


def tarite_points(fichier):
    "lecture et écriture de toutes les pointes  "
    
    # On ouvrir le fichier 
     
     
    with open(fichier,"r") as file_r :
        x = 0 
        y= 0 
        est_abssice = True 
        for ligne in file_r :
            
            if est_abssice : 
                x= int(ligne.replace("\n",""))
                est_abssice = False 
            else :
                y = int(ligne.replace("\n",""))
                est_abssice = True 
                print(svg.genere_cercle(svg.Point(x,y),1))
                
                
            
      
        


def main():
    "la fonction principale"
    if(len(sys.argv)!=2):
        print(f"Usage : {sys.argv[0]} nom_fichier ")
        sys.exit(1)
    print(svg.genere_balise_debut_image(640,480))
    print(svg.genere_balise_debut_groupe("black","black",1))
    tarite_points(sys.argv[1])
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())


if __name__=="__main__":
    main()


