#!/usr/bin/env python3

"""Listes doublement chaînées"""

import itertools
import traceur


class Cellule:
    """Une cellule d'une liste doublement chaînée.

    Contient une référence vers une valeur, une référence
    vers la cellule suivante et une référence vers la cellule
    précédente.
    """

    def __init__(self, valeur, precedent, suivant):
        self.valeur = valeur
        self.suivant = suivant
        self.precedent = precedent

    def __str__(self):
        """Pour pouvoir afficher des cellules facilement."""
        return str(self.valeur)


class ListeDoublementChainee:
    """Une liste doublement chaînée.

    Contient une référence vers la cellule de tête et une autre
    vers la cellule de queue.
    """

    def __init__(self):
        self.tete = None
        self.queue = None

    def __str__(self):
        """Pour pouvoir afficher des listes doublement chaînées facilement.

        N'hésitez pas à poser des questions à votre enseignant concernant
        cette ligne de code très jolie, mais complexe.

        On pourrait également construire notre chaîne de caractères avec
        une boucle for. Ce serait tout aussi correct.
        """
        return " --> ".join(str(cell) for cell in recupere_cellules(self))


# QUESTION 1
def ajoute_en_tete(liste_chainee, valeur):
    """Ajoute un élément en tête de liste chaînée en temps constant."""

    # Dans tous les cas, la tête doit être une nouvelle cellule.
    liste_chainee.tete = Cellule(valeur, precedent=None, suivant=liste_chainee.tete)

    # Si la liste chaînée n'était pas vide, donc qu'il
    # y avait une queue, il faut mettre à jour l'attribut
    # précédent de l'ancienne tête pour qu'il référence
    # la nouvelle tête.
    if liste_chainee.queue:
        liste_chainee.tete.suivant.precedent = liste_chainee.tete

    # Sinon il faut mettre à jour la queue de la liste chaînée.
    else:
        liste_chainee.queue = liste_chainee.tete


