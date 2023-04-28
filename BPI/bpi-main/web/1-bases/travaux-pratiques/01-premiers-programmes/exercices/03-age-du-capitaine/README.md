## Énoncé

L'objectif de cet exercice est de découvrir comment demander à l'utilisateur de saisir une entrée et comment l'utiliser ensuite.

Écrivez un programme `age_du_capitaine.py` utilisant la fonction `input` pour demander à l’utilisateur de vous donner l'âge du capitaine.
Votre programme calculera ensuite l'âge qu'aura ce dernier en 2050 et l'affichera sur la sortie standard.

**Exécutez votre programme** pour vous assurer de son bon fonctionnement.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici une proposition de correction pour le fichier `age_du_capitaine.py` :
```python
#!/usr/bin/env python3

"""Un programme python pour illustrer la notion d'entrée en plus de la notion de sortie"""

# La fonction input attend que l'utilisateur "saisisse" une chaîne de caractères sur l'entrée standard
# L'entrée standard est par défaut le clavier
# La chaîne de caractères passée en argument à la fonction input est affichée sur la sortie standard
# Celle-ci permet d'indiquer à l'utilisateur ce qu'il doit saisir
saisie = input("quel est l'âge du capitaine ?\n")

# La fonction int permet de transformer, entre autre, une chaîne de caractères en un entier
age = int(saisie)

# Un calcul très savant
age_en_2050 = age + 2050 - 2020

# Affichage de la réponse
# Ici, on voit que la fonction print de python accepte un nombre arbitraire d'arguments
# Ceux-ci sont affichés sur la sortie standard en étant séparés par des espaces.
print("en 2050, le capitaine aura", age_en_2050, "ans")
```
</details>

