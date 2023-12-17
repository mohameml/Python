# cour 07 : chaîne des caractères


## 1. Définition :

- **Définition:**

Les chaînes de caractères (`str`) sont des séquences de caractères délimitées par des guillemets simples (`'`) ou doubles (`"`). Elles sont utilisées pour représenter du texte et sont l'un des types de données fondamentaux en Python.


```python
chaine_simple = 'Ceci est une chaîne avec des guillemets simples.'
chaine_double = "Ceci est une chaîne avec des guillemets doubles."
```

Les deux formes sont équivalentes, et vous pouvez choisir celle qui convient le mieux à votre style de codage.


- **Chaînes Multilignes:***

En Python, une chaîne multiligne est une chaîne de caractères qui s'étend sur plusieurs lignes. Cela permet de définir une chaîne sur plusieurs lignes sans avoir à utiliser des caractères d'échappement tels que `\n` pour représenter des sauts de ligne.

La syntaxe pour créer une chaîne multiligne peut être réalisée de trois manières principales :

Utilisation de Triple Guillemets Simples (`'''`)

```python
chaine_multiligne = '''
Ceci est une chaîne
qui s'étend sur
plusieurs lignes.
'''
```

Utilisation de Triple Guillemets Doubles (`"""`)

```python
chaine_multiligne = """
Ceci est une chaîne
qui s'étend sur
plusieurs lignes.
"""
```

Utilisation de la Concaténation de Chaînes

```python
chaine_multiligne = (
    "Ceci est une chaîne "
    "qui s'étend sur "
    "plusieurs lignes."
)
```

Les chaînes multilignes sont souvent utilisées dans des situations où la lisibilité du code est primordiale, comme pour la documentation, les requêtes SQL, les expressions régulières complexes, etc.

```python
requete_sql = '''
SELECT *
FROM table
WHERE condition;
'''
```



- **Caracteres spéciaux :**

En Python, il existe plusieurs caractères spéciaux utilisés dans les chaînes de caractères pour représenter des caractères spéciaux ou effectuer des opérations particulières. Voici quelques-uns des caractères spéciaux couramment utilisés :

1. **`\n` :** Nouvelle ligne
   ```python
   texte = "Première ligne\nDeuxième ligne"
   ```

2. **`\t` :** Tabulation
   ```python
   texte = "Colonne1\tColonne2"
   ```

3. **`\r` :** Retour chariot
   ```python
   texte = "Ceci est une ligne.\rCeci est une autre ligne."
   ```

4. **`\\` :** Caractère d'échappement
   ```python
   chemin = "C:\\utilisateurs\\utilisateur\\documents"
   ```

5. **`\'` et `\"` :** Guillemets simples et doubles
   ```python
   texte_simple = 'C\'est une chaîne avec un apostrophe.'
   texte_double = "Ceci est une chaîne avec des guillemets \"doubles\"."
   ```

6. **`\uXXXX` et `\UXXXXXXXX` :** Caractères Unicode (UTF-16 et UTF-32)
   ```python
   unicode_utf16 = "\u03A9"  # Ω
   unicode_utf32 = "\U0001F602"  # 😂
   ```

7. **`r` devant une chaîne (`r"..."`) :** Chaîne brute (raw string)
   ```python
   chemin = r"C:\utilisateurs\utilisateur\documents"
   ```

   Dans une chaîne brute, les caractères d'échappement ne sont pas interprétés, ce qui est utile, par exemple, pour les expressions régulières.

Ces caractères spéciaux permettent d'inclure des sauts de ligne, des tabulations, des guillemets, etc., dans les chaînes de caractères sans altérer leur signification. La compréhension de ces caractères est essentielle lors de la manipulation de chaînes de caractères en Python.



#### RQ :

