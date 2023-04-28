## Énoncé

Dans un [exercice précédent](../../../../../1-bases/travaux-pratiques/02-module-svg-and-co/exercices/01-ecriture-fichier), nous avons  vu comment créer un fichier en Python avec la fonction `open`.
Vous l'avez sans doute remarqué, cette fonction permet également d'ouvrir un fichier pour le lire.

Écrivez, un programme `cat.py` qui affiche sur la sortie standard le contenu du fichier qui lui est passé en paramètre sur la ligne de commande.

Pourquoi avons nous choisi le nom `cat.py` ?

Comme toujours, **testez** votre programme.
Par exemple que doit-il afficher si on le lance en lui donnant lui-même comme argument ?

```console
[selvama@ensipc215]$ ./cat.py cat.py
```

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
`cat.py` :

```python
#!/usr/bin/env python3
"""Une version python de l'outil standard cat qui permet
d'afficher  sur la sortie standard le contenu d'un
fichier"""

import sys


def affiche_fichier(chemin_fichier):
    """Affiche le contenu du fichier donné en paramètre"""

    # On ouvre le fichier en lecture
    fichier = open(chemin_fichier, "r")

    # On parcours un fichier ligne par ligne.
    # Gardons à l'esprit que beaucoup de choses se cachent
    # derrière ces boucles. Autrement dit, ça va piquer un
    # peu au début quand on devra faire la même chose en C
    # au second semestre. Merci Python :)
    for ligne in fichier:
        print(ligne, end="")

    # N'oublions pas de fermer le fichier
    fichier.close()


# Le chemin du fichier à affiché est donné en argument sur
# la ligne de commande.
# On le récupère avec sys.argv en se rappelant que sys.arv[0]
# ne contient pas le premier argument mais le nom du programme
# lui même.
affiche_fichier(sys.argv[1])
```
</details>
