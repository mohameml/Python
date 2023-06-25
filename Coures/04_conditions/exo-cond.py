#!/usr/bin/env python3


# Exercice 3 :

def min_list(l : list ):
    " return le min de liste "

    min_l = l[0]

    for e in l[1:] :
        if e < min_l :

            min_l = e
    
    return min_l

# Exercice 4 : fréquence d'une mot 


def freq_mot(chaine):

    freq = {}

    for e in chaine :
        if e in freq :
            freq[e] += 1
        else : 
            freq[e] = 1 

    return freq 
#  Test  : 

print(freq_mot("nebill"))

        