# QUESTION 1
def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute un élément en queue de liste chaînée en temps constant."""

    # Dans tous les cas, la queue doit être une nouvelle cellule.
    liste_chainee.queue = Cellule(valeur, suivant=None, precedent=liste_chainee.queue)

    # Si la liste chaînée n'était pas vide, donc qu'il
    # y avait une tête, il faut mettre à jour l'attribut
    # suivant de l'ancienne queue pour qu'il référence
    # la nouvelle queue.
    if liste_chainee.tete:
        liste_chainee.queue.precedent.suivant = liste_chainee.queue

    # Sinon il faut mettre à jour la tête de la liste chaînée
    else:
        liste_chainee.tete = liste_chainee.queue


# QUESTION 2
def recupere_cellules(liste_chainee):
    """Renvoie un itérateur sur toutes les cellules.

    Résistant aux changements sur la cellule courante grâce à la
    sauvegarde du suivant avant le yield.
    """
    cellule_courante = liste_chainee.tete
    while cellule_courante:
        cellule_suivante = cellule_courante.suivant
        yield cellule_courante
        cellule_courante = cellule_suivante


# QUESTION 3
def recupere_cellules_inversees(liste_chainee):
    """Renvoie un itérateur sur toutes les cellules en ordre inverse.

    Avec une liste doublement chaînée c'est assez simple car nous avons
    accès au précédent de chaque cellule. Dans une liste simplement chaînée,
    il faut nécessairement mémoriser toutes les cellules du début jusqu'à la
    fin, puis parcourir à l'envers.

    Résistant aux changements sur la cellule courante grâce à la
    sauvegarde du précédent avant le yield.
    """
    cellule_courante = liste_chainee.queue
    while cellule_courante:
        cellule_precedente = cellule_courante.precedent
        yield cellule_courante
        cellule_courante = cellule_precedente


# QUESTION 4
def recherche(liste_chainee, valeur):
    """Renvoie la première cellule contenant la valeur donnée, None si pas trouvée."""

    def teste_valeur(cellule):
        """Cette fonction interne va être utiliser par `filter`."""

        # La variable valeur n'existe pas dans la fonction teste_valeur.
        # Dans ce cas, l'interpréteur va chercher une variable avec ce nom
        # dans la fonction englobante, c'est à dire la fonction `recherche`
        # ici.
        return cellule.valeur == valeur

    # On récupère un itérateur sur toutes les cellules ayant la valeur que l'on
    # cherche grâce à la fonction standard `filter`.
    # Ici il faut bien garder en tête qu'avec des itérateurs nous travaillons de
    # façon "paresseuse" (lazy en anglais), c'est à dire que la liste chaînée
    # n'est pas parcourue tant qu'on ne fait pas d'appels aux fonctions des
    # itérateurs permettant de récupérer le prochain élément.
    iterateur_cellules_filtrees = filter(teste_valeur, recupere_cellules(liste_chainee))

    # On renvoie le premier élément de cet itérateur on None si il est vide
    return next(iterateur_cellules_filtrees, None)


# QUESTION 5
def enleve_cellule(liste_chainee, cellule):
    """Enlève la cellule donnée en temps constant."""

    # Si la cellule enlevée n'est pas la tête, il faut
    # mettre à jour le champ suivant de la cellule
    # précédente.
    if cellule.precedent:
        cellule.precedent.suivant = cellule.suivant

    # Sinon il faut mettre à jour la tête de la liste chaînée.
    else:
        liste_chainee.tete = cellule.suivant

    # Si la cellule enlevée n'est pas la queue, il faut
    # mettre à jour le champ précédent de la cellule
    # suivante.
    if cellule.suivant:
        cellule.suivant.precedent = cellule.precedent

    # Sinon il faut mettre à jour la queue de la liste chaînée.
    else:
        liste_chainee.queue = cellule.precedent


# QUESTION 6
def recupere_valeurs(liste_chainee):
    """Renvoie un itérateur sur toutes les valeurs."""
    for cellule in recupere_cellules(liste_chainee):
        yield cellule.valeur


# QUESTION 6
def recupere_entiers_proches(liste_chainee):
    """Renvoie les deux valeurs (entiers) les plus proches.

    La complexité avec itertools.combinations = A^k_n / k! = n! / k!(n-k)! notée C^k_n
    avant, et maintenant (n,k) mais verticalement, appelé coefficient binomial.
    Ici on a k = 2 donc complexité = n! / 2*(n-2)! = n * (n-1) / 2
    """

    # On crée un itérateur sur toutes les valeurs de la liste chaînée.
    iterateur_valeurs = recupere_valeurs(liste_chainee)

    # On crée un itérateur sur toutes les combinaisons de 2 valeurs.
    iterateur_couples = itertools.combinations(iterateur_valeurs, 2)

    # Ici on utilise une "expression génératrice" qui crée un itérateur
    # comme une fonction génératrice.
    # Néanmoins, comme on le voit ici, pas besoin de créer de fonction avec yield
    # on utilise simplement des parenthèses avec à l'intérieur une structure de la forme:
    # (X for Y in Z)
    # Toutes les valeurs prises par X seront "yieldées" par l'itérateur créé.
    #
    # Ici l'itérateur créé contient des tuples à deux éléments :
    #   - le premier est un entier représentant la distance entre les deux valeurs stockées
    #     dans le deuxième élément
    #   - un tuple à deux éléments représentant deux valeurs
    iterateur_distance_elements = (
        (abs(e1 - e2), (e1, e2)) for e1, e2 in iterateur_couples
    )

    # Pour comprendre la ligne ci-dessous, il faut savoir que par défaut,
    # les tuples python sont ordonnés selon leur premier élément et que donc
    # si on demande à la fonction min le minimum parmi un itérateur de tuples,
    # celle-ci nous renvoie le tuple avec la plus petite première valeur,
    # en l'occurrence le plus petit abs(e1 - e2).
    min_distance_elements = min(iterateur_distance_elements)

    # Le couple le plus proche est simplement le deuxième élément du
    # tuple min trouvé ci-dessus.
    return min_distance_elements[1]


# QUESTION 6
def recupere_cellules_apres(cellule):
    """Renvoie un  itérateur sur les cellules après la cellule donnée."""
    cellule_courante = cellule
    while cellule_courante:
        yield cellule_courante
        cellule_courante = cellule_courante.suivant


# QUESTION 6
def recupere_paires_valeurs(liste_chainee):
    """Renvoie un  itérateur sur toutes les paires de valeurs."""
    for premiere in recupere_cellules(liste_chainee):
        for deuxieme in recupere_cellules_apres(premiere.suivant):
            yield premiere.valeur, deuxieme.valeur


# QUESTION 6
def recupere_entiers_proches_bis(liste_chainee):
    """Renvoie les deux valeurs les plus proches.

    Utilise le fait qu'une distance n'est jamais < 0.
    """

    def distance(paire):
        return abs(paire[0] - paire[1])

    paires = recupere_paires_valeurs(liste_chainee)
    paire_min = next(paires)
    dist_min = distance(paire_min)
    if dist_min == 0:
        return paire_min
    for paire_cour in paires:
        dist_cour = distance(paire_cour)
        if dist_cour == 0:
            return paire_cour
        if dist_cour < dist_min:
            paire_min, dist_min = paire_cour, dist_cour
    return paire_min


# QUESTION 7
def supprime_doublons(liste_chainee):
    """Supprime les éléments en double.

    On utilise un `set` pour savoir si une valeur est en
    double ou non et deux des fonctions déjà implémentées
    pour factoriser le plus possible notre code.
    """
    valeurs_vues = set()  # comme un `dict` mais ne stocke que les clefs
    for cellule in recupere_cellules(liste_chainee):
        if cellule.valeur in valeurs_vues:
            enleve_cellule(liste_chainee, cellule)
        else:
            valeurs_vues.add(cellule.valeur)


# QUESTION 8
def entrelace(liste_chainee_1, liste_chainee_2):
    """Entrelace les éléments des deux listes et vide `liste_chainee_2`.

    Après l'entrelacement, cette fonction ajoute tout le reste
    de la plus longue des deux listes chaînées à la fin.
    Cette fonction ne crée pas de nouvelle cellule.

    Pré-condition:
      - les deux listes chaînées sont non vides
    """

    # On commence par prendre un élément sur deux dans chaque liste chaînée.
    iter1, iter2 = recupere_cellules(liste_chainee_1), recupere_cellules(
        liste_chainee_2
    )
    for cellule1, cellule2 in zip(iter1, iter2):
        cellule1.precedent = cellule2.precedent
        cellule2.precedent = cellule1
        cellule2.suivant = cellule1.suivant  ## [***]
        cellule1.suivant = cellule2

    # Ici cellule2 est garantie d'exister car les deux listes chaînées
    # sont non vides et donc on est passé au moins une fois dans la boucle.
    # On le dit à pylint qui ne peut pas le savoir pour qu'il supprime ses
    # warnings :
    # pylint: disable=undefined-loop-variable

    # On va maintenant raccrocher la fin de la liste la plus longue.
    # cellule2 est la dernière cellule de liste_chainee_2 qui a été traitée, et
    # cellule2.suivant est ce qui suivait à l'origine la dernière cellule de
    # liste_chainee traitée (voir [***]). Donc, if cellule2.suivant <=>
    # if "liste_chainee_1 était plus longue que liste_chainee_2"
    if cellule2.suivant:
        # il faut raccrocher la dernière cellule de liste_chainee_2 grâce au précèdent
        # de la première cellule non traitée de liste_chainee_1
        cellule2.suivant.precedent = cellule2
    else:
        # il faut re-accrocher la fin de liste_chainee_2
        cellule2.suivant = next(iter2, None)
        # et ne pas oublier de changer la queue de liste_chainee_1
        liste_chainee_1.queue = liste_chainee_2.queue

    # On vide la deuxième liste chaînée.
    liste_chainee_2.tete, liste_chainee_2.queue = None, None


def teste_listes():
    """On teste toutes les operations de base, dans différentes configurations."""
    ex = ListeDoublementChainee()
    ajoute_en_tete(ex, 1)
    ajoute_en_tete(ex, 2)
    ajoute_en_tete(ex, 3)
    # START CORRECTION
    variable = traceur.Variable("liste_321", ex)
    traceur.display_vars(
        variable, deeply=False, visualize=False, image_name="liste_doublement_chainee"
    )
    # END CORRECTION
    elements = ListeDoublementChainee()
    ajoute_en_tete(elements, 12)
    ajoute_en_tete(elements, 15)
    ajoute_en_tete(elements, 10)
    ajoute_en_queue(elements, 12)
    ajoute_en_queue(elements, 18)
    print("10, 15, 12, 12, 18 :", elements)
    print("inversées :", *recupere_cellules_inversees(elements))
    print("entiers proches :", recupere_entiers_proches(elements))
    print("entiers proches variante :", recupere_entiers_proches_bis(elements))
    impairs = ListeDoublementChainee()
    for valeur in [2 * v + 1 for v in range(5)]:
        ajoute_en_queue(impairs, valeur)
    pairs = ListeDoublementChainee()
    for valeur in [2 * v for v in range(5)]:
        ajoute_en_queue(pairs, valeur)
    print("entrelaçons :", impairs, "et", pairs)
    entrelace(impairs, pairs)
    print("entrelacées :", impairs)
    print("inversées :", *recupere_cellules_inversees(impairs))
    impairs = ListeDoublementChainee()
    for valeur in [2 * v + 1 for v in range(5)]:
        ajoute_en_queue(impairs, valeur)
    pairs = ListeDoublementChainee()
    for valeur in [2 * v for v in range(7)]:
        ajoute_en_queue(pairs, valeur)
    print("entrelaçons :", impairs, "et", pairs)
    entrelace(impairs, pairs)
    print("entrelacées :", impairs)
    print("inversées :", *recupere_cellules_inversees(impairs))
    impairs = ListeDoublementChainee()
    for valeur in [2 * v + 1 for v in range(5)]:
        ajoute_en_queue(impairs, valeur)
    pairs = ListeDoublementChainee()
    for valeur in [2 * v for v in range(7)]:
        ajoute_en_queue(pairs, valeur)
    print("entrelaçons :", pairs, "et", impairs)
    entrelace(pairs, impairs)
    print("entrelacées :", pairs)
    print("inversées :", *recupere_cellules_inversees(pairs))
    enleve_cellule(pairs, recherche(pairs, 4))
    print("on enlève 4 :", pairs)
    print("inversées :", *recupere_cellules_inversees(pairs))
    print("on teste maintenant la suppression des doublons")
    doublons = ListeDoublementChainee()
    for valeur in (1, 3, 1, 2, 1, 4, 5, 3, 2, 6, 2):
        ajoute_en_queue(doublons, valeur)
    print("avant :", doublons)
    supprime_doublons(doublons)
    print("après :", doublons)
    print("inversées :", *recupere_cellules_inversees(doublons))


if __name__ == "__main__":
    teste_listes()
