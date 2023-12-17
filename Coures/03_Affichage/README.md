# cour 03 : Affichage 

## 1. la fonction **``print()``** :

La fonction `print()` en Python est utilisée pour afficher du texte ou des valeurs à la sortie standard, généralement sur la console. Elle est largement utilisée pour déboguer, afficher des résultats, ou simplement communiquer avec l'utilisateur. La syntaxe de base de la fonction `print()` est simple :


- **Syntaxe:**

    ```python
    print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    ```

    - **`value1, value2, ...` :** Les valeurs que vous souhaitez afficher, séparées par des virgules.

    - **`sep=' '` :** L'argument optionnel `sep` spécifie la chaîne de séparation entre les valeurs. Par défaut, il est défini sur un espace.

    - **`end='\n'` :** L'argument optionnel `end` spécifie la chaîne qui doit être ajoutée à la fin de la sortie. Par défaut, c'est un saut de ligne (`'\n'`).

    - **`file=sys.stdout` :** L'argument optionnel `file` spécifie l'objet fichier où l'on souhaite imprimer. Par défaut, il est défini sur la sortie standard (`sys.stdout`).
 
    - **`flush=False` :** L'argument optionnel `flush` est un booléen qui, s'il est défini sur `True`, force l'écriture des données dans le fichier, même si la mémoire tampon n'est pas pleine. Par défaut, il est défini sur `False`.


Exemples d'utilisation de `print()` :

```python
# Exemple basique
print("Hello, World!")

# Affichage de plusieurs valeurs avec séparateur personnalisé
x = 10
y = 20
print(x, y, sep=' | ')

# Changement de la fin de ligne
print("Cette ligne se termine par un point-virgule", end=';')

# Utilisation de la fonction flush pour forcer l'écriture immédiate
print("Contenu mis en mémoire tampon", flush=True)
```

## 2. formattage:


L'écriture formatée, également appelée formattage de chaînes, est une technique permettant d'insérer des valeurs dans une chaîne de caractères d'une manière structurée et contrôlée. Cela facilite la création de chaînes dynamiques en combinant des textes constants avec des valeurs variables. En Python, il existe plusieurs façons d'effectuer l'écriture formatée, dont les principales sont les suivantes :

### 2.1. **Utilisation des f-strings (Python 3.6 et versions ultérieures) :**

Les f-strings sont une manière plus concise et lisible d'effectuer l'écriture formatée en utilisant une syntaxe spécifique à Python. Vous pouvez incorporer des expressions Python directement dans la chaîne en utilisant la syntaxe `{expression}`.

```python
name = "Alice"
age = 30
formatted_string = f"Nom : {name}, Âge : {age}"
print(formatted_string)
# Sortie : "Nom : Alice, Âge : 30"
```

### 2.2. **Utilisation de la méthode `format()` :**

La méthode `format()` est une méthode des objets de type chaîne en Python. Elle permet d'insérer des valeurs dans une chaîne en utilisant des espaces réservés `{}`.

```python
name = "Alice"
age = 30
formatted_string = "Nom : {}, Âge : {}".format(name, age)
print(formatted_string)
# Sortie : "Nom : Alice, Âge : 30"
```

Vous pouvez également spécifier l'ordre des valeurs à l'intérieur des espaces réservés.

```python
formatted_string = "Âge : {1}, Nom : {0}".format(name, age)
print(formatted_string)
# Sortie : "Âge : 30, Nom : Alice"
```



### 2.3. **Utilisation de `%` (style de formatage ancien) :**

Bien que moins recommandé pour les versions plus récentes de Python, le style de formatage `%` est toujours pris en charge. Il fonctionne de manière similaire à la méthode `printf` en C.

```python
name = "Alice"
age = 30
formatted_string = "Nom : %s, Âge : %d" % (name, age)
print(formatted_string)
# Sortie : "Nom : Alice, Âge : 30"
```

Il est recommandé d'utiliser les f-strings pour l'écriture formatée dans les versions de Python 3.6 et ultérieures en raison de leur clarté, de leur lisibilité et de leur concision. Cependant, la méthode `format()` reste une option flexible et largement utilisée.

