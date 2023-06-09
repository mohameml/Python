
import random

# START CORRECTION
def joue_coup(cases, symbole):
    """Joue la première case libre."""
    
    # On recupere tout d'abord les cases valides :
    cases_valides = []
    
    cases_occupe = {e :"inoccupée" for e in range(9) }
    liste_valide_occupe = ["x","X","o","O"]
    
    for indice, e in enumerate(cases) :
         
        if e in liste_valide_occupe :
            cases_occupe[indice]="occupée"
        else :
            cases_valides.append(indice)
            
    return random.choice(cases_valides)



# END CORRECTION
