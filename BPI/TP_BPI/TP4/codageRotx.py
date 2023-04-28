"""Module d'encodage/décodage par rotation"""


from re import M


def rot(decalage, lettre):
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractères de taille 1 ;
       - lettre est un soit une lettre majuscule
         soit une lettre minuscule.
    """
    if len(lettre)!=1:
        return None
    code=ord(lettre)
    Majuscule=65<=code<=90
    Minuscule=97<=code<=97+26
    if not(Majuscule or Minuscule):
        return None
    if Majuscule:
        premiere_lettre="A"
    else:
        premiere_lettre="a"
    code_normalise=code-ord(premiere_lettre)
    code_rot=(code_normalise+decalage)%26 + ord(premiere_lettre)

    return chr(code_rot)


def rot13(lettre):
    """Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    
    return rot(13,lettre)









