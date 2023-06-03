## Énoncé

[Dernière séance de TP BPI, déjà, snif](https://youtu.be/5nUBWPbJFAU) : le jeu du solitaire.

L'objectif de ce jeu est de vider le plateau de tous ses pions sauf un, et il existe différentes formes de plateau.
Pour réaliser un mouvement, on prend un pion qui saute au-dessus de l’un de ses voisins avant d’atterrir dans une case vide.
Pour plus d’informations sur le jeu, vous pouvez consulter [sa page wikipedia](https://fr.wikipedia.org/wiki/Solitaire_(casse-t%C3%AAte)).

Dans ce mini projet, le plateau de jeu sera triangle avec 15 cases, les pions seront représentés en blanc et le cases vides en noir comme l'illustre l'image ci-dessous :

![solitaire.png](solitaire.png)

Nous vous fournissons un programme [solitaire.py](solitaire.py) ainsi que le module [plateau.py](plateau.py) qui va avec dont on peut voir le code ci-dessous.

`solitaire.py`:

```python
#!/usr/bin/env python3


"""Jeu du solitaire."""


import subprocess
import sys
import plateau


def calcule_solution(plat):
    """Renvoie la suite des coups à jouer **à l'envers** pour gagner.

    Renvoie la suite des coups à jouer sous la forme d'une list, ordonnée
    à l'envers. Par exemple, après exécution de la ligne :

    coups = calcule_solution(plat)

    on aura coups[0] qui contient le **dernier** coup à jouer pour gagner,
    coups[1] l'avant-dernier, ..., et coups[-1] le **premier** coup à jouer
    à partir de l'état actuel du plateau plat.

    Renvoie None si on ne peut pas gagner.
    """
    # TODO
    ...


def demande_coup(plat):
    """Demande quel coup jouer à l'utilisateur."""
    try:

        # Demande la case à jouer
        print("tapez ^C pour arrêter et lancer la résolution")
        depart = int(input("ou alors \n  donnez une case de départ: "))
        if plat.cases[depart] == plateau.VIDE:
            print("  case de départ invalide")
            raise ValueError

        # Demande la case d'arrivée
        arrivee = int(input("  donnez une case d'arrivée: "))
        if plat.cases[arrivee] == plateau.PION:
            print("  case d'arrivée invalide")
            raise ValueError

        # On vérifie que le mouvement est valide, c'est à dire
        # qu'il y a un pion entre le départ et l'arrivée.
        # Le FAMEUX "for else" de Python : c'est QUOi CE TRUC ??
        for direction, milieu in enumerate(plateau.VOISINS[depart]):
            if milieu is not None:
                apres_milieu = plateau.VOISINS[milieu][direction]
                if apres_milieu is not None and apres_milieu == arrivee:
                    break
        else:
            print("  mouvement invalide")
            raise ValueError
        # Nous (mais pas pylint) savons qu'ici milieu est défini
        # pylint: disable=undefined-loop-variable
        if plat.cases[milieu] == plateau.VIDE:
            print("  mouvement invalide")
            raise ValueError
        return depart, milieu, arrivee

    # Ici on fait suivre l'exception
    except KeyboardInterrupt:
        raise

    # Ici on redemande à l'utilisateur car il
    # a joué un coup invalide.
    # pylint, laisse nous tranquille, on gère !
    except:  # pylint: disable=bare-except
        return demande_coup(plat)


def main():
    """Lance une partie de solitaire."""

    # On determine si on est dans terminology ou non
    # pour savoir comment afficher le plateau :
    # SVG ou textuel ?
    try:
        subprocess.check_call(["tycat"])
        in_terminology = True
    except subprocess.CalledProcessError:  # Si le programme n'a pas renvoyé zéro
        in_terminology = False
    except FileNotFoundError:  # Si le programme n'est pas trouvé dans le PATH
        in_terminology = False

    # On joue tant que ^C n'est pas tapé ou qu'on a pas gagné
    plat = plateau.Plateau()
    while not plateau.est_gagnant(plat):
        plateau.affiche(plat, in_terminology)
        try:
            coup = demande_coup(plat)
        except KeyboardInterrupt:  # sur ^C
            break
        print(f"on joue de {coup[0]} a {coup[2]}")
        plateau.joue_coup(plat, coup)

    # Si le joueur humain a gagné, on s'arrête
    if plateau.est_gagnant(plat):
        print("Gagné !!!")
        sys.exit(0)

    # Sinon on demande la solution pour finir à notre
    # intelligence artificielle (fallait le placer ce
    # terme dans le cours BPI quand même !)
    suite = calcule_solution(plat)
    print()
    if suite:
        print("suite de coups possible pour terminer :")
        for debut, _, arrivee in reversed(suite):
            print("(", debut, ", ", arrivee, ")", sep="", end=" ")
        sys.exit(0)
    else:
        print("pas moyen d'aller plus loin !!!")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

`plateau.py`:

```python
"""Le module avec ce qu'il faut pour représenter le plateau."""


from itertools import islice
import os


# pylint: disable = too-few-public-methods
class Plateau:
    """Un plateau est representé par ses pions.

    On utilise un tableau dynamique de 15 cases.
    Initialement il y a un pion dans toutes les
    cases sauf dans la case numéro 12.
    """

    def __init__(self):
        self.cases = [PION for _ in range(15)]
        self.cases[12] = VIDE
        self.numero_affichage = 0


# Pour rendre le code plus lisible
VIDE = 0
PION = 1

INDICES_TO_UNICODE_VIDE = (
    ["\u24FF"]
    + [chr(ord("\u278A") + i) for i in range(10)]
    + [chr(ord("\u24EB") + i) for i in range(5)]
)

INDICES_TO_UNICODE_PION = ["\u24EA"] + [chr(ord("\u2460") + i) for i in range(15)]

# On stocke une fois pour toutes les
# voisins de chacune des 15 cases du
# plateau.
VOISINS = [
    [1, 2, None, None, None, None],
    [3, 4, 2, 0, None, None],
    [4, 5, None, None, 0, 1],
    [6, 7, 4, 1, None, None],
    [7, 8, 5, 2, 1, 3],
    [8, 9, None, None, 2, 4],
    [10, 11, 7, 3, None, None],
    [11, 12, 8, 4, 3, 6],
    [12, 13, 9, 5, 4, 7],
    [13, 14, None, None, 5, 8],
    [None, None, 11, 6, None, None],
    [None, None, 12, 7, 6, 10],
    [None, None, 13, 8, 7, 11],
    [None, None, 14, 9, 8, 12],
    [None, None, None, None, 9, 13],
]


def affiche(plateau, in_terminology):
    """Affiche le plateau en texte ou dans terminology."""
    os.system("clear")

    if in_terminology:
        nom_fichier = f"/tmp/plateau-{plateau.numero_affichage}.svg"
        plateau.numero_affichage += 1
        with open(file=nom_fichier, mode="w", encoding="utf8") as svg:
            print("<svg width='600' height='600'>", file=svg)
            print("<rect width='600' height='600' fill='white'/>", file=svg)
            cases = iter(plateau.cases)
            for ligne in range(5):
                for colonne, contenu in enumerate(islice(cases, ligne + 1)):
                    _affiche_pion_terminology(svg, ligne, colonne, contenu)
            print("</svg>", file=svg)
        os.system(f"tycat {nom_fichier}")

    else:
        cases = iter(plateau.cases)
        for ligne in range(5):
            nb_empty_cases = 4 - ligne
            print(" " * nb_empty_cases, end="")
            for colonne, contenu in enumerate(islice(cases, ligne + 1)):
                _affiche_pion_texte(ligne, colonne, contenu)
            print()


def _affiche_pion_texte(ligne, colonne, contenu):
    indice = ligne * (ligne + 1) // 2 + colonne
    charac = (
        INDICES_TO_UNICODE_VIDE[indice]
        if contenu == VIDE
        else INDICES_TO_UNICODE_PION[indice]
    )
    print(charac, end=" ")


def _affiche_pion_terminology(fichier, ligne, colonne, contenu):
    """Affiche le pion ligne/colonne dans le fichier svg donné.

    On affiche en noir un emplacement vide et en blanc un pion.
    """
    # pylint: disable=invalid-name
    y = 100 + ligne * 100
    x = 300 + (colonne - ligne / 2) * 100
    fond, trait = ("white", "black") if contenu else ("black", "white")
    indice = ligne * (ligne + 1) // 2 + colonne
    print(
        f"<circle cx='{x}' cy='{y-10}' fill='{fond}' stroke='black' r='20'/>",
        file=fichier,
    )
    print(
        f"<text x='{x}' y='{y}' fill='{trait}' text-anchor='middle' "
        f"font-size='30'>{indice}</text>",
        file=fichier,
    )


def est_gagnant(plateau):
    """Renvoie True si le plateau ne contient qu'un pion et False sinon."""
    compte = 0
    for case in plateau.cases:
        if case == PION:
            compte += 1
            if compte == 2:
                return False
    return True


def joue_coup(plateau, coup):
    """Joue le coup valide donné en modifiant le plateau donné.

    Un coup est un triplet départ, milieu, arrivée.
    """
    depart, milieu, arrivee = coup
    plateau.cases[depart] = VIDE
    plateau.cases[milieu] = VIDE
    plateau.cases[arrivee] = PION


```

Dans un premier temps il est demandé de jouer avec le programme en le lançant et d'analyser le code.

Ensuite, il est demandé d'implémenter la fonction récursive `calcule_solution` dont la docstring est rappelée ci-dessous :

```python
def calcule_solution(plat):
    """Renvoie la suite des coups à jouer **à l'envers** pour gagner.

    Renvoie la suite des coups à jouer sous la forme d'une list, ordonnée
    à l'envers. Par exemple, après exécution de la ligne :

    coups = calcule_solution(plat)

    on aura coups[0] qui contient le **dernier** coup à jouer pour gagner,
    coups[1] l'avant-dernier, ..., et coups[-1] le **premier** coup à jouer
    à partir de l'état actuel du plateau plat.

    Renvoie None si on ne peut pas gagner.
    """
```

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici le code de correction :

`solitaire.py`:

```python
def calcule_solution(plat):
    """Renvoie la suite des coups à jouer **à l'envers** pour gagner.

    Renvoie la suite des coups à jouer sous la forme d'une list, ordonnée
    à l'envers. Par exemple, après exécution de la ligne :

    coups = calcule_solution(plat)

    on aura coups[0] qui contient le **dernier** coup à jouer pour gagner,
    coups[1] l'avant-dernier, ..., et coups[-1] le **premier** coup à jouer
    à partir de l'état actuel du plateau plat.

    Renvoie None si on ne peut pas gagner.
    """
    # Si le plateau est gagnant on renvoie la liste vide:
    if plateau.est_gagnant(plat):
        return []
    # Sinon on va essayer tous les coups possibles
    for coup in plateau.recupere_coups(plat):
        # on joue le coup (1)
        plateau.joue_coup(plat, coup)
        resultat = calcule_solution(plat)
        # on defait le coup joué en (1)
        plateau.defait_coup(plat, coup)
        if resultat is not None:
            resultat.append(coup)
            return resultat

    return None
```

`plateau.py`:

```python
def defait_coup(plateau, coup):
    """Défait le coup donné, qui peut etre défait en modifiant le plateau donné.

    Un coup est un triplet depart, milieu, arrivee.
    """
    depart, milieu, arrivee = coup
    plateau.cases[depart] = PION
    plateau.cases[milieu] = PION
    plateau.cases[arrivee] = VIDE


def recupere_coups(plateau):
    """Renvoie un itérateur sur tous les coups possibles."""
    for depart, _ in filter(lambda c: c[1] == PION, enumerate(plateau.cases)):
        for direction, milieu in enumerate(VOISINS[depart]):
            if milieu is not None and plateau.cases[milieu] == PION:
                arrivee = VOISINS[milieu][direction]
                if arrivee is not None and plateau.cases[arrivee] == VIDE:
                    yield depart, milieu, arrivee
```
</details>
## Exercices

- [Incrémente](/4-recursivite/travaux-pratiques/19-fractales/exercices/01-incremente/index.html)
- [Stack overflow](/4-recursivite/travaux-pratiques/19-fractales/exercices/02-stackoverflow/index.html)
