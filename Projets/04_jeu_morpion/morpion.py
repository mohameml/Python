#!/usr/bin/env python3

"""Un jeu de morpion"""


# Les différents types de joueurs sont représentés par des modules.
# Les modules joueur_humain et joueur_ordi doivent être réalisés.
# Le module joueur_ordi_malin est fourni.
# Le module joueur_humain demande simplement à l'utilisateur de jouer.
# Le module joueur_ordi joue automatiquement. Sa stratégie n'est pas spécifiée.
import joueur_humain
import joueur_ordi
import joueur_ordi_malin



def recupere_chaine_a_afficher(symbole):
    """
    Renvoie la chaîne de caractère à afficher pour le symbole donné.

    Pour le symbole "x", le caractère unicode "MULTIPLICATION X", affiché
    en rouge doit être utilisé.
    Pour le symbole "o", le caractère unicode "WHITE CIRCLE", affiché
    en bleu doit être utilisé.

    précondition : symbole est soit "x" soit "o"
    """
    if symbole!="x" and symbole!="X" and symbole!="O" and symbole!="o":
        return symbole

    else :
        if symbole=="x" or symbole=="X" :
            return "\033[91mX\033[0m"
        else :
            return "\033[34m\u2B24\033[0m"  
        


def affiche_plateau(cases):
    """
    Affiche le plateau représenté par le tuples cases à 9 éléments.

    L'affichage se fait sur la sortie standard uniquement en utilisant
    des appels à la fonction print.

    précondition : chacune des cases contient soit
      - la chaîne de caractères "x" (case occupée par le joueur 1)
      - la chaîne de caractères "o" (case occupée par le joueur 2)
      - la chaîne de caractères "i" avec i entier correspondant au
        numéro de la case (case libre)
    précondition : cases est une liste de 9 éléments
    """
    if len(cases)!=9 :
        print("cases non vaalide")
        exit(1)
    valide = 0
    liste_valide = ["X","x","o","O", "0","1","2","3","4","5","6","7","8"]
    
    
    for e in cases :
        if e in liste_valide :
            valide+=1

            
    if valide==len(cases):
        
        
        
        print(f' {recupere_chaine_a_afficher(cases[0])} | {recupere_chaine_a_afficher(cases[1])} | {recupere_chaine_a_afficher(cases[2])} ')
        print(' --|---|---')
        print(f' {recupere_chaine_a_afficher(cases[3])} | {recupere_chaine_a_afficher(cases[4])} | {recupere_chaine_a_afficher(cases[5])} ')
        print(' --|---|---')
        print(f' {recupere_chaine_a_afficher(cases[6])} | {recupere_chaine_a_afficher(cases[7])} | {recupere_chaine_a_afficher(cases[8])} ') 
        print()
        print()
        
    else :
        print("le contenue de cases n'est pas valide")
        exit(1)       
        


def valide_win(cases):
    "return true si il y'a un joueur gagnante "
    
    
    if cases[0]==cases[1]==cases[2]:
        return True
    elif cases[3]==cases[4]==cases[5] :
        return True 
    elif cases[6]==cases[7]==cases[8]:
        return True 
    elif cases[0]==cases[3]==cases[6]:
        return True
    elif cases[1]==cases[4]==cases[7]:
        return True 
    elif cases[2]==cases[5]==cases[8]:
        return True 
    elif cases[0]==cases[4]==cases[8]:
        return True 
    elif cases[2]==cases[4]==cases[6]:
        return True 
    
    return False 
    
    

def valide_choix_joueur(choix_joueur,cases_occupe):

    # validation de choix du joueur :
    
    if cases_occupe[choix_joueur]=="inoccupée":
        return 1 
    else :
        print("votre choix n'est pas valide")
        return 0 
    
        
    
    
    


def joue_coup(joueur, joueur_num, cases, symbole):
    """
    Joue un coup.

    Cette fonction effectue les opérations suivantes tout en affichant
    ce qu'il se passe sur la sortie standard :
      - affiche le plateau représenté par cases
      - utilise le module joueur pour savoir quel coup doit être joué
      - met à jour le plateau de jeu avec ce coup
      - affiche le plateau et le numéro du joueur gagnant si c'est gagné
        puis quitte le programme
      - renvoie le nouveau plateau

    précondition : joueur est un module avec une fonction
                   joue_coup(cases, symbole) qui renvoie le
                   numéro d'une case précédemment inoccupée.
    précondition : joueur_num est soit l'entier 1 soit l'entier 2
    précondition : cases est une list de 9 éléments
    précondition : symbole est soit "x" soit "o"

    """
    
    
    cases_occupe = {e :"inoccupée" for e in range(9) }
    liste_valide_occupe = ["x","X","o","O"]
    
    for indice, e in enumerate(cases) :
         
        if e in liste_valide_occupe :
            cases_occupe[indice]="occupée"
    #  On récupere le chox de la joueur :
    
    choix_joueur=joueur.joue_coup(cases,symbole)
    
    while valide_choix_joueur(choix_joueur, cases_occupe)!=1:
        choix_joueur=joueur.joue_coup(cases,symbole)
    
    
    
        
        
    # le choix de joueur est valide 
    cases[choix_joueur]=symbole
    print(f'le choix de joueur {joueur_num} est : {choix_joueur}')
    
    affiche_plateau(cases)
    
        
    if valide_win(cases):
        print(f"Bravo le joueur {joueur_num} est gangé ")
        # Apres le jeux est termine 
        exit(1)
    else :
        return cases 
    
    
        
            
        
        
            
            
    
    
    
    
    
    
    




def joue_partie():
    """Joue une partie complète de morpion"""

    # Initialisation des deux joueurs en demandant à l'utilisateur
    # Parenthèses nécessaires pour "spliter un string literal"
    message_choix_joueur = (
        "Veuillez choisir le type du joueur {} en tapant\n"
        "  0 pour humain\n"
        "  1 pour un ordinateur\n"
        "  2 pour un ordinateur très malin\n"
        "  entrez votre choix : "
    )

    print(message_choix_joueur.format(1), end="")
    type1 = int(input())
    print(message_choix_joueur.format(2), end="")
    type2 = int(input())
    joueur1 = (
        joueur_humain
        if type1 == 0
        else (joueur_ordi if type1 == 1 else joueur_ordi_malin)
    )
    joueur2 = (
        joueur_humain
        if type2 == 0
        else (joueur_ordi if type2 == 1 else joueur_ordi_malin)
    )
    print()

    # Initialisation et affichage du plateau vide
    # Une case vide est représentée par son numéro,
    # utilisé par le joueur humain pour indiquer
    # quelle case il joue.
    cases = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    affiche_plateau(cases)
    # Joue 9 coups au maximum
    print("----------Tour 1 ---------")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    
    print("----------Tour 2 ---------")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    
    print("----------Tour 3 ---------")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    
    print("----------Tour 4 ---------")
    joue_coup(joueur1, 1, cases, "x")
    joue_coup(joueur2, 2, cases, "o")
    
    print("----------Tour 5 ---------")
    joue_coup(joueur1, 1, cases, "x")

    # Si on arrive là, il y a égalité
    print("Match nul !")


if __name__ == "__main__":
    joue_partie()
