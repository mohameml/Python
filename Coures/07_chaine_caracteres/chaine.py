#!/usr/bin/env python3

"""
cour chaine de caractérers 

"""

"-------------------- 1. chaine de liste -------------------"

"""
Les chaînes de caractères peuvent être considérées comme des listes (de caractères) un peu
particulières :
Mais a contrario des listes, les chaînes de caractères présentent toutefois une différence
notable, ce sont des listes non modifiable
"""

chaine = "sidi va à l'ècole"

# chaine[1]="s" renvoie un TypeError


"""
RQ :
Par conséquent, si vous voulez modifier une chaîne de caractères, vous devez en construire
une nouvelle. Pour cela, n'oubliez pas que les opérateurs de concaténation ( + ) et de
duplication ( * )
"""


"------------- 2. Caracteres spéciaux -----------------"

"\n" # retour a la ligne
"\t" # pour la tabulation 
# Exemple :

print("sidi va\t :  \n\ta l'école")

"\"" , "\'" # pour les caratéres " et ' 

print("Bonjour \"sidi\" ")


"----------------- 3. Préfixe de chaîne de caractères (f,r) ------------------"

"""
Un stringprefix modifie la manière dont Python va interpréter la dite string. Celui-ci doit être
systématiquement « collé » à la chaîne de caractères, c'est-à-dire pas d'espace entre les deux.

"""

# Exemple : le f-string 

a = "à l'école"
print(f"sidi va {a} ")

#----------------- le prefix : r ---------------------
"""
Le préfixe r mis pour raw string qui force la non-interprétation des caractères spéciaux 

"""

print(r"voici un retour a la ligne \n désactive")



"---------------------- 4. Méthodes associées aux chaines des car ---------------------------"
print("------------------ 4. Méthodes associées aux chaines de car -----------------------------")

print("----- 4.1 formatage de text -------")

chaine = "sidi"
print(f"{chaine.lower()}") # chaine en minuscule
print(f"{chaine.upper()}") # chaine en majscule
print(f"{chaine.capitalize()}") # met chaine[0] en Maj 


print("----- 4.2 .split() ---------")

"""
La méthode .split() découpe une chaîne de caractères en plusieurs éléments appelés
champs, en utilisant un séparateur et return une list 

"""
chaine="sidi va à l'école"
l = chaine.split()
print(l)

"""
RQ : maxsplit 
Il est également intéressant d'indiquer à .split() le nombre de fois qu'on souhaite découper
la chaîne de caractères avec l'argument maxsplit

"""

ll = chaine.split(maxsplit=1)
print(ll)


print("---- 4.3  .find() ----")

"""
La méthode .find() , quant à elle, recherche une chaîne de caractères passée en argument .
return l'indice de caracétre passe en paramétres 

"""
chaine = "sidi"

print(f"l'élement d se troue a l'indice : {chaine.find('d')} dans {chaine}")

"""
RQ :

* Si l'élément recherché est trouvé, alors l'indice du début de l'élément dans la chaîne de

* caractères est renvoyé. Si l'élément n'est pas trouvé, alors la valeur -1 est renvoyée

* La Méthode .rfind("elme")  : return l'indice de deriner Occurence de "elme" 


"""

print("------ 4.4 .replace() -------")

"""
On trouve aussi la méthode .replace() qui substitue une chaîne de caractères par une autre .

"""
chaine ="Girafe"
print(chaine)
nv_chaine = chaine.replace("G","g")
print(nv_chaine)


print("------- 4.5 .count() --------")

"""
La méthode .count() compte le nombre d'occurrences d'une chaîne de caractères passée en
argument :

"""
chaine = "sidi"

print(f"l'élement i existe {chaine.count('i')} fois dans {chaine}")

print("--------------- 4.6  .startswith   -----------------------")

"""
La méthode .startswith() vérifie si une chaîne de caractères commence par une autre
chaîne de caractères :


"""

chaine1 = "Bonjour"
chaine2 = "Bon"
chaine3 ="sidi"
print(chaine1)
print(chaine2)
print(chaine3)

print(chaine1.startswith(chaine2))
print(chaine1.startswith(chaine3))

"""
RQ :
Cette méthode est particulièrement utile lorsqu'on lit un fichier et que l'on veut récupérer
certaines lignes commençant par un mot-clé

"""

print("------------------ 4.7 strip() , lstrip() , rstrip() ------------------------")


".strip()" # la méthode .strip() permet d'enlèver les espaces (ou un argument passe en param) situés sur les bords de la chaîne de caractère 


# Exemple1:
chaine = "\t sidi va a l'école  "
print(chaine)
print(f"l'utilisation de strip():{chaine.strip()}")

# Exemple 2 :

a = "2\n"
print(a)
# on veut ignore le \n
a = a.strip('\n')
print(fr"aprés l'uitlisaltion de strip('\n') : {a}")

"""
RQ :
La méthode .strip() est très pratique quand on lit un fichier et qu'on veut se débarrasser des
retours à la ligne

"""

".lstrip()" # pour énlever des caracteres au debut de la chaine 

".rstrip()" # pour enlever des caracteres au fin de la chaine


print("-------------- 4.8 La Méthode join() ---------------------")

"""
La Méthode join() : permet de transformer une list de chaine de caracteres en une chaine de caracteres
"""

chaine = "".join([f"{i}" for i in range(10)])
print(chaine)

"""
RQ :
Les éléments de la liste initiale sont concaténés les uns à la suite des autres et intercalés par
un séparateur qui peut être n'importe quelle chaîne de caractères
"""
# Exemple :
chaine ="-".join([str(i) for i in range(10)])
print(chaine)

"""
Attention :
Attention, la méthode .join() ne s'applique qu'à une liste de chaînes de caractères.

"""

# Exemple :
chaine = "@".join(map(str,list(range(1,10))))
print(chaine)