## Description du problème

On s'intéresse à la programmation d'une structure abstraite permettant de stocker un ensemble de ressources.
Chaque ressource est unique et identifiable par un entier compris entre `0` et le nombre total de ressources `- 1`.
On ne stocke dans cet exercice que ces identifiants entiers.

Afin de stocker les ressources, on pourrait utiliser un `set`  de Python.
Si nous utilisions cette structure de donnée, alors if faudrait stocker toutes les  ressources.
Afin de diminuer les besoins de stockage, on se propose donc  de  programmer nous même  une  structure de donnée,  en réalisant  une compression des données  stockées par  plages  contiguës.
On utilisera pour ce faire un tableau dynamique d'intervalles.
Chaque intervalle sera lui-même représenté par un tableau de deux éléments :

- l'identifiant de la première ressource de l'intervalle.
- l'identifiant suivant l'identifiant de la dernière ressource de l'intervalle.

Par exemple, l'ensemble de ressources `0, 1, 3, 5, 6, 9, 10, 11, 12` sera représenté par les quatre intervalles `[0,2], [3,4], [5,7], [9, 13]`.
Inversement les intervalles `[1,3], [5,7], [8,10]` représentent l'ensemble de ressources `1, 2, 5, 6, 8, 9`.

## Travail demandé

Pour manipuler un ensemble de ressources, nous utiliserons :

- une structure `namedtuple` contenant une liste d'intervalles ainsi que le nombre total de ressources que l'ensemble peut contenir ;
- un ensemble de fonctions opérant sur cette structure.

Le squelette du code que vous devez réaliser est affiché ci-dessous et [disponible ici](ressources.py) :

```python
#!/usr/bin/env python3
"""Manipulations complexes de tableaux dynamiques : listes d'intervalles"""

from collections import namedtuple

# Un ensemble de ressource est représenté par un intervalle et le nombre total
# de ressources qu'il peut contenir.
# Concernant la façon de définir les attributs de notre namedtuple,
# le code ci-dessous est correct car la documentation de la fonction
# collections.namedtuple dit :
#   "The field_names are a sequence of strings such as ['x', 'y'].
#     Alternatively, field_names can be a single string with each
#     fieldname separated by whitespace **and/or** commas,
#     for example 'x y' or 'x, y'."
EnsembleRessources = namedtuple("EnsembleRessources", "intervalles, nb_ressources")


def cree_ensemble_ressource(nb_ressources):
    """Créé un ensemble de ressources de taille nb_ressources.

    L'ensemble est représenté par un namedtuple EnsembleRessources.

    L'ensemble créé contient toutes les ressources avec un identifiant id
    tel que 0 <= id < nb_ressources.
    """
    # TODO
    ...


def contient(ensemble_ressources, identifiant):
    """Test d'appartenance d'une ressource à un ensemble.

    Renvoie True si la ressource identifiée par l'identifiant donné
    est contenu dans ensemble_ressources et False sinon.
    """
    # TODO
    ...


def get_chaine(ensemble_ressources):
    """Renvoie une chaîne de caractère représentant l'ensemble donné".

    Par exemple, '|x..xxxxx..|' indique qu'il y a 10 ressources,
    et que les ressources 0, 3, 4, 5, 6 et 7 sont contenues dans l'ensemble.
    """
    # TODO
    ...


def ajoute(ensemble_ressources, ensemble_ressources_a_ajouter):
    """Ajoute des ressources précédemment enlevées dans un ensemble.

    Ajoute toutes les ressources de ensemble_ressources_a_ajouter dans
    l'ensemble ensemble_ressources.

    Le fait que les ressources ajoutées aient été précédemment enlevées
    implique qu'aucune des ressources à ajouter ne soit déjà présente dans
    ensemble_ressources.

    Enfin, les deux ensembles de ressources ont le même nb_ressources et les
    tableaux dynamiques d'intervalles de ces deux ressources sont triés.
    """
    # TODO
    ...


def enleve(ensemble_ressources, nb_ressources):
    """Enlève nb_ressources de l'ensemble donnée.

    Les ressources enlevées sont les nb_ressources *premières ressources* de
    l'ensemble donné.

    Cette fonction *doit renvoyer* un nouvel ensemble de ressources de même
    taille que l'ensemble donné contenant uniquement les ressources qui ont
    été enlevées.
    """
    # TODO
    ...


def test():
    """On teste en gruyerisant un ensemble de ressources"""
    ressources_disponibles = cree_ensemble_ressource(10)
    print(
        "Disponibles après création d'un ensemble à 10 éléments     :",
        get_chaine(ressources_disponibles),
    )
    ressources_reservees = [enleve(ressources_disponibles, c) for c in (2, 2, 3, 2, 1)]
    print(
        "Disponibles après 5 appels à enlève pour un total de 10    :",
        get_chaine(ressources_disponibles),
    )
    ajoute(ressources_disponibles, ressources_reservees[1])
    print(
        "Disponibles après appel à ajout avec ressources 2 et 3     :",
        get_chaine(ressources_disponibles),
    )
    ajoute(ressources_disponibles, ressources_reservees[3])
    print(
        "Disponibles après appel à ajout avec ressources 7 et 8     :",
        get_chaine(ressources_disponibles),
    )
    print(
        "Reservees renvoyées par appel à enlève 3 sur disponibles   :",
        get_chaine(enleve(ressources_disponibles, 3)),
    )
    print(
        "Disponibles après le même appel à enlève 3                 :",
        get_chaine(ressources_disponibles),
    )
    print(
        "Les intervalles de disponibles avec uniquement ressource 8 :",
        ressources_disponibles.intervalles,
    )


if __name__ == "__main__":
    test()
```

