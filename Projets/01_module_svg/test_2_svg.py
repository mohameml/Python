#!/usr/bin/env python3

"il s'agit d'un autre test de la module svg "
from collections import namedtuple
import svg
import sys 

Point = namedtuple("Point","x y")

if len(sys.argv)!=3 :
    print(f'l\'usage de cette test est : {sys.argv[0]} largeur hauteur ')
    exit(1)






def test_rect(largeur , hauteur):
    
    top_left = Point(0.25*largeur,0.25*hauteur)
    
    print(svg.genere_balise_debut_groupe("green","green","3"))
    print(svg.genere_rectangle(top_left,0.5*largeur,0.5*hauteur))
    print(svg.genere_balise_fin_groupe())
    

def test_segment(dep , arr) :
    
    print(svg.genere_balise_debut_groupe("red","red","3"))
    print(svg.genere_segment(dep,arr))
    print(svg.genere_balise_fin_groupe())

def test_polygone(points):
    
    print(svg.genere_balise_debut_groupe("yellow","None","2"))
    print(svg.genere_polygone(points))
    print(svg.genere_balise_fin_groupe())

def test_2_svg() :
    
    largeur = int(sys.argv[1])
    hauteur = int(sys.argv[2])
    
    print(svg.genere_balise_debut_image(largeur,hauteur))
    
    # On test la tracage de rectangle : 
    test_rect(largeur,hauteur)
    
    # On test la tracage de segment :
    # test_segment(Point(0,0),Point(largeur,hauteur))
    # test_segment(Point(0,hauteur),Point(largeur,0))
    
    # On test la tracage d'un polygone : triangle
    test_polygone([Point(0,0),Point(largeur,0),Point(largeur/2,hauteur)])
    test_polygone([Point(0,hauteur),Point(largeur,hauteur),Point(largeur/2,0)])
    test_polygone([Point(largeur,0),Point(largeur,hauteur),Point(0,hauteur/2)])
    test_polygone([Point(0,0),Point(0,hauteur),Point(largeur ,hauteur/2)])
    
    # On test l'ecriture de texte : 
    print(svg.genere_balise_debut_groupe_transp(0.3))
    print(svg.genere_texte(largeur/2-largeur/20,hauteur/2,"svg",5))
    print(svg.genere_balise_fin_groupe())
    
    
    
    print(svg.genere_balise_fin_image())
    
    
if __name__=="__main__":
    
    test_2_svg()
    
    
    
    
    
    