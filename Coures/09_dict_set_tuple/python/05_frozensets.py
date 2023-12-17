#!/usr/bin/env python3

"""
cour sur le frozenset
"""
"-------------- 1.Déf ----------------"

"""
Les frozensets sont des sets non modifiables et hachables.

Comme la différence entre tuple et liste, l'immutabilité des frozensets donne
l'assurance de ne pas pouvoir les modifier .
"""

"""
Pour créer un frozenset on utilise la fonction interne
frozenset() qui prend en argument un objet itérable et le convertit (opération de casting) :

"""
f = frozenset([1,2,3,4])
print(f)


"---------------- 2. Les Méthodes ----------------------"

"""
Les frozensets ne possèdent bien sûr pas les méthodes de modification des sets ( .add() , .discard() , etc.)
puisqu'ils sont non modifiables. 
Par contre, ils possèdent toutes les méthodes de comparaisons de sets ( .union() , .intersection() , etc.).

"""