La spécification de chacune des fonctions est donnée directement dans le squelette de code en tant que `docstring`.
Prenez donc le temps de lire cette documentation et d'analyser la fonction `test` pour bien comprendre ce que chacune des fonctions doit faire.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
#!/usr/bin/env python3
"""Manipulations complexes de tableaux dynamiques : listes d'intervalles"""

from collections import namedtuple

# Un ensemble de ressource est représenté par un intervalle et le nombre total
# de ressources qu'il peut contenir.
# Concernant la façon de définir les attributs de notre namedtuple,
# le code ci-dessous est correct car la documentation de la fonction
# collections.namedtuple dit :
#   "The field_names are a sequence of strings such as ['x', 'y'].
#     Alternatively, field_names can be a single string with each
#     fieldname separated by whitespace **and/or** commas,
#     for example 'x y' or 'x, y'."
EnsembleRessources = namedtuple("EnsembleRessources", "intervalles, nb_ressources")


def cree_ensemble_ressource(nb_ressources):
    """Créé un ensemble de ressources de taille nb_ressources.

    L'ensemble est représenté par un namedtuple EnsembleRessources.

    L'ensemble créé contient toutes les ressources avec un identifiant id
    tel que 0 <= id < nb_ressources.
    """
    # Un seul intervalle suffit à représenter nb_ressources contiguës
    return EnsembleRessources([[0, nb_ressources]], nb_ressources)


def contient(ensemble_ressources, identifiant):
    """Test d'appartenance d'une ressource à un ensemble.

    Renvoie True si la ressource identifiée par l'identifiant donné
    est contenu dans ensemble_ressources et False sinon.
    """

    # Il suffit de parcourir les intervalles et tester l'appartenance
    # Complexité calcul = O(len(ensemble_ressources.intervalles))
    for intervalle in ensemble_ressources.intervalles:
        if intervalle[0] <= identifiant < intervalle[1]:
            return True
    return False


def get_chaine(ensemble_ressources):
    """Renvoie une chaîne de caractère représentant l'ensemble donné".

    Par exemple, '|x..xxxxx..|' indique qu'il y a 10 ressources,
    et que les ressources 0, 3, 4, 5, 6 et 7 sont contenues dans l'ensemble.
    """

    # On parcourt tous les intervalles
    indice_courant = 0
    chaine = "|"
    for intervalle in ensemble_ressources.intervalles:
        debut, fin = intervalle
        chaine += "." * (debut - indice_courant)  # Ressources NON CONTENUES
        chaine += "x" * (fin - debut)  # Ressources CONTENUES
        indice_courant = fin

    # On rajoute les ressources NON CONTENUES de la fin
    chaine += "." * (ensemble_ressources.nb_ressources - indice_courant)
    chaine += "|"

    return chaine


