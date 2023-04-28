#!/usr/bin/env python3

"""Un programme qui ne sert à pas grand chose."""

import sys


def teste():
    """Teste les fonctions :
        - `recupere_combinaisons_2`
        - `renverse`
        - `recupere_combinaisons`
        - `recupere_parametres`

    Ces trois fonctions testées seront écrites plus tard, mais c'est
    souvent une bonne chose de commencer par les tests, donc allons-y.
    En plus, écrire ce test vous obligera à réfléchir à l'algorithme
    général à appliquer pour générer les combinaisons, sur des séquences
    simples.

    Les spécifications du travail à réaliser sont données en commentaire
    dans le corps de la fonction ci-dessous.
    Vous devez rajouter une ou plusieurs lignes de code à chaque fois
    qu'il y a un TODO suivi de trois points.
    Pensez à bien enlever ces TODO et ces trois points dès que vous les
    avez implémentés.
    Merci de respecter les spécifications À LA LETTRE pour que la
    correction automatique soit possible.

    Pour rappel, en Python une séquence `seq` est un objet sur lequel on
    peut :
      - utiliser la fonction `len(seq)` pour connaître sa taille. Cette
        opération s'effectue en temps constant ;
      - utiliser une boucle `for` pour parcourir ses éléments ;
      - accéder au ième élément avec `seq[i]` (le premier élément est à
        l'indice `0`).
    """

    print('Résultats calculés dans ma tête pour la séquence "ABCD" et k=2')
    # affiche sur la sortie standard ces combinaisons calculées dans notre
    # tête (c'est à dire pour la séquence "ABCD" et k=2), avec une seule
    # combinaison par ligne, sous forme de chaîne de caractères,
    # par exemple AC
    seq="ABCD"
    
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            print(seq[i]+seq[j])

    print('Résultats calculés par recupere_combinaisons_2("ABCD")')
    # effectue l'appel à recupere_combinaisons_2('ABCD'), puis affiche
    # sur la sortie standard les combinaisons renvoyées par cet appel,
    # avec une seule combinaison par ligne. Une combinaison étant un
    # tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print``, c'est à dire de ne faire aucun
    # formatage. La combinaison AC sera donc affichée de la façon
    # suivante : ('A', 'C')
    l=recupere_combinaisons_2('ABCD')
    for tuple in l:
        
        print(tuple)


    

    

    # affiche sur la sortie standard une ligne vide
    print()

    print("Résultat de renverse sur [1, 2, 3]")
    # effectue l'appel à renverse([1, 2, 3]), puis
    # puis affiche sur ce résultat
    print(renverse([1, 2, 3]))

    # affiche sur la sortie standard une ligne vide
    print()

    print("Résultats calculés dans ma tête pour la séquence [0, 1, 2, 3, 4] et k=3")
    # affiche sur la sortie standard ces combinaisons calculées dans notre
    # tête (c'est à dire pour la séquence [0, 1, 2, 3, 4] et k=3), avec
    # une seule combinaison par ligne, sous forme de chaîne de caractères,
    # par exemple 014
    tab=[0,1,2,3,4]
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            for k in range(j+1,len(tab)):
                print(str(tab[i])+str(tab[j])+str(tab[k]))
    





    print("Résultats calculés par recupere_combinaisons([0, 1, 2, 3, 4], 3)")
    # effectue l'appel à recupere_combinaisons([0, 1, 2, 3, 4], 3), puis
    # affiche sur la sortie standard les combinaisons renvoyées par cet
    # appel, avec une seule combinaison par ligne. Une combinaison étant
    # un tuple, on vous demande pour l'affichage de passer directement ce
    # tuple à la fonction `print`, c'est à dire de ne faire aucun formatage.
    # La combinaison 014 sera donc affichée de la façon suivante : (0, 1, 4)
    l2= recupere_combinaisons([0,1,2,3,4], 3)
    for tuple in l2:
        t=(int(tuple[0]),int(tuple[1]),int(tuple[2]))
        print(t)
        




    # affiche sur la sortie standard une ligne vide
    print()

    # effectue l'appel recupere_parametres(x) avec x étant premier
    # argument de la ligne de commande puis affiche la séquence et
    # k renvoyés par cet appel.
    # Par exemple pour l'exécution de `python combinaisons.py input.txt`
    # x est `input.txt`
    print(
        "Résultats de recupere_parametres sur le fichier donné "
        "en paramètre sur la ligne de commande"
    )
    sequence,k=recupere_parametres(sys.argv[1])
    print(sequence)
    print(k)
    # affiche sur la sortie standard une ligne vide
    print()

    print(
        "Résultats calculés par recupere_combinaisons sur "
        "les paramètres dans le fichier"
    )
    # effectue l'appel à recupere_combinaisons en utilisant les paramètres
    # renvoyés par l'appel à recupere_parametres(x), puis affiche sur la
    # sortie standard les combinaisons renvoyées par cet appel, avec une
    # seule combinaison par ligne. Une combinaison étant un tuple, on vous
    # demande pour l'affichage de passer directement ce tuple à la fonction
    # `print`, c'est à dire de ne faire aucun formatage. La combinaison AC
    # sera donc affichée de la façon suivante : ('A', 'C')
    l1=recupere_combinaisons(sequence,int(k))
    for tuple in l1:
        print(tuple)



