## Énoncé

L'objectif de ce mini-projet est de réimplémenter le TP [mots suivants](../../../../2-iterations/travaux-pratiques/mini-projets/09-mots-suivants) en utilisant des générateurs.

Quels sont les avantages ?
Quels sont ls inconvénients ?

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Avantages :
   - tout aussi lisible ;
   - pas besoin de tout créer en mémoire ;
   - très certainement plus performant, justement parce qu'on ne construit pas de `list`, non ?

Inconvénients :
   - aucun si l'on a conscience que c'est très difficile de faire la même chose dans d'autres langages impératifs.

Et voici le code de correction :

```python
#!/usr/bin/env python3
"""
On fait une analyse de texte pour dessiner le graphe des mots suivants.
Permet l'utilisation de dictionnaires et une imbrication de structures.
On se sert des donnees pour générer des phrases aléatoires.
"""
import sys
from re import finditer
from random import choice, random
from os import system

# En VRAI Python, il faut utiliser un générateur ici,
# plutôt que de créer un tableau dynamique qui contient
# tout en mémoire.
# C'est ce qu'on fait maintenant qu'on connaît :)
def get_mots(nom_fichier):
    """Renvoie un générateur sur tous les mots du fichier.

    Élimine au passage tout ce qui n'est pas une lettre.
    """
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            for mot in finditer("[a-zA-Z]+", ligne):
                yield mot.group(0)


# En VRAI python, il faut utiliser un générateur ici,
# plutôt que de créer un tableau dynamique qui contient
# tout en mémoire.
# C'est ce qu'on fait maintenant qu'on connaît :)
def get_couples(iterateur):
    """Renvoie un générateur sur tous les couples.

    Le générateur renvoyé contient tous les couples d'elements
    successifs de l'itérateur donne.
    """
    valeur_precedente = next(iterateur)
    for valeur in iterateur:
        yield valeur_precedente, valeur
        valeur_precedente = valeur


def analyse_texte():
    """Analyse le fichier donné en argument.

    L'analyse parcours les mots du fichier et dessine le graphe
    des mots suivants.

    Ensuite, une phrase aléatoire est générée à partir du dictionnaire
    des mots.
    """

    # Parcours
    if len(sys.argv) != 2:
        print("utilisation :", sys.argv[0], "fichier_texte")
        sys.exit(1)
    suivants = compte_mots_suivants(sys.argv[1])
    genere_graphe(suivants)

    # Génération d'une petite phrase aleatoire.
    mot_depart = choice(list(suivants.keys()))
    phrase = [mot_depart]
    for _ in range(10):
        phrase.append(get_suivant_aleatoire(phrase[-1], suivants))
    print(" ".join(phrase))


def compte_mots_suivants(nom_fichier):
    """Renvoie le dictionnaire des mots suivants.

    Renvoie un dictionnaire associant a chaque mot m1 du fichier
    un dictionnaire associant a chaque mot m2 suivant m1 dans le
    fichier le nombre de fois ou m2 apparait apres m1.
    """
    mots_suivants = {}
    mots = get_mots(nom_fichier)
    for last_mot, mot in get_couples(mots):
        # Insert last_mot in dictionary if needed
        if not last_mot in mots_suivants:
            dico = {}
            mots_suivants[last_mot] = dico
        else:
            dico = mots_suivants[last_mot]
        # Increment counter of last_mot followed by mot
        if not mot in dico:
            dico[mot] = 1
        else:
            dico[mot] += 1
    return mots_suivants


def genere_graphe(suivants):
    """Génère le graphe dans les fichiers mots-suivants.dot et .png.

    Attention : il faut analyser des petits textes seulement car le
    layout du graph par l'outil dot peut vite coûter très cher en temps
    de calcul.
    """

    # On créer un fichier au format texte dot, utilisé pour
    # décrire un graphe.
    with open("mots-suivants.dot", "w") as fichier_dot:
        fichier_dot.write("digraph {\n")
        for mot, mots_suivants in suivants.items():
            for suivant, count in mots_suivants.items():
                fichier_dot.write("{} -> {} [label = {}]\n".format(mot, suivant, count))
        fichier_dot.write("}")

    # On utilise l'outil dot pour convertir le fichier .dot en image
    system("dot -Tpng mots-suivants.dot -o mots-suivants.png")


def get_suivant_aleatoire(mot, suivants):
    """Tire aléatoirement un suivant du mot donné.

    Le tirage aléatoire doit être pondéré par le nombre d'occurrences.
    Si le mot donne n'a pas de suivant, retourne un mot aléatoire.
    """
    if not mot in suivants:
        return choice(list(suivants.keys()))
    # Create frequency table
    total_suivants = sum(suivants[mot].values())
    frequency_table = {}
    total = 0
    for suivant, count in suivants[mot].items():
        total += count / total_suivants
        frequency_table[total] = suivant
    # Randomly choose from table
    choic = random()
    last = 0
    for count, suivant in frequency_table.items():
        if choic >= last and choic < count:
            return suivant
        last = count
    assert False


if __name__ == "__main__":
    analyse_texte()
```
</details>
## Exercices

- [Débogage visuel](/3-references/travaux-pratiques/15-listes-sc/exercices/02-debogage-visuel/index.html)
- [Référence vers une fonction](/3-references/travaux-pratiques/17-op-listes-sc-yield/exercices/01-reference-vers-fonction/index.html)
