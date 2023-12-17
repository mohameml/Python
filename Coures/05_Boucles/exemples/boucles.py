#!/usr/bin/env python3

# ---------- la fonction enumérate -------------- 

# Python possède toutefois la fonction enumerate() qui vous permet d'itérer sur les indices et
# les éléments eux-mêmes


l = list(range(10))


for i , e in enumerate(l) :
    print(f"l'élement d'indice {i} est {e}")


# ------------ Exemple ---------------------- 

# Triangle : 
print("---------- Triangle -------------")
for i in range(10):
    print("*"*i)


# Triangle invérse   : 
print("---------- Triangle inversé  --------------")
for i in range(10):
    print("*"*(10-i))


# Triangle gauche : 
étoile = "*"
print("------------- Triangle gauche : ---------------")
for i in range(10):
    étoile = "*"*i
    print(f"{étoile :>9s}")


# pyramide  : 

print("------------- pyramide  : ---------------")
for i in range(10):
    étoile = "*"*i
    print(f"{étoile :^9s}")










