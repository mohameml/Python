#!/usr/bin/env python3

"""
Cour sur les fonctions en python 
"""

"----------------- 1.Déf ---------------"

def add(x:int,y:int)->int :
    return x+y

print(add(1,2))


# Argument facultaif 
def f(x,y,z=1) :
    return x+y-z
print(f(1,2))
print(f(1,2,3))

"------------ 2. Varaibles globales et locales ---------------"

"""
Une variable est dite locale lorsqu'elle est créée dans une fonction. Elle n'existera
et ne sera visible que lors de l'exécution de la fonction.
"""

def nb_comm(a,b):
    c = a+b # c est locale 
    return abs(c)


"""
Une variable est dite globale lorsqu'elle est créée dans le programme principal. Elle sera visible
partout dans le programme.

"""
d = nb_comm(1,2) # d est globale


"------- visulaiser ce code en : python Tutor ---------------"
# définition des fonctions
def polynome(x):
    return (x**2 - 2*x + 1)
    
def calc_vals(debut, fin):
    liste_vals = []
    for x in range(debut, fin + 1):
        liste_vals.append(polynome(x))
    
    return liste_vals

# programme principal
print(calc_vals(-5, 5))


"--------------- 3. recusrivité -------------------------"
"""
Une fonction récursive est une fonction qui s'appelle elle-même. Les fonctions récursives
permettent d'obtenir une efficacité redoutable dans la résolution de certains algorithmes.
"""

" visulaiser ce code sur python Tutor "

def calc_factorielle(nb):
    if nb == 1:
        return 1
    else:
        return nb * calc_factorielle(nb - 1)
# prog principal
print(calc_factorielle(4))



# RQ :

"Si on veut vraiment modifier une variable globale dans une fonction, il faut utiliser le mot-clé global :"

def ma_fonction():
    global x
    return x+1

x = 1 
print(ma_fonction())

"""
RQ : Dans ce dernier cas, le mot-clé global a forcé la variable x à être globale plutôt que locale au
sein de la fonction

"""

