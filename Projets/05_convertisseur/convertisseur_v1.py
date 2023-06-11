#!/usr/bin/env python3

" convertisseur  v1 "
import svg



def conevrtissur_v1():
    
    " fonction de conversion "
 
    for _ in range(1000):
        x = input()
        y = input()
        print(svg.genere_cercle(svg.Point(int(x),int(y)),1))

        
    
def main():
    " fonction principale "
    
    print(svg.genere_balise_debut_image(640,480))
    print(svg.genere_balise_debut_groupe("black", "white", 2))
    conevrtissur_v1()
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image()) 
    
main()
