#!/usr/bin/env python3
"""test de la MT reconnaissant le langage L1 de l'exo 1.

Usage:

    ./test_l1.py chemin_vers_votre_solution.mt 

"""
import sys

def accepte(nom_fichier, mot, ok):
    from simule import simule

    print("testing:", repr(mot), end="\t")
    (etat, est_final, nb_pas, r) = simule(nom_fichier, mot, False,False)

    if est_final:
        assert ok
        print(" OK (as expected)")
    else:
        assert (not ok)
        print(" KO (as expected)")        
        
if len(sys.argv) != 2:
    print("Enter a name of machine as arg")
    sys.exit(1)

nom_fichier = sys.argv[1]
        
for mot in ("c", "aca", "bcb", "abcab", "bacba", "aacaa", "abacaba", "bbaacbbaa", "aaabbacaaabba"):
    accepte(nom_fichier, mot, True)

for mot in ("", "ca", "ac", "aaa", "abcba", "bacbab", "babcba", "aaacaab", "bbaacccbbaa", "bcbcb"):
    accepte(nom_fichier, mot, False)

    
