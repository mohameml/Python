## Énoncé

On se propose de travailler sur des opérations de haut niveau sur les listes simplement chaînées réalisées précédemment dans le mini projet [Listes simplement chaînées](../../../15-listes-sc/mini-projets/01-listes-simplement-chainees/).
Vous **testerez** vos fonctions au fur et à mesure de vos développements sur les entrées qui vous semblent les plus pertinentes.
Mis à part le constructeur de la classe `ListeSimplementChainee` **aucune des fonctions ci-dessous ne doit créer de nouvelles cellules**.

Dans ce mini projet nous allons mettre en pratique les concepts d'itérateur, d'itérable et de fonction génératrice.
Pour rappel :

- **un itérable est une instance à partir de laquelle on peut récupérer un itérateur** et donc une instance sur laquelle on peut faire une boucle `for` ;
- **un itérateur est une instance à partir de laquelle on peut récupérer le prochain élément** ;
- **un itérateur est un itérable** ;
- **une fonction génératrice, aussi appelée générateur** renvoie un itérateur (donc un itérable d'après le point ci-dessus).

Travail demandé :

- Modifiez le constructeur `__init__` de la classe `ListeSimplementChainee` pour construire une liste simplement chaînée à partir d'un itérable.
  Par exemple `ListeSimplementChainee(range(1, 10))` doit construire une liste contenant tous les entiers entre 1 (inclus) et 9 (inclus).
- Implémentez un générateur `recupere_cellules(liste_chainee)` qui renvoie un itérateur sur toutes les cellules de la liste donnée.
- Implémentez une fonction `remplace_valeurs(liste_chainee, transforme)` qui remplace pour chaque cellule la valeur par la valeur renvoyée par l'appel de fonction `transforme(valeur)`.
- Étant donnée une fonction `filtre(valeur)` renvoyant un booléen, on souhaite récupérer un itérateur sur toutes les cellules de la liste simplement chaînée pour lesquelles `filtre(valeur)` renvoie `True`.
  Implémentez un générateur `filtre_cellules(liste_chainee, filtre)` renvoyant un tel itérateur.
  Votre générateur de filtrage devra lancer une exception si `filtre(valeur)` ne renvoie pas un booléen.
- Utilisez `filtre_cellules(liste_chainee, filtre)` pour implémenter une fonction `supprime_cellules(liste_chainee, filtre)` qui élimine de `liste_chainee` toutes les cellules pour lesquelles `filtre(valeur)` renvoie `False`.
- Implémentez une fonction `concatene(liste_chainee_1, liste_chainee_2)` rajoutant les cellules de `liste_chainee_2` à la fin de `liste_chainee_1`.
 `liste_chainee_2` doit devenir vide.

- Implémentez une fonction `decoupe(liste_chainee, fonction)` qui crée et retourne deux listes simplement chaînées décrites ci-dessous (attention : l'ordre des cellules dans chacune des deux listes simplement chaînées est conservé) :
    - une liste chaînée contient les cellules pour lesquelles la fonction `fonction` renvoie `True` ;
    - la seconde liste chaînée contient les autres cellules.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici le code de correction :

```python
#!/usr/bin/env python3

"""Opérations de haut niveau sur des listes simplement chaînées."""



class Cellule:
    """Une cellule d'une liste simplement chaînée."""

    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

    def __str__(self):
        """Renvoie la valeur en chaîne de caractères."""
        return str(self.valeur)


class ListeSimplementChainee:
    """Une liste simplement chaînée."""

    def __init__(self, valeurs):
        self.tete = None
        self.queue = None
        self.taille = 0

        # valeurs est un itérable, on peut donc
        # récupérer un itérateur pour le parcourir.
        valeurs_it = iter(valeurs)

        # On récupère la première valeur
        # si elle existe sinon on récupère
        # None
        valeur = next(valeurs_it, None)

        if valeur is not None:

            # Création d'une nouvelle cellule
            cell = Cellule(valeur)

            # Ajout en tête et en queue
            self.tete = cell
            self.queue = cell

            # Ne pas oublier de mettre la taille à jour
            self.taille += 1

            # On traite toutes les valeurs suivantes
            # de la même manière
            for valeur in valeurs_it:

                # Création d'une nouvelle cellule
                cell = Cellule(valeur)

                # Ajout en queue
                self.queue.suivant = cell
                self.queue = cell

                # Ne pas oublier de mettre la taille à jour
                self.taille += 1

    def __str__(self):
        """Renvoie taille = X, val1 --> val2 --> val3 ...

        On implémente cette méthode spéciale `__str__` pour
        pouvoir afficher nos listes simplement chaînées
        avec de simples appels à `print`.
        """

        # La liste chaînée vide
        if self.tete is None:
            return "liste chaînée vide"

        # On parcourt la liste chaînée pour
        # construire la chaîne de caractères
        cell = self.tete
        first = True
        res = "taille = " + str(self.taille) + ", "
        while cell is not None:
            if not first:
                res += " --> "
            first = False
            # Possible car __str__ est définie dans la
            # classe Cellule ci-dessus
            res += str(cell)
            cell = cell.suivant
        return res


def recupere_celllules(liste_chainee):
    """Renvoie un itérateur sur toutes les cellules."""
    cell = liste_chainee.tete
    while cell is not None:
        yield cell
        cell = cell.suivant


def remplace_valeurs(liste_chainee, transforme):
    """Remplace les valeurs des cellules en appliquant la fonction transforme."""

    # Ici on utilise le générateur pour parcourir la liste chaînée.
    # Il n'y a pas de surcoût en calcul ni en mémoire, et le code
    # de parcours de liste est découplé du code de transformation.
    cellules_it = recupere_celllules(liste_chainee)
    for cell in cellules_it:
        cell.valeur = transforme(cell.valeur)


def filtre_cellules(liste_chainee, filtre):
    """Renvoie un itérateur sur les cellules filtrées."""

    # On utilise encore le générateur pour parcourir la liste chaînée.
    cellules_it = recupere_celllules(liste_chainee)
    for cell in cellules_it:
        filtree = filtre(cell.valeur)
        if not isinstance(filtree, bool):
            raise TypeError("la fonction filtre a renvoyé autre chose qu'un booléen")
        if filtree:
            yield cell


def supprime_cellules(liste_chainee, filtre):
    """Supprime toutes les cellules de liste pour lesquelles le filtre renvoie False.

    Coût = O(n) avec n qui est la taille de la liste chainée.
    """

    # Là encore, on va utiliser notre générateur.
    # ATTENTION, il ne faut pas modifier la liste
    # chaînée pendant que nous utilisons l'itérateur
    # renvoyé par le générateur !
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

    # Les modifications sur la liste chaînée
    # sont faites à la fin.
    liste_chainee.tete = tete
    liste_chainee.queue = queue
    if liste_chainee.queue:
        liste_chainee.queue.suivant = None
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


def ajoute_en_queue(liste_chainee, valeur):
    """Ajoute une valeur dans une nouvelle cellule en queue.

    Coût = O(1) grâce au pointeur de queue.
    """
    cellule = Cellule(valeur)
    if liste_chainee.queue:
        liste_chainee.queue.suivant = cellule
    else:
        liste_chainee.tete = cellule
    liste_chainee.queue = cellule
    liste_chainee.taille += 1


def decoupe(liste_chainee, fonction):
    """Crée et retourne deux listes : les cellules ne validant pas la fonction et les autres.

    Coût = O(n) avec n qui est la taille de la liste chainée.
    """

    # On crée les deux nouvelles listes
    non = ListeSimplementChainee(range(0))
    oui = ListeSimplementChainee(range(0))

    # Là encore, on va utiliser notre générateur pour
    # rajouter chacune des cellules dans la bonne liste
    # en fonction du résultat de l'appel à la fonction
    # `fonction`
    for cellule in recupere_celllules(liste_chainee):
        if fonction(cellule.valeur):
            ajoute_en_queue(oui, cellule)
        else:
            ajoute_en_queue(non, cellule)

    # Il n'y a rien apres la fin de chacune des listes.
    # Il faut donc "casser" le suivant de la queue
    # pour chacune des deux listes.
    for liste in (non, oui):
        if liste.queue is not None:
            liste.queue.suivant = None
    return (non, oui)


def multiplie_par_deux(val):
    """Multiplie val par deux et renvoie le résultat"""
    return val * 2


def est_multiple_de_trois(val):
    """Renvoie True si val est multiple de 3, et False sinon"""
    return val % 3 == 0


def teste_fonctions():
    """Teste les fonctions ci-dessus"""

    # Teste le constructeur
    liste_chainee_vide = ListeSimplementChainee(range(1, 1))
    print("une liste vide :", liste_chainee_vide)
    liste_chainee = ListeSimplementChainee(range(42, 42 + 8))
    print("une liste à 7 éléments :", liste_chainee)

    # Teste la transformation
    remplace_valeurs(liste_chainee_vide, multiplie_par_deux)
    print(
        "une liste vide après remplacement des valeurs par multiplication par deux :",
        liste_chainee_vide,
    )
    remplace_valeurs(liste_chainee, multiplie_par_deux)
    print(
        "une liste à 7 éléments après remplacement des valeurs par multiplication par deux :",
        liste_chainee,
    )

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
    print(
        "supression des non-multiple de trois sur liste à 7 éléments :", liste_chainee
    )

    # On teste tous les cas "limites" pour la concaténation
    liste_chainee_1 = ListeSimplementChainee(range(0))
    liste_chainee_2 = ListeSimplementChainee(range(0))
    print(
        "résultat concaténation", liste_chainee_1, "avec", liste_chainee_2, ":", end=" "
    )
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(5))
    liste_chainee_2 = ListeSimplementChainee(range(0))
    print(
        "résultat concaténation", liste_chainee_1, "avec", liste_chainee_2, ":", end=" "
    )
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(0))
    liste_chainee_2 = ListeSimplementChainee(range(5))
    print(
        "résultat concaténation", liste_chainee_1, "avec", liste_chainee_2, ":", end=" "
    )
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)
    liste_chainee_1 = ListeSimplementChainee(range(5))
    liste_chainee_2 = ListeSimplementChainee(range(5))
    print(
        "résultat concaténation", liste_chainee_1, "avec", liste_chainee_2, ":", end=" "
    )
    concatene(liste_chainee_1, liste_chainee_2)
    print(liste_chainee_1, "et", liste_chainee_2)

    # Teste trie pairs / impairs
    # Ici on utilise des lambdas : c'est à dire
    # des fonctions anonyme créées directement
    # dans un appel de fonction.
    liste_chainee = ListeSimplementChainee(range(0))
    print("résultat découpe pairs/impairs sur", liste_chainee, ":", end=" ")
    impairs, pairs = decoupe(liste_chainee, lambda x: x % 2 == 0)
    print(pairs, "et", impairs)
    liste_chainee = ListeSimplementChainee(range(11))
    print("résultat découpe pairs/impairs sur", liste_chainee, ":", end=" ")
    impairs, pairs = decoupe(liste_chainee, lambda x: x % 2 == 0)
    print(pairs, "et", impairs)


if __name__ == "__main__":
    teste_fonctions()

```
</details>
## Exercices

- [Première classe](/3-references/travaux-pratiques/15-listes-sc/exercices/01-premiere-classe/index.html)
- [Débogage visuel](/3-references/travaux-pratiques/15-listes-sc/exercices/02-debogage-visuel/index.html)
- [Référence vers une fonction](/3-references/travaux-pratiques/17-op-listes-sc-yield/exercices/01-reference-vers-fonction/index.html)
- [Référence vers une fonction](/3-references/travaux-pratiques/17-op-listes-sc-yield/exercices/01-reference-vers-fonction/index.html)