def recupere_parametres(filename):
    """Renvoie un tuple à deux entrées contenant la séquence et
    le paramètre k, DANS CET ORDRE, lus à partir du fichier passé
    en paramètre.

    Spécifications PRÉCISES (pensons aux tests automatiques)
    sur le format du fichier :
       - la première ligne contient le nombre k
       - les lignes suivantes contiennent les éléments de la séquence

    Vous trouverez un fichier `input.txt` dans votre dossier `exam` à
    titre d'exemple.
    """
    fichier=open(filename,"r")
    l=fichier.readlines()
    k=l[0].strip("\n")
    sequence=""
    for e in l[1:]:
        b=e.strip("\n")
        sequence = sequence + b
    fichier.close()
    return sequence,int(k)



def recupere_combinaisons_2(sequence):
    """ "Renvoie toutes les combinaisons de taille 2 de la séquence donnée.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par une
         `list` de `tuple`.
    """
    l=[]
    for i in range(len(sequence)):
        for j in range(i+1,len(sequence)):
            tuple=(sequence[i],sequence[j])
            l.append(tuple)
    return l




def renverse(sequence):
    """
    Renvoie une nouvelle `list` contenant tous les éléments
    de la séquence donnée en paramètre mais dans l'ordre inverse.
    """
    sequence_inverse=sequence[::-1]
    l=list(sequence_inverse)
    return l


def recupere_combinaisons(s , k):
    """
    Renvoie toutes les combinaisons de taille k de la sequence donnée.

    Attention, cette fonction est difficile à implémenter.
    Il est vivement conseillé de réfléchir à un algorithme sur le
    papier avant de se lancer dans le code.
    Vous pouvez utiliser la fonction `renverse` si besoin,
    mais ce n'est pas du tout une obligation.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - les combinaisons renvoyées sont représentées par
         une `list` de `tuple`.
    """
    l=[]
    sequence=""
    for i in s:
        sequence = sequence + str(i)
     
    n=len(sequence)
    for i in range(n-k+2):
        seq=sequence[i:k-1+i]
        for e in sequence[k-1+i:]:
            l.append(tuple(seq+e))
    return l

def affiche_nombre_combinaisons():
    """Affiche le nombre de k-combinaisons d'une séquence de taille n.

    On vous demande ici d'afficher sur la sortie standard la formule que
    vous écririez au tableau lors d'une séance de TD, pour répondre à cette question.

    Spécifications PRÉCISES (pensons aux tests automatiques) :
       - l'affichage de la formule se fera en fonction de la taille de la séquence n,
         et du paramètre k
       - les seuls caractères autorisés dans la chaîne affichée sont :
           + `*`, `/` et `-`
           + les lettres `n` et `k`
           + des parenthèses
           + le caractère `!` (factorielle)
    """
    formule="n!/k!(n-k)!"
    return formule


# La fonction teste() est appelée uniquement dans
# le cas où le programme est invoqué comme programme
# principal avec `python combinaisons.py input.txt`
# ou avec `./combinaisons.py input.txt`
if __name__ == "__main__":
    teste()
