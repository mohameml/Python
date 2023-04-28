## Énoncé

Un étudiant stratège a obtenu les résultats suivants dans un cursus imaginaire :

- 17 en maths avec coefficient 9
- 15 en physique avec coefficient 6
- 4 en histoire ancienne de l'informatique avec coefficient 1

Écrivez un programme `moyenne.py` qui :

- enregistre chacune de ces notes à l'aide d'un tuple à deux éléments, représentant la note et son coefficient ;
- calcule et affiche la moyenne totale de l'étudiant en accédant aux éléments des tuples.

Enfin, comme l'histoire ancienne de l'informatique est un cours fondamental, essayez de modifier son coefficient **à la suite de votre programme**, c'est à dire après avoir déjà affecté la valeur `1` à ce coefficient.
    Que se passe-t-il ? Pourquoi ?

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

`moyenne.py` :

```python
#!/usr/bin/env python3

"""Exercice pour illustrer la notion de tuple python"""

# Declaration des résultats en utilisant des tuples
resultat_maths = (17, 9)
resultat_physique = (15, 6)
resultat_histoire_info = (4, 1)

# Calcule de la moyenne en utilisant les tuples.
# On accède au ième élément d'un tuple t à l'aide de t[i]
total = (resultat_maths[0] * resultat_maths[1] +
         resultat_physique[0] * resultat_physique[1] +
         resultat_histoire_info[0] * resultat_histoire_info[1])
moyenne = total / (resultat_maths[1] + resultat_physique[1] + resultat_histoire_info[1])
print("La moyenne de l'étudiant stratège est " + str(moyenne))

# On essaye de modifier le coefficient de l'histoire de l'info
resultat_histoire_info[1] = 12
```


Lorsque l'on exécute `moyenne.py`, on obtient le résultat suivant :

```console
La moyenne de l'étudiant stratège est 15.4375
Traceback (most recent call last):
  File "./moyenne.py", line 19, in <module>
    resultat_histoire_info[1] = 12
TypeError: 'tuple' object does not support item assignment
```

Il est **FONDAMENTAL** de prendre le temps de lire **TOUS** les messages d'erreurs.
Donc il faut que nous comprenions celui-ci.
L'interprète nous dit exactement quel est le problème, à savoir qu'à la ligne 19 de notre programme nous essayons d'affecter une valeur à un élément d'un tuple alors que ce n'est pas permis.

En effet, en python le type tuple est un type **immuable**. C'est-à-dire qu'une fois un tuple `t` défini, celui-ci ne va plus changer.
Il est donc toujours interdit de faire quelque chose comme `t[x] = ...`.
</details>
