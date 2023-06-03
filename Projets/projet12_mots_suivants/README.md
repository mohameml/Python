## Description du problème

On souhaite effectuer une analyse sur les mots d'un texte.
Plus particulièrement, on se propose de savoir pour chaque mot `mi` d'un texte donné, quels sont les mots `mij` qui le suivent.
De plus, on souhaite associer à chaque couple de mots `(mi, mij)` un compteur `cij` représentant le nombre d’occurrences du couple `(mi, mij)` dans le texte.

Une fois ces données calculées, on utilise l'outil de visualisation de graphes `graphviz / dot` pour les représenter.

Par exemple, pour le texte suivant (Le serpent python, Charles Trenet) :

```console
c’est un serpent python
c’est un python serpent
qui se promene dans la foret
pour chercher a devorer
un beau petit lapin.
car le serpent python a faim
il a une faim sans fin !
mais betes et gens sont partis hier
loues par la Metro Goldwyn Mayer
pour figurer dans un film de Tarzan
qui doit rapporter beaucoup d’argent !
et le serpent piteux
est triste et se mord la queue
car il comprend, o desespoir
qu’il ne mangera pas ce soir.

soudain le bois s’eveille
arrivent des appareils
de prises de vues de prise de son
c’est la scene du grand frisson
on lache des animaux
des lions et des rhino-
ceros qu’ont l’air feroce comm’ tout
mais sont doux comme des toutous
notre serpent du haut d’une branche en l’air
voit monsieur Johnny Weissmuller
qui fait joujou avec un elephant
quel joli tableau pour les enfants.
mais tant de cinema
ne remplit pas l’estomac
du pauvre serpent qui n’aura pas
qui n’aura pas de repas.

quand une idee subtile
germe au coeur du reptile
profitant d’une repetition
voici qu’avec precaution
dans l’ombre du crepuscule
il avance il recule
puis happe un morceau minuscule
un morceau de pellicule
qui depassait d’une boite en fer
c’etait la grande scene du Val d’Enfer
tournee le matin dans une cloche a plongeur
pour mieux voir evoluer le nageur.
et comme un spaghetti
le python en appetit
avale deux cents metres a present
des aventures de Tarzan !

puis il s’en va joyeux
pensant : " c’est merveilleux
je vais dormir maintenant trois semaines
digerer ce film sans peine. "
rampant par-ci par-la
il s’enroule, oh la la,
autour d’un cocotier geant
mais soudain s’ecrie : " j’ai en...
j’ai envie de vomir c’est affreux, tu m’as
empoisonne, cinema
tarzan n’est pas pour les pauvres pythons
j’en ai mal jusqu’au bout des tetons. "
et la moralite
du serpent depite
c’est que parfois trop de cine parleur
peut vous donner mal au coeur
ou que les hommes digerent, dit-on,
mieux que les serpents pythons.
```

Le graphe obtenu est le suiant :

![graphe de "Le serpent python"](mots-suivants.png)

## Travail demandé

Comment stocker ces données ?

On utilise un dictionnaire `suivants`.
Chaque clef est un mot `mi`.
À chaque clef, il faut associer un ensemble de mots, chacun muni d’un compteur.
Pour ce faire, on utilise à nouveau un dictionnaire.
Chaque valeur du dictionnaire `suivants` est donc un dictionnaire dont les clefs sont les `mij` et les valeurs sont les `cij`.

On vous demande de compléter le fichier `mots_suivant.py` affiché ci-dessous et [disponible ici](mots_suivants.py) qui réalise la lecture d’un fichier, son analyse, l’affichage du graphe et enfin la génération d’une petite phrase en se déplaçant aléatoirement dans le graphe.

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


def get_mots(nom_fichier):
    """Renvoie un tableau dynamique sur tous les mots du fichier.

    Elimine au passage tout ce qui n'est pas une lettre.
    """
    mots = []
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            for mot in finditer("[a-zA-Z]+", ligne):
                mots.append(mot.group(0))
    return mots


def get_couples(tableau):
    """Renvoie un un tableau dynamique des couples.

    Le tableau dynamique renvoyé contient tous les couples d'elements
    successifs du tableau donné.
    """
    couples = []
    valeur_precedente = tableau[0]
    for valeur in tableau[1:]:
        couples.append((valeur_precedente, valeur))
        valeur_precedente = valeur
    return couples


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
    # TODO
    ...


def genere_graphe(suivants):
    """Genere le graphe dans les fichiers mots-suivants.dot et .png.

    Attention : il faut analyser des petits textes seulement car le
    layout du graph par l'outil dot peut vite coûter très cher en temps.
    """

    # On créer un fichier au format texte dot, utilisé pour
    # décrire un graphe.
    with open("mots-suivants.dot", "w") as fichier_dot:
        # TODO : écrire le graphe dans le fichier .dot
        ...

    # On utilise l'outil dot pour convertir le fichier .dot en image
    system("dot -Tpng mots-suivants.dot -o mots-suivants.png")


def get_suivant_aleatoire(mot, suivants):
    """Tire aléatoirement un suivant du mot donné.

    Le tirage aléatoire doit être pondéré par le nombre d'occurrences.
    Si le mot donne n'a pas de suivant, retourne un mot aléatoire.
    """
    # TODO
    ...


if __name__ == "__main__":
    analyse_texte()
```

En guise de documentation du format .dot, voici le fichier [mots-suivants.dot](mots-suivants.dot) généré pour notre exemple ci dessus.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
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


def get_mots(nom_fichier):
    """Renvoie un tableau dynamique sur tous les mots du fichier.

    Elimine au passage tout ce qui n'est pas une lettre.
    """
    mots = []
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            for mot in finditer("[a-zA-Z]+", ligne):
                mots.append(mot.group(0))
    return mots


def get_couples(tableau):
    """Renvoie un un tableau dynamique des couples.

    Le tableau dynamique renvoyé contient tous les couples d'elements
    successifs du tableau donné.
    """
    couples = []
    valeur_precedente = tableau[0]
    for valeur in tableau[1:]:
        couples.append((valeur_precedente, valeur))
        valeur_precedente = valeur
    return couples


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
    """Genere le graphe dans les fichiers mots-suivants.dot et .png.

    Attention : il faut analyser des petits textes seulement car le
    layout du graph par l'outil dot peut vite coûter très cher en temps.
    """

    # On créer un fichier au format texte dot, utilisé pour
    # décrire un graphe.
    with open("mots-suivants.dot", "w") as fichier_dot:
        # TODO : écrire le graphe dans le fichier .dot
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
    # If mot does not have suivant
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

- [Boucles for](/2-iterations/travaux-pratiques/05-convertisseur/exercices/01-boucles-for/index.html)
- [Le hasard fait bien les choses](/2-iterations/travaux-pratiques/06-images-pgm/exercices/01-le-hasard-fait-bien-les-choses/index.html)
- [Ligne de commandes et arguments](/2-iterations/travaux-pratiques/07-kaleidoscope/exercices/01-parametres-main/index.html)
- [Lecture de fichier](/2-iterations/travaux-pratiques/09-sous-suite/exercices/02-lecture-fichier/index.html)
- [Dictionnaires](/2-iterations/travaux-pratiques/13-mots-suivants/exercices/01-dico/index.html)
