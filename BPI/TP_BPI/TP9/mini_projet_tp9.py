#!/usr/bin/env python3
import sys 
fichier=sys.argv[1]

fichier=open(fichier,"r")

# Différents types de suites
STATIONNAIRE = 0
CROISSANTE = 1
DECROISSANTE = -1

def traite_nombre(suite, type_suite, nombre):
    """Traite le nombre donné vis à vis de la suite donnée.

    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite a changé
    de sens.
    """
    n=len(suite)-1
    if suite==[]:
        return (True,STATIONNAIRE)
    
    if nombre>suite[n]:
        if type_suite==STATIONNAIRE or type_suite==CROISSANTE:
            return (True,CROISSANTE)
        if type_suite==DECROISSANTE:
            return (False,CROISSANTE)
    if nombre<suite[n]:
        if type_suite==STATIONNAIRE or type_suite==DECROISSANTE:
            return (True,DECROISSANTE)
        if type_suite==CROISSANTE :
            return (False,DECROISSANTE)
    if nombre==suite[n]:
        return (True,STATIONNAIRE)

ligne=fichier.readline()
suite=[]
finale=[]
type_suite=STATIONNAIRE
avant=[]

while ligne:
    ligne=ligne.split(" ")
    for i in range(len(ligne)):
        ligne[i]=int(ligne[i])
    for nombre in ligne:
        info=traite_nombre(suite,type_suite,nombre)
        if info[0]:
            suite.append(nombre)
            type_suite=info[1]

        else:
            if len(suite)>=len(finale):
                finale=suite
            suite=avant+[nombre]
            type_suite=info[1]
        avant=[nombre]
    
    ligne=fichier.readline()
print(finale)

fichier.close()
    


    



