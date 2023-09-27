#!/usr/bin/env python3



"------------------------------ II. Les dictionnaires -----------------------------------------"

print("--------------------------- Les dictionnaires ---------------------------------------")
"""

1.Déf :

Les dictionnaires sont des collections non ordonnées d'objets (ceci
est vrai jusqu'à la version 3.6 de Python, voir remarque ci-dessous). Il ne s'agit pas d'objets séquentiels
comme les listes ou chaînes de caractères, mais plutôt d'objets dits de correspondance (mapping objects en
anglais) ou tableaux associatifs
"""

d = {}
d["sidi"] = 1
d["Ahmedou"] = 2
d["khaled"] = 3
print(d)

for cle in d :
    print(f"{cle}->{d[cle]}")

"""
RQ :

Une règle est toutefois requise, les objets utilisés comme clé doivent être hachables .


"""

"---------------------  2. Les Méthodes : .keys() , .values() et .items() -------------------"

print(d.keys()) # la méthode keys renvoie les cles de la dict d .
print(d.values()) # la méthode .values() renvoie les valeures de la dict d 

for cle in d.keys() :
    print(cle)

for val in d.values():
    print(val)

"""
RQ : les structures renvoient par les Méthodes .keys() && .values() sont des structures partuciles non indexable mais iterables . 

"""

print(d.items()) # La Méthodes return un Objet iterable (cle , val)

"------------------ 3. Test d'appertanace -------------------------------"

"""
Pour vérifier si une clé existe dans un dictionnaire, on peut utiliser le test d'appartenance avec l'opérateur in
qui renvoie un booléen .
"""
print(f"'sidi' dans d  :{'sidi' in d}")
print("doudou" in d) # Test d'appertance de cle "doudou" in 


# RQ :
print(1 in d.values()) # si on veut tester une val dans l'ensemble de val de d.


"-------------- 4. La Méthode .get() -------------------"

"""
Par défaut, si on demande la valeur associée à une clé qui n'existe pas, Python renvoie une erreur :(KeyError)
La méthode .get() s'affranchit de ce problème. Elle extrait la valeur associée à une clé mais ne renvoie pas
d'erreur si la clé n'existe pas .
Syntaxe : dict.get("cle") --> return la valeur associe à la cle.

"""
d = {"n1":1,"n2":2}
print(d.get("n1"))
print(d.get("n4"))
"RQ: On peut également indiquer à .get() une valeur par défaut si la clé n'existe pas :"
print(d.get("n3",3))
print(d)

"--------------- 5. Tri d'un dict -----------------------"

"------------ 5.1 tri par cles -------------------"

d = {"sidi":1 , "khaled":2}
d_tri = sorted(d) # return la liste de clées tries en ordre croissant 
print(d_tri)

"------------ 5.2 tri par valeures ------------------"

print(sorted(d,key=d.get)) # return la liste des clées tri par ordre croissant des valeures 

"RQ1 : L'argument key=dico.get indique  qu'il faut réaliser le tri par les valeurs du dictionnaire."

"RQ2 : L'argument reverse=True fonctionne également pour l'ordre decroissante"
print(sorted(d,key=d.get,reverse=True))


"------------ 6.Clé associée au minimum ou au maximum des valeurs  -------------"

"les fonctions max et min acceptent l'argument , key="
print(max(d,key=d.get)) # return la clé associe a la valeur max 

print(min(d,key=d.get)) # return la clé associe a la valeur min 

"""
RQ : 
En créant une liste de dictionnaires qui possèdent les mêmes clés, on obtient une structure qui ressemble à
une base de données :
BD = [
{"nom": "sidi","age":18 , "Numero":0001} ,
{"nom": "sidi","age":18 , "Numero":0001} , 
{"nom": "sidi","age":18 , "Numero":0001} , 
{"nom": "sidi","age":18 , "Numero":0001} , 
]
"""

"--------------- 7. La fonction l: dict -------------------"

ll = [["nom","sidi"],["age",18],["Numero","0001"]]

d = dict(ll)
print(f"{ll}--dict--->{d}")


"---------- 8. dict des comprehension --------------"

d = {i:i*2 for i in range(10)}
print(d)