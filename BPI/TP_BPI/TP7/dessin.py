import random
import svg
def couleur_aleatoire():
    couleur=("grren","orange","blue","red","yellow","brown","purple","grey","lime")
    return random.choice(couleur)

def affiche_triangle(triangle_tourne, couleur):

    niveau_opacite=random.random()
    print(svg.genere_balise_debut_groupe_transp(niveau_opacite),f'<polygon points="{triangle_tourne}"  fille="{couleur}"/>',svg.genere_balise_fin_groupe())



