#!/usr/bin/env python3

from copy import deepcopy

"""
cour liste en python 
"""

"--------------- 1.Déf -------------------"

"""
* liste est une structure de données qui contient une série des valeures.
* Python autorise la construction de liste contient des valeures de type #ts.
"""

print("------------- affichage -------------------")

l = [1,2,"sidi",1.02, 'A'] 
print(l) # on peut afficher le contenu d'une liste grace à print()

# afficher les élements un par un 
for e in l :
    print(e)


for i in range(len(l)):
    print(l[i])


"------------------ 2.opérations ------------------------"

# Addition :

l1  = [1,2,3,4]
l2 = [5,6]
l_add = l1+l2
print("----------- addition ------------")
print(f"{l1}+{l2}={l_add}")
print()

# multiplication 
print("------------ Mult par un fateur ------------------")
facteur = 2

# On remarque que la mult d'une liste par un facteur :duplice la liste facteur fois 
print(f"{l1}*{facteur}={l1*facteur}")


"------------------------------ 3 . Indicage d'une liste -------------------"
print("-------------- Indicage ----------------------------")

"""
l = [1 ,2 ,3 ,4 ,5]
i :  0  1  2  3  4 
i_n : -5 -4 -3 -2 -1 
"""

l = [1,2,3,4,5,6]

print(f"l'élemnt d'indice -1 de {l} est : {l[-1]}")
print()

"---------------------------------- 4.Traches -----------------------------------"
print("-------------- Tranche ----------------------")

"""
Un autre avantage des listes est la possibilité de sélectionner une partie d'une liste en utilisant
un indiçage construit sur le modèle [m:n+1] pour récupérer tous les éléments, du émième au
énième (de l'élément m inclus à l'élément n+1 exclu), 
On dit alors qu'on récupère une tranche de la liste.

"""


animaux = ["girafe", "tigre", "singe", "souris"]

print(f"animaux = {animaux}")
print(f"la tranche [0:2] de animaux est :  {animaux[0:2]}")
print(f"la tranche [0:2] de animaux est :  {animaux[0:3]}")
print(f"la tranche [0:2] de animaux est :  {animaux[0:]}")
print(f"la tranche [0:2] de animaux est :  {animaux[:]}")
print(f"la tranche [0:2] de animaux est :  {animaux[1:]}")
print(f"la tranche [0:2] de animaux est :  {animaux[1:-1]}")



"""
RQ :
Notez que lorsqu'aucun indice n'est indiqué à gauche ou à droite du symbole deux-points,
Python prend par défaut tous les éléments depuis le début ou tous les éléments jusqu'à la fin
respectivement.

"""

"""
On peut aussi préciser le pas en ajoutant un symbole deux-points supplémentaire et en
indiquant le pas par un entier.

Finalement, on se rend compte que l'accès au contenu d'une liste fonctionne sur le modèle
liste[début:fin:pas] .
"""
print()
print()
print("Tranche avce pas : ")
x = list(range(10))

print(x)
print(x[::2]) # avec pas = 2
print(x[0:-1:2])


"--------------------- 5. qq focntionss "

"""
len : len(l) # pour mesurer la taille d'une liste 
sum : sum(l) # calcule la somme des élemes d'une liste 
max , min : return min , max d'une liste 

"""

print(f"La Somme de la liste [0.....100] est : {sum([i for i in range(101)])}")
print("\n")


"------------------ 6 . Méthodes associées aux listes ------------"
print("-------------- 6 . Méthodes associées aux listes ----------")


# 6.1 le Méthode .append()
print("6.1 le Méthode .append()")
a =[1,2,3]
print(a)

a.append(4) # ajouter 4 a la fin de a
print(a)


# 6.2 La Méthode insert(indice , élem)
print("6.2 La Méthode insert(indice , élem)")
a = [1,2,3]
print(a)
a.insert(0,10)
print(a)

# 6.3 L'instruction del
print("6.3 L'instruction del")
a = [1,2,3]
print(a)
del a[1]
print(a)


# 6.4 la Méthode .remove()
print("6.4 la Méthode .remove()")
" La méthode .remove() supprime un élément d'une liste à partir de sa valeur : (1 ere Occurence )"

a = [1,2,3,4,3]
print(a)
a.remove(3)
print(a)

# 6.5 La Méthode .sort()
print("6.5 La Méthode .sort()")

"La méthode .sort() trie les éléments d'une liste du plus petit au plus grand:"

a = [6,4,2,1,0,2,3,10]
print(a)
a.sort()
print(a)    

"L'argument reverse=True spécifie le tri inverse, c'est-à-dire du plus grand au plus petit élément"
a.sort(reverse=True)
print(a)


#6.6  La fonctino : sorted
print("6.6  La fonctino : sorted")
"""
La fonction sorted() trie également une liste. Contrairement à la méthode précédente
.sort() , cette fonction renvoie la liste triée et ne modifie pas la liste initiale .

"""

a = [6,4,2,1,0,2,3,10]
print(a)
b = sorted(a)
print(b)    

"L'argument reverse=True spécifie le tri inverse, c'est-à-dire du plus grand au plus petit élément"
c = sorted(a, reverse=True)
print(c)



#6.7 Le Méthode reverse()
print("6.7 La Méthode reverse()")

a = [3,2,1,4,5]
print(a)
a.reverse()
print(a)


#6.8 la Méthode() .count() :

"""
La méthode .count() compte le nombre d'éléments (passés en argument) dans une liste :
"""

a = [1,2,1,2,3,4,1]

print(f"l'élement 1 existe dans {a} : {a.count(1)} fois ")

"----------------------- 8. Test d'appertaance ----------------------"

"""
L'opérateur in teste si un élément fait partie d'une liste.
La variation avec not permet, a contrario, de vérifier qu'un élément n'est pas dans une liste.
"""

print("---------- Test d'appertanace ---------------------")
a = [1 , 2 ,3 ,6 ,7, 9 ]

print(f"l'élemnt {1} est dans {a} : {1 in a}")
print(f"l'élement {2} n'est pas dans {a} : {2 not in a}")

"------------------ 9. Copy d'une liste -----------------"
print("------------------------ 9. Copy d'une list --------------------")
a = [1,2,3,4,5]
b = a # e l'affectation d'une liste créeen réalité une référence et non une copie .
a[0] = -1 
print(a)
print(b)

c =a[:] # une copie de a dans c 
d = list(a) # une copie de a dans c 
e = deepcopy(a) # une copie de a dans c : qui marche tjr.


"---------------- 10. liste de comprehension ----------------"

print("---------------- 10. liste de comprehension ----------------")
"""
En Python, la notion de liste de compréhension (ou compréhension de listes) représente une
manière originale et très puissante de générer des listes. La syntaxe de base consiste au moins
en une boucle for au sein de crochets précédés d'une variable (qui peut être la variable
d'itération ou pas ):
   [i for i in l if ... else ..]

"""

# exemple1 
l = [2*i for i in range(10)]
print(l)
# exemple 2 

l = [i for i in range(10) if i%2==0 ]
print(l)