[site officielle unicode](https://unicode.org/charts/)


## 2.  **Accès aux éléments :** 

En Python, vous pouvez accéder aux caractères individuels d'une chaîne de caractères en utilisant l'index de chaque caractère. Les indices commencent à zéro pour le premier caractère de la chaîne. 


- **Accès par Index Positif :**

```python
texte = "Python"

# Accéder au premier caractère
premier_caractere = texte[0]  # 'P'

# Accéder au deuxième caractère
deuxieme_caractere = texte[1]  # 'y'

# Accéder au troisième caractère
troisieme_caractere = texte[2]  # 't'
```

- **Accès par Index Négatif (en partant de la fin) :**

```python
texte = "Python"

# Accéder au dernier caractère
dernier_caractere = texte[-1]  # 'n'

# Accéder à l'avant-dernier caractère
avant_dernier_caractere = texte[-2]  # 'o'
```


- **Accéder à une Tranche de Caractères (Slicing) :**

Vous pouvez également accéder à une sous-chaîne (tranche) de caractères en spécifiant une plage d'indices.

```python
texte = "Python"

# Extraire les trois premiers caractères
trois_premiers_caracteres = texte[0:3]  # 'Pyt'

# Extraire les caractères de l'index 2 à la fin
apres_deuxieme_caractere = texte[2:]  # 'thon'
```


- **Boucle pour Parcourir les Caractères :**

```python
texte = "Python"

# Parcourir les caractères de la chaîne
for caractere in texte:
    print(caractere)
```



## 3. **Opération:**


### 3.1 Concaténation :

La concaténation de deux chaînes se fait en utilisant l'opérateur `+`.

```python
chaine1 = "Bonjour"
chaine2 = " le monde"
concatenation = chaine1 + chaine2  # "Bonjour le monde"
```

### 3.2 Répétition :

La répétition d'une chaîne peut être effectuée en utilisant l'opérateur `*`.

```python
mot = "Python "
repetition = mot * 3  # "Python Python Python "
```

### 3.3 Longueur d'une Chaîne :

La longueur d'une chaîne (le nombre de caractères) peut être obtenue en utilisant la fonction `len()`.

```python
texte = "Hello, World!"
longueur = len(texte)  # 13
```





## 4. **Méthodes des chaîne des caractères:**

Les méthodes des chaînes de caractères en Python sont des fonctions intégrées qui vous permettent d'effectuer diverses opérations sur les chaînes. 

Voici quelques-unes des méthodes les plus couramment utilisées, avec des descriptions et des exemples :

### 1. `upper()`

**Description :** Convertit tous les caractères d'une chaîne en majuscules.

**Exemple :**
```python
texte = "Hello, World!"
majuscules = texte.upper()
# Résultat : "HELLO, WORLD!"
```

### 2. `lower()`

**Description :** Convertit tous les caractères d'une chaîne en minuscules.

**Exemple :**
```python
texte = "Hello, World!"
minuscules = texte.lower()
# Résultat : "hello, world!"
```

### 3. `capitalize()`

**Description :** Met en majuscule le premier caractère de la chaîne.

**Exemple :**
```python
texte = "hello, world!"
capitalise = texte.capitalize()
# Résultat : "Hello, world!"
```

### 4. `title()`

**Description :** Met en majuscule le premier caractère de chaque mot dans la chaîne.

**Exemple :**
```python
texte = "hello world"
titree = texte.title()
# Résultat : "Hello World"
```

### 5. `find(substring)`

**Description :** Recherche la première occurrence de la sous-chaîne donnée et renvoie l'index du début (ou -1 si non trouvé).

**Exemple :**
```python
texte = "Hello, World!"
position = texte.find("World")
# Résultat : 7
```

### 6. `replace(old, new)`

**Description :** Remplace toutes les occurrences de la sous-chaîne spécifiée par une nouvelle sous-chaîne.

**Exemple :**
```python
texte = "Hello, World!"
nouveau_texte = texte.replace("World", "Python")
# Résultat : "Hello, Python!"
```

### 7. `split(separator)`

**Description :** Divise la chaîne en une liste de sous-chaînes en fonction du séparateur spécifié.

**Exemple :**
```python
texte = "Bonjour, le monde"
mots = texte.split(", ")
# Résultat : ['Bonjour', 'le monde']
```

### 8. `strip()`

En Python, les méthodes `strip()`, `lstrip()`, et `rstrip()` sont utilisées pour supprimer les espaces (ou d'autres caractères spécifiés) des bords d'une chaîne de caractères. Voici comment elles fonctionnent :

- **`strip()`:**

    **Description :** Supprime les espaces (ou d'autres caractères spécifiés) au début et à la fin de la chaîne.

    **Exemple :**

        ```python
        texte = "   Bonjour, le monde   "
        nettoye = texte.strip()
        # Résultat : "Bonjour, le monde"
        ```

- **`lstrip()`:**
 
    **Description :** Supprime les espaces (ou d'autres caractères spécifiés) au début (à gauche) de la chaîne.


    **Exemple :**

    ```python
    texte = "   Bonjour, le monde   "
    nettoye_gauche = texte.lstrip()
    # Résultat : "Bonjour, le monde   "
    ```

- **`rstrip()`:**

    **Description :** Supprime les espaces (ou d'autres caractères spécifiés) à la fin (à droite) de la chaîne.
 
    **Exemple :**
    
    ```python
    texte = "   Bonjour, le monde   "
    nettoye_droite = texte.rstrip()
    # Résultat : "   Bonjour, le monde"
    
    ```

Dans ces exemples, la méthode `strip()` supprime tous les espaces au début et à la fin de la chaîne, `lstrip()` supprime uniquement les espaces à gauche, et `rstrip()` supprime uniquement les espaces à droite.


- **Spécifier les Caractères à Supprimer:**

Toutes ces méthodes acceptent en option un argument qui spécifie les caractères à supprimer. Par exemple, si vous voulez supprimer tous les points et les tirets de la chaîne, vous pouvez utiliser `strip(".-")`.

```python
texte = "--.Bonjour, le monde.--"
nettoye = texte.strip(".-")
# Résultat : "Bonjour, le monde"
```

Ces méthodes sont utiles pour nettoyer les chaînes d'entrée, par exemple, lors de la lecture de données d'un fichier ou de la saisie utilisateur, en éliminant les espaces inutiles qui pourraient causer des problèmes lors de la manipulation des données.

### 9. `join(iterable)`

La méthode `join()` en Python est une méthode de chaîne (`str`) qui permet de concaténer (joindre) les éléments d'un itérable (comme une liste) en une seule chaîne de caractères. Cette méthode prend une séquence d'éléments comme argument et renvoie une nouvelle chaîne qui est la concaténation de ces éléments, séparés par la chaîne sur laquelle la méthode est appelée.

- **Syntaxe :**

```python
chaîne_de_jointure.join(iterable)
```

- `chaîne_de_jointure` : La chaîne qui sera utilisée comme séparateur entre les éléments de l'itérable.
- `iterable` : L'itérable (par exemple, une liste ) dont les éléments sont des ``str`` (Attention ).

- **Exemple :**

```python
mots = ["Bonjour", "le", "monde"]
chaîne_jointe = " ".join(mots)
# Résultat : "Bonjour le monde"
```

Dans cet exemple, les mots de la liste `mots` sont joints en une seule chaîne de caractères en utilisant l'espace comme séparateur.

- **Utilisation avec d'autres types d'itérables :**

La méthode `join()` peut être utilisée avec n'importe quel itérable, pas seulement avec des listes. Par exemple, avec un générateur d'éléments :

```python
nombres = (str(x) for x in range(5))
chaîne_nombres = "-".join(nombres)
# Résultat : "0-1-2-3-4"
```

La méthode `join()` est utile pour construire des chaînes à partir d'éléments d'une liste ou d'un autre itérable de manière efficace. Elle est souvent utilisée en combinaison avec la compréhension de liste ou d'autres méthodes de génération d'itérables.

### 10. `count(substring)`

**Description :** Compte le nombre d'occurrences de la sous-chaîne donnée dans la chaîne.

**Exemple :**
```python
texte = "Hello, World! Hello, Python!"
occurrences = texte.count("Hello")
# Résultat : 2
```


### 11. `startswith(prefix)`

**Description :** Vérifie si la chaîne commence par le préfixe spécifié.

**Exemple :**
```python
texte = "Bonjour, le monde"
commence_par_bonjour = texte.startswith("Bonjour")
# Résultat : True
```

### 12. `endswith(suffix)`

**Description :** Vérifie si la chaîne se termine par le suffixe spécifié.

**Exemple :**
```python
texte = "Bonjour, le monde"
se_termine_par_monde = texte.endswith("monde")
# Résultat : True
```

### 13. `isalpha()`

**Description :** Vérifie si tous les caractères de la chaîne sont alphabétiques (lettres).

**Exemple :**
```python
texte = "Python"
est_alphabetique = texte.isalpha()
# Résultat : True
```

### 14. `isdigit()`

**Description :** Vérifie si tous les caractères de la chaîne sont des chiffres.

**Exemple :**
```python
numerique = "12345"
est_numerique = numerique.isdigit()
# Résultat : True
```

### 15. `isalnum()`

**Description :** Vérifie si tous les caractères de la chaîne sont alphanumériques (lettres ou chiffres).

**Exemple :**
```python
texte_alphanumerique = "Python3"
est_alphanumerique = texte_alphanumerique.isalnum()
# Résultat : True
```




Ces exemples illustrent quelques-unes des méthodes de base des chaînes de caractères en Python. Il existe bien d'autres méthodes, chacune avec sa propre fonctionnalité. Vous pouvez consulter la documentation officielle de Python pour en savoir plus sur les méthodes de chaînes : [Documentation Python - Méthodes de Chaînes](https://docs.python.org/3/library/stdtypes.html#string-methods).





## 5. **Formatage de Chaînes:**


### 5.1 Utilisation de l'Opérateur `%`

```python
nom = "Doe"
age = 30
message = "Bonjour, je m'appelle %s et j'ai %d ans." % (nom, age)
```

### 5.2 Utilisation de la Méthode `format()`

```python
message_format = "Bonjour, je m'appelle {} et j'ai {} ans.".format(nom, age)
```

### 5.3 F-Strings (Disponibles à partir de Python 3.6)

```python
message_fstring = f"Bonjour, je m'appelle {nom} et j'ai {age} ans."
```




