#!/usr/bin/env python3
""" ce programme sert a resoudre le td 12 decembre 2017 "
dans un fichier sur chaque ligne:
>>>>> on l'adrese IP de l'utilisateur 
>>>>> on a la date de visite de l'utilisateur 
>>>>> on a l'heure de visite
>>>>> le fichier visite par l'uitilisateur   
"""


def charger_info(fichier):
    " cette fonction permet de charger des info a partir d'un fichier"

    file = open(fichier, "r")
    l = []

    for ligne in file:
        ligne = ligne.replace("\n", "")
        liste_donnes = ligne.split(" ")
        l.append(liste_donnes)
    file.close()

    return l


def nb_fic_date(l):
    d = {}
    for donne in l:
        date = donne[1]
        if date in d:
            d[date] += 1
        else:
            d[date] = 1

    return d


def le_10_date(d):
    l = []
    for k in d:
        l.append((d[k], k))
    l.sort(reverse=True)

    return l[0:10]


def test():
    l=charger_info("logpdf.txt")
    d=nb_fic_date(l)
    for i in le_10_date(d):
        print(i)

 
