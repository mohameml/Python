#!/usr/bin/env python3

"""
cour sur le set (ensemble)

"""

"--------------------- 1.Déf -------------------------------"

"""
le set sont  modifiables, non hachables, non ordonnés, non indexables et de ne contenir qu'une seule
copie maximum de chaque élément. 

"""

s = {1,2,3}
print(s)
print(type(s))

"RQ : Les sets ne peuvent contenir que des objets hachables "

"------------- 2. La fonction : set -----------------------"

print(f"[1,2,3,4,5]--set-->{set([1,2,3,4])}")
print(f"{range(4)}---set--->{set(range(4))}")
print(f"sidi ----set---> {set('sidi')}")


"RQ : les sets sont itérables :"
s = set(range(10))

for i in s :
    print(i)


"--------------- 3. Les Méthodes -----------------"

"""
La méthode .add() ajoute au set l'élément passé en argument.

"""

s = {1,2,3}
s.add(4)
print(s)

"""
La méthode .discard() retire du set l'élément passé en argument.

"""
s.discard(1)
print(s)

"""
la méthode .union() realise l'union de 2 ensembles 
"""
s1 = {1,2,3,4}
s2 = {1,2,5,6}
print(s1.union(s2))

"""
La Méthode .intersection() permet de faire l'intersection entre 2 ensembles

"""

s3 = {1,2,3,4}
s4 = {1,10}
print(s4.intersection(s3))


"""
la  Méthode .difference()

L'instruction s1.difference(s2) renvoie sous la forme d'un nouveau set les éléments de s1 qui ne sont pas
dans s2 ,et vie versa .
"""
print(s3.difference(s4))
print(s3)

"""
La méthode .issubset() indique si un set est inclus dans un autre set
"""
s1 = {1,2,3}
s2 = {2}

print(s1.issubset(s2))
print(s2.issubset(s1))

"""
La méthode .isdisjoint() indique si un set est disjoint d'un autre set

"""
print(s1.isdisjoint(s2))






"RQ : les sets ne supportent pas les opérateurs + et * ."


"-------------  4. Utilité --------------------"

"------- 4.1 Supprimer la redodance -----------------"
l=[1,2,3,4,1,2,3,5]
print(l)
l=list(set(l))
print(l)

"------------- 4.2 Un compteur des lettres ----------------- :"
seq = "atctcgatcgatcgcgctagctagctcgccatacgtacgactacgt"
print(seq)
l = [(base , seq.count(base)) for base in set(seq)]
print(l)

"------------ 5. Les Opérations : Union and Intersection ------------"

s1 = {1,2,3,4,5,6}
s2 = {2,4,8,9}
s_union = s1 | s2
print(s_union)

s_inter = s & s2 
print(s_inter)

"------------ 6. set en comprehension -------------------"

s = {i for i in range(10)}
print(s)
