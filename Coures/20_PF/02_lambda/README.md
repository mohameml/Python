# Cour : **Les Fonctions Lambda en Python**

> Les **fonctions lambda** en Python sont des **fonctions anonymes** (sans nom) définies en une seule ligne. Elles sont souvent utilisées pour des opérations simples et concises.

---

## 📌 **1. Définition et Syntaxe**

Une **fonction lambda** est une **fonction anonyme** qui peut prendre plusieurs arguments mais ne peut contenir qu'une **seule expression**.

### 🔹 **Syntaxe Générale :**

```python
lambda arguments: expression
```

-   **`lambda`** : Mot-clé qui définit une fonction anonyme.
-   **`arguments`** : Liste des paramètres (comme dans une fonction `def`).
-   **`expression`** : Une seule ligne d'instruction qui est **évaluée et retournée** (pas d'instruction `return` nécessaire).

### ✅ **Exemple Simple :**

```python
carre = lambda x: x ** 2
print(carre(5))  # 25
```

🟢 **Explication :**

-   `lambda x: x ** 2` définit une fonction qui prend `x` et retourne `x²`.
-   `carre(5)` exécute la fonction et retourne `5² = 25`.

---

## 🎯 **2. Différence entre `lambda` et `def`**

Les **fonctions `lambda`** sont des **fonctions anonymes et concises**, tandis que **les fonctions `def`** permettent d'écrire du code plus structuré.

🔹 **Avec `def` :**

```python
def carre(x):
    return x ** 2
print(carre(5))  # 25
```

🔹 **Avec `lambda` :**

```python
carre = lambda x: x ** 2
print(carre(5))  # 25
```

| Critère                  | `lambda`                           | `def`                                   |
| ------------------------ | ---------------------------------- | --------------------------------------- |
| **Nom de fonction**      | Anonyme                            | Doit être nommé                         |
| **Nombre d'expressions** | Une seule ligne                    | Plusieurs instructions possibles        |
| **Lisibilité**           | Compacte, mais peut être illisible | Plus clair pour les fonctions complexes |
| **Utilisation**          | Simple et rapide                   | Fonctionnalités avancées                |

---

## 🎯 **3. Utilisation des `lambda` avec `map()`, `filter()` et `reduce()`**

Les **fonctions lambda** sont souvent utilisées avec des **fonctions d'ordre supérieur** comme `map()`, `filter()` et `reduce()`.

### ✅ **3.1 `map()` - Appliquer une fonction à une séquence**

```python
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x ** 2, nombres))
print(carres)  # [1, 4, 9, 16, 25]
```

🟢 **Explication** : `map()` applique la fonction `lambda x: x**2` à chaque élément de la liste.

---

### ✅ **3.2 `filter()` - Filtrer les éléments selon une condition**

```python
nombres = [1, 2, 3, 4, 5, 6]
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # [2, 4, 6]
```

🟢 **Explication** : `filter()` conserve uniquement les éléments où `x % 2 == 0`.

---

### ✅ **3.3 `reduce()` - Réduction d'une séquence en une seule valeur**

```python
from functools import reduce

nombres = [1, 2, 3, 4, 5]
somme = reduce(lambda x, y: x + y, nombres)
print(somme)  # 15
```

🟢 **Explication** : `reduce()` additionne les éléments successivement (`1+2=3`, `3+3=6`, etc.).

---

## 🎯 **4. Lambda avec le Tri (`sorted()`)**

Les **lambdas** sont utiles pour trier des listes avec `sorted()`.

### ✅ **4.1 Trier une liste de tuples**

```python
eleves = [("Alice", 20), ("Bob", 18), ("Charlie", 22)]
tri_par_age = sorted(eleves, key=lambda x: x[1])
print(tri_par_age)
# [('Bob', 18), ('Alice', 20), ('Charlie', 22)]
```

🟢 **Explication** : On trie la liste selon le **deuxième élément** de chaque tuple (l'âge).

---

### ✅ **4.2 Trier en ordre décroissant**

```python
nombres = [3, 1, 4, 2]
tri_inverse = sorted(nombres, key=lambda x: -x)
print(tri_inverse)  # [4, 3, 2, 1]
```

🟢 **Explication** : `-x` inverse l'ordre naturel du tri.

---

## 🎯 **5. Lambda avec `max()` et `min()`**

Les **fonctions lambda** peuvent être utilisées pour spécifier un critère dans `max()` et `min()`.

### ✅ **Trouver l'élément le plus long**

```python
mots = ["Python", "Lambda", "Programmation", "Code"]
mot_le_plus_long = max(mots, key=lambda x: len(x))
print(mot_le_plus_long)  # 'Programmation'
```

🟢 **Explication** : `max()` compare les mots selon leur **longueur**.

---

## 🎯 **6. Utilisation Avancée avec `functools.partial`**

On peut utiliser `lambda` pour **fixer certains paramètres** d'une fonction.

🔹 **Sans `lambda` :**

```python
def multiplier(x, y):
    return x * y

multiplier_par_2 = lambda y: multiplier(2, y)
print(multiplier_par_2(5))  # 10
```

🔹 **Avec `functools.partial` (plus propre) :**

```python
from functools import partial

multiplier_par_2 = partial(multiplier, 2)
print(multiplier_par_2(5))  # 10
```

🟢 **Explication** : `partial()` fixe `x=2`, donc `multiplier_par_2(y)` revient à `2 * y`.

---

## 🔥 **7. Avantages et Inconvénients des Lambdas**

### ✅ **Avantages :**

-   🏎 **Syntaxe courte et lisible** (surtout pour des fonctions simples).
-   ⚡ **Parfait pour les fonctions d'ordre supérieur** (`map()`, `filter()`, etc.).
-   📌 **Évite la déclaration de fonctions inutiles**.

### ❌ **Inconvénients :**

-   ❌ **Moins lisible si complexe** (ex. `lambda x: x[1] + x[2] if x[0] == 1 else x[1]`).
-   ❌ **Impossible d'écrire plusieurs instructions** (une seule expression autorisée).
-   ❌ **Pas de docstring** (contrairement aux `def`).

---

## 🚀 **8. Quand utiliser `lambda` ?**

✅ **À utiliser si :**

-   La fonction est **courte et simple**.
-   Elle est utilisée **une seule fois**.
-   Elle est **passée en argument** à une autre fonction (`map()`, `sorted()`, etc.).

❌ **À éviter si :**

-   La logique est **complexe** → utiliser `def`.
-   La fonction est **réutilisée plusieurs fois** → donner un nom avec `def`.

---

## 🚀 **Conclusion**

Les **fonctions lambda** sont un **outil puissant** pour écrire du code Python concis et élégant. Elles sont **particulièrement utiles** avec `map()`, `filter()`, `sorted()` et `reduce()`.

👉 **Besoin d'un exercice avancé avec `lambda` et la finance quantitative ou le machine learning ?** 🚀
