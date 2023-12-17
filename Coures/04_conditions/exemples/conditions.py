#!/usr/bin/en python3 

""" 
cour 04 : les conditions 
"""


# ------------- 1.  l'instrcution if ------------- 


x = 2

if x==2 :
    print(" Test valide ")
 
# ------------- 2.  l'instrcution else  ------------- 


x = 3

if x==2 :
    print(" Test valide ")
else :
    print("Test échoue ")


# ------------- 3.  l'instrcution elif  ------------- 

# On peut utiliser une série de tests dans la même instruction if , notamment pour tester
# plusieurs valeurs d'une même variable

x = 4

if x==2 :
    print(" Test valide x= 2 ")
elif x==3 :
    print("Test valide x=3")
elif x==4 :
    print("Test valide x=4")
elif x==5 :
    print("Test valide x=5")
else :
    print("Test échoue ")


# ------------- 4. Tests multiples   ------------- 

# ou : or  && ET : and 

y = int(input("valeur de y : "))
z = int(input("valeur de z : "))
e = y==z 

if e or y < z  : 
    print("Test valide ")
else :
    print(" Test échoue ")

# -------------- 5 . les instructtions : break && continue ----------- 


# L'instruction break stoppe la boucle.

print("------- Test break ----------")
for i in range(10):
    if i == 2 :
        break 
    print(i)

# L'instruction continue saute à l'itération suivante, sans exécuter la suite du bloc d'instructions
# de la boucle

print("------- Test continue  ----------")
for i in range(10):
    if i == 2 :
        continue
    print(i)


# ----------------- 6. Tests de valeur sur des floats -------------------


# bool1 = True 
bool1 = 0.3 == 0.3 
print(f" bool1 = {bool1} ")


# bool2 = False 
bool2 = (3 - 2.7) == 0.3 
print(f" bool2 = {bool2} ")

print(f" la valeur de 3 - 2.7 = {3-2.7}")


# La bonne pratique est :  de vérifier si un float est compris dans un intervalle avec
# une certaine précision. 

# Exemple :
précision = 0.0001
var = 3.0 - 2.7
bool3 = 0.3 - précision < var < 0.3 + précision
print(f"bool3 = {bool3}")

bool4 =  abs(var - 0.3) < précision
print(f"bool4 = {bool4}")

