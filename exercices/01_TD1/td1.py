#!/usr/bin/env python3
"""
-------------------- TD1 ----------------
"""
print("------- exercice 1 : porteé d'une varaiable -------")

# on definie ici une varaiale globale
une_var_glob = 7


def f(un_param):
  # une varaible definie dans une fonction est  locale
  une_var_loc = 4
  une_autre_var_loc = un_param + une_var_loc
  print(une_autre_var_loc)


f(une_var_glob)
print(une_var_glob)
print("----------Exercice 2 : portée des variables avec même nom--------")

# a globale vaut 7
a = 7


def f(a):
  b = 8
  a = a + b
  print(a)


a = 11
print(a)
f(a)
print(a)

print("---- exemple 2 ----")

c = 10
print(c)


def change_nb(c):
  c += 1
  return c


c = change_nb(c)
print(c)

print("-------------Exercice 3 : typage dynamique--------------")
"""

Le typage dynamique est un concept dans la programmation qui se réfère à la capacité d'un langage de programmation à déterminer le type d'une variable au moment de l'exécution. Cela signifie que vous n'avez pas besoin de déclarer explicitement le type d'une variable avant de l'utiliser, et que le type de la variable peut changer au cours de l'exécution du programme.

"""

a = "1"
b = "3"
print(a + b)
a = 1
b = 3
print(a + b)

# a = "1"
# b = 3
# print(a + b)

t1 = (1, 3)
print(t1[0] + t1[1])

# t2 = (1, "3")
# print(t2[0] + t2[1])
"""
On remarque que le python est un langage de typage dynamique 

"""

print("------ exercice 4 : Nos propres type : namedtuple--------------")

from collections import namedtuple

Perssonne = namedtuple("Personne", "nom, prenom, age")

persson1 = Perssonne("sidi", "khaled", 28)

print(persson1)

print(persson1.age)

# persson1.nom = "mohamed"
# cette affectaion va retouner une erruere car le namedtuple sont immutables

print(persson1.nom)
