#!/usr/bin/env python3
import svg
TAILLE_CASE=40

DROITE=0
HAUT=1
GAUCHE=2

def dessine_case(abscisse,ordonnee,numero_case):
    sommet1 = svg.Point(abscisse, ordonnee)  # En bas à gauche
    sommet2 = svg.Point(abscisse, ordonnee - TAILLE_CASE)  # En haut à gauche
    sommet3 = svg.Point(abscisse + TAILLE_CASE, ordonnee - TAILLE_CASE)
    sommet4 = svg.Point(abscisse + TAILLE_CASE, ordonnee)  # En bas à droite

    # Affichage du rectangle
    print(svg.genere_balise_debut_groupe("black", "none", 1))
    points=(sommet1,sommet2,sommet3,sommet4)
    print(svg.genere_polygone(points),"\n")
    print(svg.genere_balise_fin_groupe())

    # Affichage du texte
    print(svg.genere_balise_debut_groupe("none", "red", 0))
    print( svg.genere_texte(abscisse + 2,ordonnee - 2,TAILLE_CASE / (3 if numero_case != 41 else 1.5),str(numero_case))+"\n")
    print(svg.genere_balise_fin_groupe())
def genere_ligne(abscisse_case,ordonnee_case,nombre_de_case,direction,numero_1_case):
    "deesine une ligne  des cases dans une direction doone "
    abscisse=abscisse_case
    ordonnee=ordonnee_case
    mouvements=((+TAILLE_CASE,0),(0,-TAILLE_CASE),(-TAILLE_CASE,0))
    for numero in range(numero_1_case,numero_1_case+nombre_de_case):
         dessine_case(abscisse,ordonnee,numero)
         abscisse+=mouvements[direction][0]
         ordonnee+=mouvements[direction][1]

def dessine_lignes(hauteur,nombre_lignes,directions,nb_cases):
    "fonction qui dessine toutes les lignes"
    abscisse_courante=0
    ordonnee_courante=hauteur
    numero_case_courante=1
    mouvements=((+TAILLE_CASE*(nb_cases[0]-1),-TAILLE_CASE),(0,-TAILLE_CASE*nb_cases[1]),(-TAILLE_CASE*(nb_cases[2]-1),-TAILLE_CASE))






    
    for ligne in range(nombre_lignes):
        direction=directions[ligne%len(directions)]
        nombre_case_ligne=nb_cases[ligne%len(nb_cases)]
       
        genere_ligne(abscisse_courante,ordonnee_courante,nombre_case_ligne,direction,numero_case_courante)
        abscisse_courante+=mouvements[direction][0]
        ordonnee_courante+=mouvements[direction][1]
        numero_case_courante+=nombre_case_ligne

def generation_plateau(largeur,hauteur):

    nb_cases_ligne=largeur//TAILLE_CASE
    nb_lignes=hauteur//TAILLE_CASE
    if not nb_lignes % 2:
        nb_lignes -= 1



    print(svg.genere_balise_debut_image(largeur,hauteur))
    print(svg.genere_rect(largeur,hauteur,"lightgray",0,0))


    
    directions=[DROITE,HAUT,GAUCHE,HAUT]
    nb_cases=[nb_cases_ligne,1,nb_cases_ligne,1]

    dessine_lignes(hauteur,nb_lignes,directions,nb_cases)

    print(svg.genere_balise_fin_image())

generation_plateau(800,600)





        

        







    



