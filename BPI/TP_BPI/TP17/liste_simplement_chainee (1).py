#!/usr/bin/env python3

"""Listes simplements chainees + quelques operations"""

import traceur


class Cellule:
    """Une cellule d'une liste chaînée"""

    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

    def __str__(self):
        return "cellule_" + str(self.valeur)


class ListeSimplementChainee:
    """Une liste simplement chainee."""

    def __init__(self):
        self.tete = None
        self.queue = None
        self.taille = 0

    def __init__(self, iterable):
        self.tete = None
        self.queue = None
        self.taille = 0
        for e in iterable:
            ajoute_en_queue(self, e)

    def __str__(self):
        """Renvoie val1 --> val2 --> val3 ..."""
        return " --> ".join([str(c.valeur) for c in recupere_cellules(self)])


def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute une cellule en tete"""
    # Temps constant
    liste_chainee.taille += 1
    liste_chainee.tete = Cellule(valeur, liste_chainee.tete)
    if liste_chainee.queue is None:
        liste_chainee.queue = liste_chainee.tete
    return liste_chainee


def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une cellule en queue."""
    # Possible en temps constant grace au pointeur de queue.
    liste_chainee.taille += 1
    cellule = Cellule(valeur, None)
    if liste_chainee.queue is not None:
        liste_chainee.queue.suivant = cellule
    else:
        liste_chainee.tete = cellule
    liste_chainee.queue = cellule
    return liste_chainee


def recupere_cellules(liste_chainee):
    """Renvoie un itérateur sur toutes les cellules."""
    cell = liste_chainee.tete
    while cell is not None:
        yield cell
        cell = cell.suivant


