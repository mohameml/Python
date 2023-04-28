#!/usr/bin/env python3
"""Un exemple de références vers des fonctions"""

def multiplie_par_deux(un_nombre):
    """Renvoie un_nombre multiplié par deux"""
    return un_nombre * 2

def ajoute_42(un_nombre):
    """Renvoie un_nombre + 42"""
    return un_nombre + 42

def applique_operation(un_nombre, operation):
    """Renvoie le résultat de l'opération donnée sur le nombre donné"""
    return operation(un_nombre)

def main():
    """Test de nos fonctions"""
    entier = 17
    # fonc1 et fonc2 sont des références vers une fonction
    fonc1 = multiplie_par_deux
    fonc2 = ajoute_42
    # On appelle multiplie_par_deux comme d'habitude.
    # C'est à dire en utilisant son nom.
    # Ce-dernier n'est en fait qu'une référence vers
    # la fonction elle-même.
    print(multiplie_par_deux(entier))
    # fonc1 est une référence vers une fonction
    # au même titre que multiplie_par_deux.
    # On peut donc l'appeler.
    print(fonc1(entier))
    # On passe une référence vers une fonction
    # en paramètre à la fonction applique_operation
    print(applique_operation(entier, multiplie_par_deux))
    # On passe une référence vers une fonction
    # en paramètre à la fonction applique_operation
    print(applique_operation(entier, fonc2))
    # On passe une référence vers une fonction
    # en paramètre un entier à la place d'une fonction
    # à la fonction applique_operation --> ERREUR
    print(applique_operation(entier, fonc1(entier)))

if __name__ == "__main__":
    main()
