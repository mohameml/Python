## Énoncé

L'objectif de cet exercice est d'écrire notre première fonction.

Écrivez un programme `somme.py` qui demande deux entiers à l’utilisateur puis affiche leur somme à l’écran.

Vous factoriserez le code en définissant une fonction `demande_entier` qui :

- affiche un message à l’utilisateur lui demandant d'entrer un entier ;
- renvoie l'entier saisi par l'utilisateur.

**Exécutez votre programme** pour vous assurer de son bon fonctionnement.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici une proposition de correction pour le fichier `somme.py` :
```python
#!/usr/bin/env python3

"""Un programme avec une petite fonction"""


def demande_entier():
    """Demande gentiment un entier à l'utilisateur"""
    print("entrez un entier\n")
    str_saisie = input()  # input renvoie une chaîne de caractères
    return int(str_saisie)


def demande_entiers_et_affiche_somme():
    """Fonction de test et affichage du résultat"""
    # On fait un premier appel à la fonction demande_entier()
    # L'interpréteur saute donc à la ligne 8 ci-dessus
    # puis revient à la ligne 17 après avoir exécuté les
    # lignes, 8, 9 et 10.
    entier1 = demande_entier()

    # Idem pour le deuxième appel.
    entier2 = demande_entier()

    # On affiche le résultat
    somme = entier1 + entier2
    print("la somme vaut", somme)

demande_entiers_et_affiche_somme()
```
</details>

