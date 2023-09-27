#!/usr/bin/env python3

"""
cour sur les containers 

"""

"--------------------------- I.  Containers  --------------------------------"

"----- 1. Déf ----------"
"""
Déf :
Un container est un nom générique pour définir un objet Python qui contient une collection d'autres objets.
Exemple :
list , chaine de caracteres et le range .....

"""

"-------- 2. Propriétes ---------------"

"""
1. Test d'appertanace # elem in l 
2. Supporter la fonction len()  # len(l)
3.les élmeents sont ordonées  
4. Indexable (subscriptable en anglais) : on peut retrouver un élément par son indice 
5. Itérable  : on peut faire une boucle dessus


"""


# Exemple 1 :
l =["1",1,[1,2]]

print("1" in l )

#Exemple 2 :
chaine ="sidi va à l'école"
print("sidi" in chaine)


"------------- 3. Objet Séquentielle ---------------"

"""
Un objet séquentiel ou séquence :est un container itérable, ordonné et indexable. 
Les objets séquentiels sont les
listes, les chaînes de caractères, les objets de type range, ainsi que les tuples (cf. plus bas).

"""


"--------------------- 4. Mutabilite ---------------------"

"""
Un objet est dit non modifiable lorsqu'on ne peut pas le modifier, ou lorsqu'on ne peut pas en modifier un
de ses éléments si c'est un container. On parle aussi d'objet immuable (immutable object en anglais).

Exemple : chaine des carcateres , tuple .

"""


"---------------------- 5. Identifiant d'un Objet ------------------------------"

"""
Identifiant d'un objet est un nombre entier qui est garanti constant pendant toute la durée de vie de l'objet.

Cet identifiant est en général unique pour chaque objet. 
Toutefois, pour des raisons d'optimisation, Python crée parfois le même identifiant pour deux objets non modifiables différents
qui ont la même valeur.

L'identifiant peut être assimilé à l'adresse mémoire de l'objet qui elle aussi est unique. 

En Python, on utilise la fonction interne id() qui prend en argument un objet et renvoie son identifiant .
"""

# Exemple sur le list :
l=[1,2]
print(f"L'id de {l} avant : {id(l)}")
l.append(3)
print(f"L'id de {l} aprés la modification: {id(l)} ")

print("Donc l'id ne change ce qui justifie la mutabilite de list ")


"--------------------------------- 6. hachabilité ---------------------------------"

"""
Un objet Python est dit hachable (hashable en anglais) s'il est possible de calculer une valeur de hachage sur
celui-ci avec la fonction interne hash()

"""

"""
RQ 1:
En programmation, la valeur de hachage peut être vue comme une
empreinte numérique de l'objet
"""

"""
RQ 2 :

Les objets hachables sont les chaînes de caractères, les entiers, les floats, les booléens, les objets de type
range, les tuples (sous certaines conditions) et les frozensets ; 
par contre, les listes, les sets et les dictionnaires sont non hachables

"""