#!/usr/bin/env python3

"""
Cour sur le tuple en python 

"""

"----------------------- 1.Déf ------------------------------"

"""
Les tuples sont des objets séquentiels (itérables, ordonnés et indexables) mais ils sont toutefois non modifiables.
,ils sont hachables sous certaines conditions .

"""

t = (1,2,3,4)
print(t)
print(type(t))
print(t[1])  
print(t[-1])
print(t[::-1]) # l'indicage comme list 

print(id(t))
t+=(2,)
print(id(t))
print("id de t est change donc : tuples sont immutables ")


"""
RQ : Pour créer un tuple d'un seul élément , utilisez 
une syntaxe avec une virgule (element,) , pour
éviter une ambiguïté avec une simple expression
"""
t = (2)
print(type(t))
t=(2,)
print(type(t))

# RQ : On peut definr un tuple sans parhéntense : 
t = 1,2,3,4
print(t)
print(type(t))

# RQ : Les opérateurs + et * fonctionnent comme pour les listes (concaténation et duplication) :
print(f"{(1,2,3)}+{(4,5)}={(1,2,3)+(4,5)}")
print(f"{(1,2)}*{2}={(1,2)*2}")

"------------ 2. La fonction : tuple -----------------------"
t = tuple([1,2,3])
print(t)

seq="chaine"
t = tuple(seq)
print(t)


# RQ : Iterations sur plusieres elem :
liste = [(i,i+1,i+2) for i in range(10)]
print(liste)

for x,y,z in liste :
    print(f"{x}->{y}->{z}->",end="")

print()

"------------- 3.Tuples contant de listes ------------"

t=([1,2],3)
print(t)
t[0].append(3)
print(t)

"RQ : "

"-------------------- 4. Hachabilité des tuples  ----------------------------"

"""
Les tuples sont hachables s'ils ne contiennent que des éléments hachables.
"""
t=(1,2,3)
print(hash(t))









