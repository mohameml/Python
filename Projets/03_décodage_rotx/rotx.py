#!/usr/bin/env python3

"""Module d'encodage/décodage par rotation"""


def rot(decalage, lettre):
    """
    Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractères de taille 1 ;
       - lettre est un soit une lettre majuscule , soit une lettre minuscule.
         
    """
    # On verifie tout d'abord les Préconditions :
    
    if len(lettre)==1 :
        
        decode_lettre=ord(lettre)+decalage 
        if  65 <= ord(lettre) <= 90 :
            
            if decode_lettre > 90 :
                res = decode_lettre-90
                return chr(65+res-1)
            else :
                return chr(decode_lettre)
            
        
        elif 97 <= ord(lettre) <= 122 :
            
            if decode_lettre > 122 :
                res = decode_lettre-122
                return chr(97+res-1)
            
            
            return chr(decode_lettre)
            
        
        
        return lettre
        
    
    return lettre
        
    
    


def rot13(lettre):
    """
    Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    
    if len(lettre)==1 :
        return rot(13,lettre)


    
    
