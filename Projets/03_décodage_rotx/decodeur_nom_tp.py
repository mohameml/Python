#!/usr/bin/env python3

import rotx

""" 
Ensuite, vous devrez réaliser un programme decodeur_nom_tp.py qui effectue les opérations suivantes :

    - demande à l'utilisateur de saisir un nom de fichier et crée un fichier portant ce nom dans le répertoire courant ;
    - utilise le module rotx pour décoder chacune des lettres du nom de ce TP (nirPrfne, encodé avec un décalage de 13) et 
    écrit le résultat dans le fichier créé à l'étape précédente ;
    - affiche sur la sortie standard votre prénom encodé par un décalage de 4 en utilisant un seul appel à la fonction print.
"""

# On recupere l'info de l'utilisateur

nom_fichier=input("le nom de fichier : ")
chaine="nirPrfne"
chaine_dec ="".join([rotx.rot13(e) for e in chaine])

with open(nom_fichier,"w") as fichier :
    print(chaine_dec,file=fichier)
    
# L'affichage de nom decode par declage de 4 :

print(rotx.rot(4,"N"),rotx.rot(4,"e"),rotx.rot(4,"b"),rotx.rot(4,"i"),rotx.rot(4,"l"),sep="")
    

    
  
