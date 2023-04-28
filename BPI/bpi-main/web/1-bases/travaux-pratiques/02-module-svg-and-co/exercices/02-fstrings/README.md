## Énoncé

Dans cet exercice nous allons voir comment construire des chaînes de caractères à partir d'autres chaînes de caractères et de nombres en utilisant des `f-strings`.

Il existe d'autres méthodes que les `f-strings` permettant d'atteindre le même objectif, notamment la méthode `format` du type `str` que vous connaissez peut-être. Nous privilégierons néanmoins les `f-strings` (introduits en python 3.6) pour leur simplicité d'utilisation.

**Analysez** le programme python `fsrtings_ex.py` ci-dessous ainsi que le résultat de son exécution :

```python
#!/usr/bin/env python3

"""Illustration simple des f-strings."""


def teste_fstrings():
    """Utilisation de f-strings pour afficher un message."""
    prenom = "Alexia"
    age = 8
    message_a_afficher = f"{prenom} a {age} ans"
    print(message_a_afficher)


teste_fstrings()
```

```console
> ./fstrings_ex.py
Alexia a 8 ans
```

**Implémentez et testez** une fonction `convertit_point_en_chaine(x, y)` qui renvoie une chaîne de caractère représentant le point d'abscisse `x` et d'ordonnée `y`. `x` et `y` sont des `float`.

On utilisera une représentation utilisant des parenthèses.
Par exemple, le point d'abscisse `12.2` et d'ordonnée `3.3` est représenté par la chaîne de caractères `"(12.2, 3.3)"`.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```python
#!/usr/bin/env python3

"""Illustration simple des f-strings."""


def teste_fstrings():
    """Utilisation de f-strings pour afficher un message."""
    prenom = "Alexia"
    age = 8
    message_a_afficher = f"{prenom} a {age} ans"
    print(message_a_afficher)


teste_fstrings()
```
</details>