def ajoute(ensemble_ressources, ensemble_ressources_a_ajouter):
    """Ajoute des ressources précédemment enlevées dans un ensemble.

    Ajoute toutes les ressources de ensemble_ressources_a_ajouter dans
    l'ensemble ensemble_ressources.

    Le fait que les ressources ajoutées aient été précédemment enlevées
    implique qu'aucune des ressources à ajouter ne soit déjà présente dans
    ensemble_ressources.

    Enfin, les deux ensembles de ressources ont le même nb_ressources et les
    tableaux dynamiques d'intervalles de ces deux ressources sont triés.
    """

    def recolle_intervalles_contigus(intervalles):
        """Fonction interne.

        Itère sur tous les intervalles et recolle toutes
        les plages contiguës pour réduire le nombre d'intervalles.
        """
        nouveaux_intervalles = []
        for intervalle in intervalles:
            if nouveaux_intervalles and nouveaux_intervalles[-1][1] == intervalle[0]:
                nouveaux_intervalles[-1][1] = intervalle[1]
            else:
                nouveaux_intervalles.append(intervalle)

        return nouveaux_intervalles

    # On va fusionner les deux tableaux dynamiques d'intervalles
    # qui sont triés en utilisant l'algorithme de fusion vu en TD.
    # Coût fusion = O(len(ensemble_ressources.intervalles) +
    #                 len(ensemble_ressources_a_ajouter.intervalles))
    intervalles_fusionnes = []
    indice_ensemble = 0
    indice_ensemble_a_ajouter = 0
    while indice_ensemble < len(
        ensemble_ressources.intervalles
    ) and indice_ensemble_a_ajouter < len(ensemble_ressources_a_ajouter.intervalles):

        # On chercher le "plus petit" intervalle, c'est à dire celui
        # qui commence avec la plus petite ressource.
        if (
            ensemble_ressources.intervalles[indice_ensemble][0]
            < ensemble_ressources_a_ajouter.intervalles[indice_ensemble_a_ajouter][0]
        ):
            intervalle_min = ensemble_ressources.intervalles[indice_ensemble]
            indice_ensemble += 1
        else:
            intervalle_min = ensemble_ressources_a_ajouter.intervalles[
                indice_ensemble_a_ajouter
            ]
            indice_ensemble_a_ajouter += 1

        # On ajoute le plus petit intervalle dans le tableau dynamique fusionné.
        intervalles_fusionnes.append(intervalle_min)

    # Quand on sort de la boucle, il faut recopier les éléments du plus grand
    # des deux tableaux dynamiques.
    if indice_ensemble == len(ensemble_ressources.intervalles):
        indice_reste = indice_ensemble_a_ajouter
        tab_dyn_reste = ensemble_ressources_a_ajouter.intervalles
    else:
        indice_reste = indice_ensemble
        tab_dyn_reste = ensemble_ressources.intervalles
    for i in range(indice_reste, len(tab_dyn_reste)):
        intervalles_fusionnes.append(tab_dyn_reste[i])

    # On recolle les intervalles qui se touchent.
    # Coût = O(len(intervalles_fusionnes))
    #      = O(len(ensemble_ressources.intervalles) +
    #          len(ensemble_ressources_a_ajouter.intervalles))
    intervalles_fusionnes_recolles = recolle_intervalles_contigus(intervalles_fusionnes)

    # La fonction dit qu'il faut modifier l'ensemble donné en paramètres.
    # On ne doit donc pas renvoyer directement le tableau dynamique
    # d'intervalles fusionnés.
    # On ne peut pas non plus modifier l'attribut "intervalles" du namedtuple
    # passé en paramètre car celui-ci est immutable.
    # Il faut vider l'ancien tableau dynamique d'intervalles et le remplir avec
    # les intervalles fusionnés et recollés.

    # O(len(ensemble_ressources.intervalles)) en CPython pour gestion mémoire
    ensemble_ressources.intervalles.clear()

    # Coût = O(len(intervalles_fusionnes_recolles))
    #      = O(len(ensemble_ressources.intervalles) +
    #          len(ensemble_ressources_a_ajouter.intervalles))
    ensemble_ressources.intervalles.extend(intervalles_fusionnes_recolles)

    # Coût total = O(len(ensemble_ressources.intervalles) +
    #                len(ensemble_ressources_a_ajouter.intervalles))



