#!/usr/bin/env python3

" cour 03 : affichage "


# ------------- 1. la fonction print()  ---------------

# la fonction print : affiche le contenu + retour à la ligne
print("Hello world !")

# pour désactiver le retour à la ligne
print("sidi", end="")
print(" va a l'école ")

# utiliser deux print sur le meme ligne
print("Bonjour ")
print("le gars ")

# a l'aide de la fonction print on peut afficher le contenu d'une variable

var = 3
print(var)

# la fonction print prend : un nombre des variables infinie
a = b = c = d = e = 2
# il y'a un espace par défaut entre deux variables lors de l'affichage
print(a, b, c, d, e, "sidi")

# l'argument sep
print("Bonj", "our", sep="")
print("Hello", "world", "!", sep="-")


# ------------------ 2. Ecriture formatée --------------


# ------------------- 2.1. f-string -----------------

# Défintion
chaine = f'hello le world '
print(type(chaine))
print(chaine)

# Exemple
age = 20
nom = "sidi"
print(f'{nom} a {age} ans ')

# Spécificarion de format

# Exemple
a = 100/3
b = float(f'{a:.2f}')
print(b)
print(type(b))

print(f"la valeur approchée de a est {a:.2f}")


""" 
.xf : pour le float , x: un enteir positif
.d : pour le int 
.s : pour le string  
"""
c = 100
print(f'la valeur de a est {c:d}')


# l'aligénement avce f-string
print(123456)
# ceci signifie que "10" va prendre 8 espace et situe à droite
print(f"{10:>8d}")

print(f"{10:<8d}", end="")  # à gauche

print(f"{10:^8d}")  # au centre

# on indiquer le lettre de remplissage
print(f"{10:0>8d}")
print(f"{10:*^8d}")

# ce formatage est également valable pour le str : en utilsant "s" au lieu "d"


chaine = "sidi"


print(f"{chaine:^8s}")
print(f"{chaine:*^8s}")

# Remarque en float : On combiner le nombre de carctéres avec le nombre de décimales

e = 100/3
print(f"{a:7.3f}")  # par défaut justifé a droite
print(f"{a:^7.3f}")



# ---------------  2.2 . la méthode .format() ---------------   

age = 30
chaine_2 = "sidi a {} ans ".format(age)
print(chaine_2)


# ---------------  2.3.  l'opérateur % ---------------   

age = 30
nom = "sidi"
chaine_3 = "%s a %d ans "%(nom,age)
print(chaine_3)


