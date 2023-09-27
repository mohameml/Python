#!/usr/bin/env python3

from pile import Pile 


print("------------ Test de création ------------:")
p1 = Pile([1])
print(p1)

# Test d'empliemnt dans la pile :
print("----------- Test d'émpliement : -------------------")
for i in range(2,11):
    p1.empiler(i)

print(p1)

# Test de la Méthode : est_vide()
print("--------- est_vide() ----------")
print(f"{p1}est vide : {p1.est_vide()}")
p2 = Pile([])
print(f"{p2} est vide : {p2.est_vide()}")

# Test de la fonction : length 

print("------- test de la fonction : length ----------")

print(p1.length())
print(p2.length())


def test_length(pile,taille):

    if pile.length()==taille:
        print(f"Test de la Méthode length() :\033[92m{'PASSED'}\033[0m")
    else : 
        print(f"Test de la Méthode length() :\033[91m{'FAILED'}\033[0m")

test_length(p1,10)
test_length(p2,0)


p1.extend([11,12,13])
print(p1)