def enleve(ensemble_ressources, nb_ressources):
    """Enlève nb_ressources de l'ensemble donnée.

    Les ressources enlevées sont les nb_ressources *premières ressources* de
    l'ensemble donné.

    Cette fonction *doit renvoyer* un nouvel ensemble de ressources de même
    taille que l'ensemble donné contenant uniquement les ressources qui ont
    été enlevées.
    """

    # La spécification demande explicitement d'enlever les premières
    # ressources pour discuter de complexité.
    # Autrement dit la spécification demande de "manger" un tableau
    # dynamique du mauvais côté, c'est à dire au début.
    # En effet, on pourrait faire du pop(0) sur la liste d'intervalles
    # en entrée, mais ça ferait du O(len(ensemble_ressources.intervalles))
    # au total au pire cas.
    # Dans le code suivant, pop(0) n'est donc pas utilisé, ni pop
    # tout cours d'ailleurs.

    # On parcours l'ensemble donné pour savoir quels sont les
    # intervalles à enlever.
    # O(len(ensemble_ressources.intervalles))
    nb_ressources_allouees = 0
    intervalles_alloues = []
    for indice, intervalle in enumerate(ensemble_ressources.intervalles):
        taille = intervalle[1] - intervalle[0]
        # On s'arrête dès qu'on a alloué assez de ressources
        if nb_ressources_allouees + taille >= nb_ressources:
            manque = nb_ressources - nb_ressources_allouees
            coupe = indice
            break
        nb_ressources_allouees += taille
        intervalles_alloues.append(intervalle)

    # On copie les intervalles alloués, tous au début du tableau dynamique
    # Ici on a la version pythonique avec un tranchage, mais on peut
    # très bien avoir une boucle avec du append(), c'est "pareil".
    # O(len(ensemble_ressources.intervalles))
    intervalles_alloues = ensemble_ressources.intervalles[:coupe]

    # L'intervalle situé juste à la limite n'a pas
    # été ajouté aux intervalles alloués car il faut
    # le découper.
    # On le découpe et on l'ajoute ici
    # O(1)
    debut, fin = ensemble_ressources.intervalles[coupe]
    limite = debut + manque
    intervalles_alloues.append([debut, limite])

    # On rajoute si nécessaire aux intervalles restants le
    # deuxième morceau de l'intervalle situé juste à la limite.
    # O(1)
    intervalles_restants = []
    if limite != fin:
        intervalles_restants.append([limite, fin])

    # Puis on recolle tout ce qui reste
    # O(len(ensemble_ressources.intervalles))
    intervalles_restants.extend(ensemble_ressources.intervalles[coupe + 1 :])

    # La fonction dit qu'il faut modifier l'ensemble donné en paramètres.
    # On ne doit donc pas renvoyer directement le tableau dynamique
    # d'intervalles restants.
    # On ne peut pas non plus modifier l'attribut "intervalles" du namedtuple
    # passé en paramètre car celui-ci est immutables.
    # Il faut vider l'ancien tableau dynamique d'intervalles et le remplir avec
    # les intervalles restants.

    # O(len(ensemble_ressources.intervalles)) en CPython pour gestion mémoire
    ensemble_ressources.intervalles.clear()

    # O(len(intervalles_restants)) = O(len(ensemble_ressources.intervalles))
    ensemble_ressources.intervalles.extend(intervalles_restants)

    # Coût total = O(len(ensemble_ressources.intervalles))

    return EnsembleRessources(intervalles_alloues, ensemble_ressources.nb_ressources)


def test():
    """On teste en gruyerisant un ensemble de ressources"""
    ressources_disponibles = cree_ensemble_ressource(10)
    print(
        "Disponibles après création d'un ensemble à 10 éléments     :",
        get_chaine(ressources_disponibles),
    )
    ressources_reservees = [enleve(ressources_disponibles, c) for c in (2, 2, 3, 2, 1)]
    print(
        "Disponibles après 5 appels à enlève pour un total de 10    :",
        get_chaine(ressources_disponibles),
    )
    ajoute(ressources_disponibles, ressources_reservees[1])
    print(
        "Disponibles après appel à ajout avec ressources 2 et 3     :",
        get_chaine(ressources_disponibles),
    )
    ajoute(ressources_disponibles, ressources_reservees[3])
    print(
        "Disponibles après appel à ajout avec ressources 7 et 8     :",
        get_chaine(ressources_disponibles),
    )
    print(
        "Reservees renvoyées par appel à enlève 3 sur disponibles   :",
        get_chaine(enleve(ressources_disponibles, 3)),
    )
    print(
        "Disponibles après le même appel à enlève 3                 :",
        get_chaine(ressources_disponibles),
    )
    print(
        "Les intervalles de disponibles avec uniquement ressource 8 :",
        ressources_disponibles.intervalles,
    )


if __name__ == "__main__":
    test()
```
</details>

## Exercices

- [Tableaux](/2-iterations/travaux-pratiques/09-sous-suite/exercices/01-tableaux/index.html)
- [Boucles for](/2-iterations/travaux-pratiques/05-convertisseur/exercices/01-boucles-for/index.html)
- [Je m'en vais comme un prince !](/2-iterations/travaux-pratiques/optionnels/02-blobwars/exercices/01-je-m-en-vais-comme-un-prince/index.html)
