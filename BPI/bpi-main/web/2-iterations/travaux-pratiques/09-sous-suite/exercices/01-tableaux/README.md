## Énoncé

On commence par rappeler la terminologie utilisée en BPI (TD4, c'est à dire premier TD du chapitre 2) :

- **type abstrait (abstract data type, ADT en anglais)** : ensemble d'opérations et ensemble de propriétés ;
- **structure de données** : mise en œuvre concrète d'un type abstrait ;
- **séquence de taille fixe** : type abstrait avec 2 opérations : `get(i)` et `set(i, v)` ;
- **tableau** : mise en œuvre du type abstrait séquence de taille fixe à l'aide d'un segment de mémoire contiguë. Pour rappel, les tableaux n'existent pas en Python. Les deux opérations `get(i)` et `set(i)` s'effectuent en temps constant : la ième case se trouve en partant du début du tableau et en ajoutant `i` fois la taille d'une case. Autrement dit, la taille du tableau n'intervient pas quand on cherche à savoir où se trouve la ième case.
- **séquence de taille variable** : type abstrait avec les deux opérations disponibles sur les séquences de taille fixe et des opérations d'insertion et de suppression ;
- **tableau dynamique** : mise en œuvre du type abstrait séquence de taille variable à l'aide d'un tableau ;
- **list** : tableau dynamique de Python ;

Pour créer une `list` (donc un **tableau dynamique**) en Python il suffit d'utiliser des crochets :

```console
>>> tab_dyn = [1, 2, 3]
```

Lancez l'interpréteur interactif, et faites des petits tests pour :

- créer une `list` ;
- accéder à un élément à partir d'un index ;
- ajouter un élément à la fin ;
- ajouter un élément au début ;
- supprimer un élément à la fin ;
- supprimer un élément au début.

Pensez à utiliser la commande `help` fournie par l'interpréteur interactif.
Par exemple `help(list.append)`.

Enfin, **quelle est la complexité en temps de chacun de ces tests ?**.
Autrement dit, quel est le nombre d'opérations nécessaires à chacune des opérations sur une `list` Python ?
**VOUS DEVEZ AVOIR COMPRIS ET CONNAÎTRE PAR CŒUR LA RÉPONSE À CETTE QUESTION !**

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

`tableaux.py` :

```python
#!/usr/bin/env python3
"""Premiers tests avec des tableaux dynamiques python"""

# Une list (sans le E), c'est à dire un tableau dynamique.
tab_dyn = [1, "super", "tableau dynamique", "python"]
print(tab_dyn)

# Un accès indexé, sachant que ça commence à zéro.
# Ça ne coûte pas cher car le tableau est contigu
# en mémoire.
# Autrement dit, complexité en temps = O(1)
elem = tab_dyn[2]
print(elem)

# Ajout à la fin
# Ça ne coûte pas cher car on colle juste le nouvel
# élément dans une place libre à la fin.
# Autrement dit, complexité en temps = O(1)
tab_dyn.append(41)
print(tab_dyn)

# Ajout au début.
# Ça coûte cher, faut bouger tout le monde vers la droite.
# Autrement dit, complexité en temps = O(n) avec n qui est
# la taille du tableau dynamique.
tab_dyn.insert(0, "je me suis incrusté en tête du tableau")
print(tab_dyn)

# Suppression à la fin.
# Ça ne coûte pas cher, on enlève juste le dernier élément.
# Autrement dit, complexité en temps = O(1)
tab_dyn.pop()
print(tab_dyn)

# Suppression au début.
# Ça coûte cher, faut bouger tout le monde vers la gauche.
# Autrement dit, complexité en temps = O(n) avec n qui est
# la taille du tableau dynamique.
tab_dyn.pop(0)
print(tab_dyn)
```
</details>