def recherche(liste_chainee, valeur):
    """Recherche une valeur dans la liste_chainee donnée.

    Renvoie la premiere cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    cellule = liste_chainee.tete
    while(cellule is not None):
        if cellule.valeur == valeur:
            return cellule
        cellule = cellule.suivant
    return None


def supprime(liste_chainee, valeur):
    """Enleve la premiere cellule contenant la valeur donnée."""
    if(liste_chainee.tete is None):  # Cas pas d'éléments
        return liste_chainee
    if(liste_chainee.tete.valeur == valeur):  # Cas suppression de la tête
        liste_chainee.taille -= 1
        if liste_chainee.tete.suivant is None:  # Cas suppression seul élément
            liste_chainee.tete = None
            liste_chainee.queue = None
            return liste_chainee
        liste_chainee.tete = liste_chainee.tete.suivant
        return liste_chainee
    if liste_chainee.tete.suivant is None:  # Cas un seul élément à garder
        return liste_chainee

    # Cas avec minimum 2 cellules et la tête est à garder :
    cellule = liste_chainee.tete.suivant
    prec = liste_chainee.tete
    while(cellule is not None):
        if cellule.valeur == valeur:
            liste_chainee.taille -= 1
            prec.suivant = cellule.suivant  # Suppression
            if prec.suivant is None:  # cas de la queue
                liste_chainee.queue = prec
            return liste_chainee
        prec = cellule
        cellule = cellule.suivant
    return liste_chainee


def remplace_valeurs(liste_chainee, transforme):
    """Fait un map sur la liste en gros"""
    """Remplace les valeurs des cellules en appliquant la fonction transforme."""

    # Ici on utilise le générateur pour parcourir la liste chaînée.
    # Il n'y a pas de surcoût en calcul ni en mémoire, et le code
    # de parcours de liste est découplé du code de transformation.
    for cell in recupere_cellules(liste_chainee):
        cell.valeur = transforme(cell.valeur)


def filtre_cellules(liste_chainee, filtre):
    """Renvoie un itérateur sur les cellules filtrées."""

    # On utilise encore le générateur pour parcourir la liste chaînée.
    for cell in recupere_cellules(liste_chainee):
        filtree = filtre(cell.valeur)
        if not isinstance(filtree, bool):
            raise TypeError(
                "la fonction filtre a renvoyé autre chose qu'un booléen")
        if filtree:
            yield cell


def supprime_cellules(liste_chainee, filtre):
    """Supprime tous les cellules de liste pour lesquelles le filtre renvoie False.

    Coût = O(n) avec n qui est la taille de la liste chainée.
    """
    gardees_it = filtre_cellules(liste_chainee, filtre)
    tete = None
    queue = None
    taille = 0
    prec = None
    for cell in gardees_it:
        if tete is None:
            tete = cell
        if prec is not None:
            prec.suivant = cell
        queue = cell
        prec = cell
        taille += 1

    liste_chainee.tete = tete
    liste_chainee.queue = queue
    liste_chainee.taille = taille


def concatene(liste_chainee_1, liste_chainee_2):
    """Concatène liste_chainee_2 à liste_chainee_1 et vide liste_chainee_2.

    Ici c'est du temps constant, la preuve y a pas de boucle !
    C'est cool les listes chaînées :-)
    """
    # Si la liste 1 est vide, on change la tête
    if liste_chainee_1.tete is None:
        liste_chainee_1.tete = liste_chainee_2.tete
    # Sinon on lie les deux listes
    else:
        liste_chainee_1.queue.suivant = liste_chainee_2.tete

    # Si la liste 2 n'est pas vide, on change la queue
    if liste_chainee_2.tete is not None:
        liste_chainee_1.queue = liste_chainee_2.queue

    # On met à jour la taille
    liste_chainee_1.taille += liste_chainee_2.taille

    # On vide la liste 2
    liste_chainee_2.tete = None
    liste_chainee_2.queue = None


def decoupe(liste_chainee, fonction):
    """Crée et retourne deux listes : les cellules validant la fonction et les autres.
    Coût = O(n) avec n qui est la taille de la liste chainée.
    """
    # On crée les deux nouvelles listes
    oui = ListeSimplementChainee(range(0))
    non = ListeSimplementChainee(range(0))
    # Là encore, on va utiliser notre générateur pour
    # rajouter chacune des cellules dans la bonne liste
    # en fonction du résultat de l'appel à la fonction
    # `fonction`
    for cellule in recupere_cellules(liste_chainee):
        if fonction(cellule.valeur):
            ajoute_en_queue(oui, cellule)
        else:
            ajoute_en_queue(non, cellule)
    # Il n'y a rien apres la fin de chacune des listes.
    # Il faut donc "casser" le suivant de la queue
    # pour chacune des deux listes.
    for liste in (oui, non):
        if liste.queue is not None:
            liste.queue.suivant = None
    return (oui, non)


def test_listes():
    def multiplie_par_deux(val):
        """Multiplie val par deux et renvoie le résultat"""
        return val * 2

    def est_multiple_de_trois(val):
        """Renvoie True si val est multiple de 3, et False sinon"""
        return val % 3 == 0

    """Teste les fonctions ci-dessus"""

    # Teste le constructeur
    liste_chainee_vide = ListeSimplementChainee(range(1, 1))
    print("une liste vide :", liste_chainee_vide)
    liste_chainee = ListeSimplementChainee(range(42, 42 + 7))
    print("une liste à 7 éléments :", liste_chainee)

    # Teste la transformation
    remplace_valeurs(liste_chainee_vide, multiplie_par_deux)
    print("une liste vide après remplacement des valeurs par multiplication par deux :",
          liste_chainee_vide)
    remplace_valeurs(liste_chainee, multiplie_par_deux)
    print("une liste à 7 éléments après remplacement des valeurs par multiplication par deux :",
          liste_chainee)

    # Teste le filtre
    filtrees = filtre_cellules(liste_chainee_vide, est_multiple_de_trois)
    print("filtrage multiple de trois sur liste vide :", *filtrees)
    filtrees = filtre_cellules(liste_chainee, est_multiple_de_trois)
    # l'étoile ici est nécessaire pour que les cellules soient passées
    # en argument à `print` et non pas l'itérateur `filtrees`
    print("filtrage multiple de trois sur liste à 7 éléments :", *filtrees)
    # Teste de l'exception
    # filtrees = filtre_cellules(liste_chainee, multiplie_par_deux)
    # print(*filtrees)

    # Teste la suppression
    supprime_cellules(liste_chainee_vide, est_multiple_de_trois)
    print("supression sur liste vide :", liste_chainee_vide)
    supprime_cellules(liste_chainee, est_multiple_de_trois)
    print("supression des non-multiple de trois sur liste à 7 éléments :", liste_chainee)

    # On teste tous les cas "limites" pour la concaténation
    liste_chainee_1 = ListeSimplementChainee(range(0))
    liste_chainee_2 = ListeSimplementChainee(range(0))
    print("résultat concaténation", liste_chainee_1, "avec",
          liste_chainee_2, ":", end=" ")
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(5))
    liste_chainee_2 = ListeSimplementChainee(range(0))
    print("résultat concaténation", liste_chainee_1, "avec",
          liste_chainee_2, ":", end=" ")
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(0))
    liste_chainee_2 = ListeSimplementChainee(range(5))
    print("résultat concaténation", liste_chainee_1, "avec",
          liste_chainee_2, ":", end=" ")
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(5))
    liste_chainee_2 = ListeSimplementChainee(range(5))
    print("résultat concaténation", liste_chainee_1, "avec",
          liste_chainee_2, ":", end=" ")
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)

    # Teste trie pairs / impairs
    # Ici on utilise des lambdas : c'est à dire
    # des fonctions anonyme créées directement
    # dans un appel de fonction.
    liste_chainee = ListeSimplementChainee(range(0))
    print("résultat découpe pairs/impairs sur", liste_chainee, ":", end=" ")
    pairs, impairs = decoupe(liste_chainee, lambda x: x % 2 == 0)
    print(pairs, "et", impairs)
    liste_chainee = ListeSimplementChainee(range(11))
    print("résultat découpe pairs/impairs sur", liste_chainee, ":", end=" ")
    pairs, impairs = decoupe(liste_chainee, lambda x: x % 2 == 0)
    print(pairs, "et", impairs)


if __name__ == "__main__":
    test_listes()
