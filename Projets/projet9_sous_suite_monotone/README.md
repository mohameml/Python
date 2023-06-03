## Objectifs

On souhaite effectuer une analyse sur un fichier texte contenant une suite de nombres.
Le fichier est composé de chiffres, d'espaces et de retours chariot.
On cherche à trouver quelle est la plus grande sous-suite monotone de termes consécutifs du fichier.

Votre programme devra en outre récupérer le nom du fichier à lire sur la ligne de commande à l’aide du module `sys`.

Par exemple dans le fichier [`suite1.txt`](suite1.txt), la plus grande sous-suite monotone de termes consécutifs est  : `[1, 2, 3, 4]`.
Dans le fichier [`suite2.txt`](suite2.txt), la plus grande sous-suite monotone de termes consécutifs est : `[1, 2, 4, 7, 9]`.
Enfin, dans le fichier [`suite3.txt`](suite3.txt), la plus grande sous-suite monotone de termes consécutifs est : `[90, 53, 53, 52, 30, 2, 1]`.

Réfléchissez à votre algorithme **sur le papier** avant de vous lancer dans le code.

On se propose d’arriver au résultat final en trois étapes.

## Étape 1

Écrire une première boucle qui parcourt tous les nombres du fichier.
Pour ce faire, on propose de lire le fichier ligne par ligne, en récupérant les nombres séparés par des espaces (à l'aide de `split`).
On fera attention à ne pas occuper de la mémoire pour rien. En particulier, **on s'interdit de stocker l'intégralité du contenu du fichier en mémoire**.
En pratique, on s'autorise à stocker simplement le contenu d'une ligne du fichier.
Pour le moment, les nombres sont simplement affichés sur la sortie standard.

## Étape 2

Écrire une fonction qui traite un nombre vis à vis d'une suite donnée :

```python
def traite_nombre(suite, type_suite, nombre):
    """Traite le nombre donné vis à vis de la suite donnée.

    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite a changé
    de sens.
    """
```

Par "type de suite", on entend ici que la suite est croissante, décroissante ou stationnaire.
On pourra ainsi s'appuyer sur des constantes globales (ou regarder comment déclarer un type énuméré en python, c'est l'occasion !) :

```python
# Différents types de suites
STATIONNAIRE = 0
CROISSANTE = 1
DECROISSANTE = -1
```

## Étape 3

Utiliser la fonction de l'étape précédente dans la boucle de l'étape numéro 1 pour trouver la plus grande sous-suite monotone ?

Quelle est la **complexité en temps** de votre programme ?

Quelle est la **complexité en mémoire** de votre programme ?

## Notes

Pour simplifier le problème vous pouvez éventuellement commencer en consommant les éléments au fur et à mesure (pas d'éléments communs entre les suites).

Si plusieurs suites ont la même taille maximale, vous pouvez renvoyer n'importe laquelle lors du calcul de la suite de taille maximale.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

Voici le code d'une correction possible :
```python
#!/usr/bin/env python3

"""Plus grande suite monotone dans un fichier."""
import sys

# Différents types de suites (je n'ai pas parlé d'enum en cours)
STATIONNAIRE = 0
CROISSANTE = 1
DECROISSANTE = -1


def compte_dernier(suite):
    """Compte le nombre de fois ou le dernier element est répété dans la suite."""
    dernier = suite[-1]
    compte = 0
    for element in reversed(suite):
        if element != dernier:
            return compte
        compte += 1
    return compte


def changement_sens(type_suite, dernier, nouvel_element):
    """Détecte si l'ajout du nouvel element est possible.

    L'ajout est testé avec le type de suite donné.
    """
    if type_suite == CROISSANTE:
        return dernier > nouvel_element
    return dernier < nouvel_element


def traite_nombre(suite, type_suite, nombre):
    """Traite le nombre donné vis à vis de la suite donnée.

    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite a changé
    de sens.
    """
    if suite:  # Si la suite n'est pas vide
        dernier = suite[-1]

        # On peut toujours ajouter un nombre à une suite stationnaire
        if type_suite == STATIONNAIRE:
            if dernier > nombre:
                nouveau_type_suite = DECROISSANTE
            elif dernier < nombre:
                nouveau_type_suite = CROISSANTE
            else:
                nouveau_type_suite = STATIONNAIRE
            return (True, nouveau_type_suite)

        # Sinon si la suite change de sens
        if changement_sens(type_suite, dernier, nombre):
            nouveau_type_suite = type_suite * -1  # on inverse le sens
            return (False, nouveau_type_suite)

        # Sinon la suite garde le même sens
        return (True, type_suite)

    # Une suite à 1 élément est stationnaire
    return (True, STATIONNAIRE)


def main():
    """Affiche la plus grande suite monotone du fichier donné."""
    if len(sys.argv) != 2:
        print("usage : ", sys.argv[0], "nom_fichier_nombres")
        sys.exit(1)

    plus_grande_suite_monotone = []
    suite_courante = []
    type_suite_courante = None

    # On parcours le fichier d'entrée
    # with est un mot clef spécifique à python
    # qui nous permet de ne pas nous soucier
    # de la fermeture d'un fichier lorsque
    # open est utilisé après le with. Autrement
    # dit, le fichier sera fermé automatiquement
    # dans tous les cas.
    with open(sys.argv[1], "r") as fichier:
        for ligne in fichier:
            nombres_dans_ligne = ligne.split()
            for nombre in nombres_dans_ligne:
                ajout_ok, nouveau_type_suite = traite_nombre(
                    suite_courante, type_suite_courante, nombre
                )

                # On rajoute le nombre à la suite courante si ok
                if ajout_ok:
                    suite_courante.append(nombre)
                    type_suite_courante = nouveau_type_suite

                # On démarre une nouvelle suite sinon
                else:
                    if len(suite_courante) > len(plus_grande_suite_monotone):
                        plus_grande_suite_monotone = suite_courante
                    suite_courante = [
                        suite_courante[-1] * compte_dernier(suite_courante)
                    ]
                    suite_courante.append(nombre)
                    type_suite_courante = nouveau_type_suite

    # Est-ce que la dernière suite est la plus grande ?
    if len(suite_courante) > len(plus_grande_suite_monotone):
        plus_grande_suite_monotone = suite_courante

    print("La plus grande sous suite monotone est", plus_grande_suite_monotone)


if __name__ == "__main__":
    main()
```
</details>

## Exercices

- [Tableaux](/2-iterations/travaux-pratiques/09-sous-suite/exercices/01-tableaux/index.html)
- [Boucles for](/2-iterations/travaux-pratiques/05-convertisseur/exercices/01-boucles-for/index.html)
- [Ligne de commandes et arguments](/2-iterations/travaux-pratiques/07-kaleidoscope/exercices/01-parametres-main/index.html)
- [Lecture de fichier](/2-iterations/travaux-pratiques/09-sous-suite/exercices/02-lecture-fichier/index.html)
