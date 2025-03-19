# Cour :

Les fonctions **`map`**, **`filter`** et **`zip`** sont des fonctions très utiles en Python pour travailler avec des collections comme les listes ou les tuples de manière efficace et élégante.

---

## 1. `map()`

La fonction `map()` applique une fonction à chaque élément d'un **itérable** et retourne un **itérable** contenant les résultats.

### Syntaxe :

```python
map(function, iterable)
```

-   `function` : Fonction appliquée à chaque élément.
-   `iterable` : Une liste, un tuple, un range, etc.

### Exemples :

#### Appliquer une fonction sur chaque élément d'une liste :

```python
def carre(x):
    return x ** 2

nombres = [1, 2, 3, 4, 5]
resultat = map(carre, nombres)
print(list(resultat))  # [1, 4, 9, 16, 25]
```

#### Avec une `lambda` :

```python
nombres = [1, 2, 3, 4, 5]
resultat = map(lambda x: x ** 2, nombres)
print(list(resultat))  # [1, 4, 9, 16, 25]
```

#### Appliquer une fonction à plusieurs listes :

```python
a = [1, 2, 3]
b = [4, 5, 6]
somme = map(lambda x, y: x + y, a, b)
print(list(somme))  # [5, 7, 9]
```

---

## 2. `filter()`

La fonction `filter()` permet de **filtrer** les éléments d'un itérable en gardant uniquement ceux qui **respectent une condition**.

### Syntaxe :

```python
filter(function, iterable)
```

-   `function` : Une fonction qui retourne `True` ou `False`.
-   `iterable` : Une liste, un tuple, etc.

### Exemples :

#### Filtrer les nombres pairs :

```python
nombres = [1, 2, 3, 4, 5, 6]
pairs = filter(lambda x: x % 2 == 0, nombres)
print(list(pairs))  # [2, 4, 6]
```

#### Filtrer les mots de plus de 3 lettres :

```python
mots = ["chat", "chien", "rat", "souris"]
longs = filter(lambda mot: len(mot) > 3, mots)
print(list(longs))  # ['chat', 'chien', 'souris']
```

---

## 3. `zip()`

La fonction `zip()` permet d'**associer** les éléments de plusieurs itérables **en tuples**.

### Syntaxe :

```python
zip(iterable1, iterable2, ...)
```

-   Les éléments sont regroupés **par index**.
-   L'itération s'arrête au **plus petit iterable**.

### Exemples :

#### Associer deux listes :

```python
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
resultat = zip(noms, ages)
print(list(resultat))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

#### Convertir en dictionnaire :

```python
cles = ["nom", "age", "ville"]
valeurs = ["Alice", 25, "Paris"]
dictionnaire = dict(zip(cles, valeurs))
print(dictionnaire)  # {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
```

#### Avec trois listes :

```python
prenoms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
villes = ["Paris", "Lyon", "Marseille"]

resultat = zip(prenoms, ages, villes)
print(list(resultat))
# [('Alice', 25, 'Paris'), ('Bob', 30, 'Lyon'), ('Charlie', 35, 'Marseille')]
```

---

## Conclusion

| Fonction   | Utilité                                                      |
| ---------- | ------------------------------------------------------------ |
| `map()`    | Appliquer une fonction à chaque élément d'une liste.         |
| `filter()` | Garder uniquement les éléments qui respectent une condition. |
| `zip()`    | Associer plusieurs listes ensemble.                          |

Ces fonctions sont souvent utilisées avec les **lambda functions** pour un code plus concis et lisible. Elles permettent de **remplacer des boucles `for`** tout en gardant une approche **fonctionnelle et optimisée**.

Tu veux des exercices pratiques pour t’entraîner ? 🚀
