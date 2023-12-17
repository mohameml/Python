# cour 05 : Les Boucles 


## 1. La boucle `for` :

La boucle `for` en Python est utilisée pour itérer sur une séquence (comme une liste, un tuple, une chaîne de caractères, ou d'autres objets itérables) ou pour exécuter un ensemble d'instructions un certain nombre de fois. Voici la syntaxe générale de la boucle `for` en Python :

```python
for variable in sequence:
    # Bloc de code à exécuter à chaque itération
    # Utilisez la variable dans le bloc de code
```

- **`variable` :** Variable qui prend successivement chaque valeur de la séquence.
- **`sequence` :** Séquence sur laquelle itérer (liste, tuple, chaîne, etc.).


exemples d'utilisation de la boucle `for` :

- Itération sur une liste :

```python
fruits = ["pomme", "banane", "orange"]

for fruit in fruits:
    print(fruit)
```



- Itération sur les caractères d'une chaîne de caractères :

```python
word = "Python"

for char in word:
    print(char)
```


- **Boucle `for` avec une instruction `else` :**

La clause `else` d'une boucle `for` est exécutée lorsque la séquence est épuisée (la boucle s'est terminée normalement, pas avec un `break`).

```python
for i in range(3):
    print(i)
else:
    print("La boucle est terminée.")
```

La boucle `for` en Python est polyvalente et peut être utilisée dans de nombreux contextes pour itérer sur différentes structures de données ou pour effectuer des opérations répétitives.



## 2. la fonction ``range()`` :


La fonction `range()` en Python est utilisée pour générer une séquence d'entiers. Elle est couramment utilisée avec les boucles `for` pour itérer sur une séquence de nombres. La syntaxe de base de la fonction `range()` est la suivante :

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

- **`start` (facultatif) :** La valeur de départ de la séquence. Par défaut, c'est 0.
- **`stop` :** La valeur à laquelle la séquence s'arrête (exclue).
- **`step` (facultatif) :** L'incrément (pas) entre les nombres de la séquence. Par défaut, c'est 1.

Voici quelques exemples d'utilisation de la fonction `range()` :

### 2.1. Utilisation de `range()` avec une seule valeur (arrêt) :

```python
for i in range(5):
    print(i)
# Résultat : 0, 1, 2, 3, 4
```

### 2.2 Utilisation de `range()` avec une valeur de début et une valeur d'arrêt :

```python
for i in range(2, 8):
    print(i)
# Résultat : 2, 3, 4, 5, 6, 7
```

### 2.3. Utilisation de `range()` avec une valeur de début, une valeur d'arrêt et un pas :

```python
for i in range(1, 10, 2):
    print(i)
# Résultat : 1, 3, 5, 7, 9
```

### 2.4. Utilisation de `range()` pour générer une liste :

```python
numbers = list(range(5))
print(numbers)
# Résultat : [0, 1, 2, 3, 4]
```

### 2.5. Utilisation de `range()` à l'envers :

```python
for i in range(5, 0, -1):
    print(i)
# Résultat : 5, 4, 3, 2, 1
```

### Remarques importantes :

- La séquence générée par `range()` est semi-ouverte, c'est-à-dire que la valeur d'arrêt n'est pas incluse.
- Si vous n'indiquez qu'un seul argument à `range()`, il sera interprété comme la valeur d'arrêt.
- Si vous indiquez deux arguments, ils seront interprétés comme la valeur de début et la valeur d'arrêt.
- Si vous indiquez trois arguments, ils seront interprétés comme la valeur de début, la valeur d'arrêt, et le pas.

La fonction `range()` est un outil utile pour générer des séquences d'entiers dans diverses situations, en particulier dans le contexte des boucles `for`.



## 3. la fonction **`enumerate()`** :


La fonction `enumerate()` en Python est une fonction intégrée qui permet d'itérer sur une séquence tout en conservant une trace de l'indice actuel de l'élément. Elle renvoie un objet énumérant, qui est souvent utilisé dans les boucles `for`. La syntaxe de base de `enumerate()` est la suivante :

```python
enumerate(iterable, start=0)
```

- **`iterable` :** La séquence (liste, tuple, chaîne, etc.) que vous souhaitez énumérer.
- **`start` (facultatif) :** La valeur à partir de laquelle les indices commencent. Par défaut, c'est 0.

La fonction `enumerate()` renvoie un objet énumérant, où chaque élément est un tuple contenant un indice et la valeur correspondante de la séquence.

Voici comment vous pouvez utiliser `enumerate()` dans une boucle `for` :

```python
fruits = ["pomme", "banane", "orange"]

for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")
```

Output :
```
Index 0: pomme
Index 1: banane
Index 2: orange
```

Dans cet exemple, `enumerate(fruits)` renvoie une séquence d'objets tuples, où chaque tuple contient l'indice et la valeur correspondante de la liste `fruits`. La boucle `for` parcourt ensuite cette séquence et décompose chaque tuple en deux variables : `index` et `value`.

L'argument facultatif `start` spécifie la valeur à partir de laquelle les indices commencent. Si vous voulez que les indices commencent à 1 au lieu de 0, vous pouvez le spécifier comme suit :

```python
for index, value in enumerate(fruits, start=1):
    print(f"Index {index}: {value}")
```

Output :
```
Index 1: pomme
Index 2: banane
Index 3: orange
```

La fonction `enumerate()` est utile lorsque vous devez parcourir une séquence tout en conservant une trace de l'indice actuel.



## 4. la boucle while :

La boucle `while` en Python est utilisée pour répéter un bloc de code tant qu'une condition spécifiée reste vraie. Voici la syntaxe générale de la boucle `while` :

```python
while condition:
    # Bloc de code à exécuter tant que la condition est vraie
    # Assurez-vous qu'il y a une modification de la condition pour éviter une boucle infinie
```

Le bloc de code à l'intérieur de la boucle `while` sera répété tant que la condition est vraie. La condition est évaluée avant chaque itération.

Voici quelques exemples d'utilisation de la boucle `while` :

### 4.1. Exemple basique :

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Dans cet exemple, la boucle `while` s'exécutera tant que la variable `count` est inférieure à 5. À chaque itération, la valeur de `count` est imprimée, et la boucle continue jusqu'à ce que la condition ne soit plus vraie.

### 4.2. Utilisation de `break` pour sortir de la boucle :

```python
count = 0

while True:
    print(count)
    count += 1
    if count >= 5:
        break
```

Dans cet exemple, la boucle `while` s'exécute indéfiniment jusqu'à ce que `count` atteigne la valeur de 5. À ce moment, la déclaration `break` est utilisée pour sortir de la boucle.

### 4.3. Utilisation de `continue` pour passer à l'itération suivante :

```python
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
```

Dans cet exemple, la déclaration `continue` est utilisée pour passer à l'itération suivante lorsque `count` est égal à 3. Ainsi, le nombre 3 ne sera pas imprimé.

### 4.4. Utilisation de la boucle `else` avec `while` :

La clause `else` d'une boucle `while` est exécutée lorsque la condition devient fausse, à moins que la boucle n'ait été interrompue par `break`.

```python
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("La boucle est terminée.")
```

La déclaration `else` sera exécutée lorsque la condition de la boucle `while` devient fausse.

