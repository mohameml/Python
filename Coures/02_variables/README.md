# cour 02 : Les Variables


## 1. Définition :

Une variable est une zone de la mémoire de l'ordinateur dans laquelle une valeur est stockée. Aux yeux du programmeur, cette variable est définie par un nom, alors que pour l'ordinateur, il s'agit en fait d'une adresse, c'est-à-dire d'une zone particulière de la mémoire.

En Python, la déclaration d'une variable et son initialisation (c'est-à-dire la première valeur que l'on va stocker dedans) se font en même temps

```python
a = 2 
print(a)
```

Ligne 1. Dans cet exemple, nous avons déclaré, puis initialisé la variable a avec la valeur 2.

 
- Python a « deviné » que la variable était un entier. On dit que Python est un langage au **``typage dynamique``**.

- Python a alloué (réservé) l'espace en mémoire pour y accueillir un entier. Chaque type de variable prend plus ou moins d'espace en mémoire, Python a aussi fait en sorte qu'on puisse retrouver la variable sous le nom x 

- Enfin, Python a assigné la valeur 2 à la variable x .


Dans d'autres langages (en C par exemple), il faut coder ces différentes étapes une par une. Python étant un langage dit de **``haut niveau``**, la simple instruction x = 2 a suffi à réaliser les 3 étapes en une fois !


## 2. Les types de variables :

En Python, les variables n'ont pas besoin d'être explicitement déclarées avec un type spécifique. Le type d'une variable est déterminé dynamiquement au moment de l'exécution en fonction de la valeur que la variable contient. Cependant, Python est un langage fortement typé, ce qui signifie que le type d'une variable est important lors de son utilisation dans des opérations.

Voici quelques-uns des types de variables de base en Python :



1. **Entier (`int`) :** Représente des nombres entiers.

    ```python
    x = 5
    y = -10
    ```

2. **Nombre à virgule flottante (`float`) :** Représente des nombres à virgule flottante.

    ```python
    pi = 3.14159
    age = 25.5
    ```

3. **Booléen (`bool`) :** Représente les valeurs de vérité, soit `True` ou `False`.

    ```python
    is_true = True
    is_false = False
    ```

4. **Chaîne de caractères (`str`) :** Représente des séquences de caractères.

    ```python
    message = "Bonjour, Python!"
    ```

5. **NoneType (`None`) :** Représente l'absence de valeur.

    ```python
    result = None
    ```

Ces sont quelques-uns des types de variables de base en Python. Il existe également des types plus avancés et des types personnalisés définis par l'utilisateur. Vous pouvez utiliser la fonction `type()` pour connaître le type d'une variable à un moment donné.



[doc_pyton_type](https://docs.python.org/3/library/stdtypes.html)



## 3. Nommage :

Le nommage des variables en Python suit certaines conventions pour assurer la lisibilité du code et la compréhension facile. Voici quelques règles et bonnes pratiques pour le nommage des variables en Python :

1. **Règles de Base :**
    - Les noms de variable peuvent contenir des lettres (majuscules ou minuscules), des chiffres et le caractère souligné (_).
    - Le nom de la variable ne peut pas commencer par un chiffre.
    - Il est recommandé d'utiliser des caractères en minuscules pour les noms de variable (PEP 8 - les conventions de style de code Python).

2. **Conventions de Style (PEP 8) :**
    - Les noms de variable doivent être des mots significatifs et descriptifs.
    - Utilisez des lettres minuscules pour les noms de variable simples (`x`, `count`) et des majuscules pour les noms de variable composés (`my_variable`).
    - Évitez d'utiliser des caractères en majuscules uniquement pour les noms de variables (`MY_VARIABLE`), sauf dans le cas de constantes (variables dont la valeur ne change pas).

3. **Évitez les Noms de Variables Uniquement Composés de Chiffres :**
    - Bien que légaux, les noms de variables composés uniquement de chiffres (`x1`, `value2`) peuvent être difficiles à comprendre. Essayez d'inclure des lettres significatives dans vos noms de variables pour plus de clarté.

4. **Évitez les Noms de Variables Réservés :**
    - N'utilisez pas les mots réservés du langage Python comme noms de variables. Par exemple, évitez d'utiliser des noms tels que `if`, `else`, `for`, etc.

5. **Utilisez des Noms descriptifs :**
    - Choisissez des noms de variables qui reflètent clairement le but ou la signification de la variable. Par exemple, utilisez `total_amount` au lieu de `t`.

6.  **sensible à la casse:**

    - Enfin, Python est sensible à la casse, ce qui signifie que les variables TesT , test ou TEST sont différentes.

Exemple de bonnes pratiques de nommage :

```python
# Noms de variables simples
count = 10
name = "John"

# Noms de variables composés
total_amount = 100.50
user_age = 25

# Noms de variables constants en majuscules
MAX_VALUE = 1000
PI = 3.14
```


## 4. Les opérations:

Python prend en charge diverses opérations pour effectuer des calculs, manipuler des données et interagir avec des variables. 

Voici un aperçu des opérations courantes en Python :

### Opérations Numériques :

1. **Addition (`+`):**
   ```python
   result = 10 + 5   # result prend la valeur 15
   ```

2. **Soustraction (`-`):**
   ```python
   result = 20 - 8   # result prend la valeur 12
   ```

3. **Multiplication (`*`):**
   ```python
   result = 6 * 7    # result prend la valeur 42
   ```

4. **Division (`/`):**
   ```python
   result = 15 / 3   # result prend la valeur 5.0 (flottant)
   ```

5. **Division entière (`//`):**
   ```python
   result = 15 // 2  # result prend la valeur 7 (entier)
   ```

6. **Modulo (`%`):**
   ```python
   result = 17 % 5   # result prend la valeur 2 (reste de la division)
   ```

7. **Puissance (`**`):**
   ```python
   result = 2 ** 3   # result prend la valeur 8 (2 élevé à la puissance 3)
   ```

### Opérations sur les Chaînes de Caractères :

1. **Concaténation (`+`):**
   ```python
   message = "Hello" + " " + "World"  # message prend la valeur "Hello World"
   ```

2. **Répétition (`*`):**
   ```python
   repeated = "ABC" * 3  # repeated prend la valeur "ABCABCABC"
   ```

### Opérations Logiques :

1. **ET (`and`):**
   ```python
   result = True and False  # result prend la valeur False
   ```

2. **OU (`or`):**
   ```python
   result = True or False   # result prend la valeur True
   ```

3. **Négation (`not`):**
   ```python
   result = not True        # result prend la valeur False
   ```

### Opérations de Comparaison :

1. **Égalité (`==`):**
   ```python
   result = 5 == 5    # result prend la valeur True
   ```

2. **Inégalité (`!=`):**
   ```python
   result = 10 != 8   # result prend la valeur True
   ```

3. **Supérieur (`>`), Inférieur (`<`), Supérieur ou Égal (`>=`), Inférieur ou Égal (`<=`):**
   ```python
   greater = 10 > 5   # greater prend la valeur True
   ```

Ces opérations sont fondamentales pour manipuler des données en Python. Vous pouvez les utiliser dans des expressions mathématiques, des comparaisons, des opérations logiques, et bien plus encore.


## 5. Casting:

Le casting en Python fait référence à la conversion d'une variable d'un type à un autre. Python prend en charge plusieurs fonctions de casting qui permettent de convertir des données d'un type à un autre. 

Voici quelques-unes des fonctions de casting couramment utilisées :

1. **Casting vers un Entier (`int()`):**
   - Convertit une variable en un entier.

    ```python
    float_number = 10.5
    int_number = int(float_number)  # int_number prend la valeur 10
    ```

2. **Casting vers un Nombre à Virgule Flottante (`float()`):**
   - Convertit une variable en un nombre à virgule flottante.

    ```python
    int_number = 5
    float_number = float(int_number)  # float_number prend la valeur 5.0
    ```

3. **Casting vers une Chaîne de Caractères (`str()`):**
   - Convertit une variable en une chaîne de caractères.

    ```python
    number = 42
    str_number = str(number)  # str_number prend la valeur "42"
    ```

4. **Casting vers un Booléen (`bool()`):**
   - Convertit une variable en un booléen. La plupart des valeurs sont converties en `True`, sauf certaines comme `0`, `False`, ou des objets vides qui sont convertis en `False`.

    ```python
    value = 0
    bool_value = bool(value)  # bool_value prend la valeur False
    ```

5. **Casting vers une Liste (`list()`):**
   - Convertit une séquence (par exemple, une chaîne de caractères ou un tuple) en une liste.

    ```python
    string_sequence = "Python"
    list_sequence = list(string_sequence)  # list_sequence prend la valeur ['P', 'y', 't', 'h', 'o', 'n']
    ```

6. **Casting vers un Tuple (`tuple()`):**
   - Convertit une séquence (par exemple, une liste) en un tuple.

    ```python
    list_sequence = [1, 2, 3]
    tuple_sequence = tuple(list_sequence)  # tuple_sequence prend la valeur (1, 2, 3)
    ```

7. **Casting vers un Ensemble (`set()`):**
   - Convertit une séquence (par exemple, une liste) en un ensemble.

    ```python
    list_sequence = [1, 2, 2, 3]
    set_sequence = set(list_sequence)  # set_sequence prend la valeur {1, 2, 3}
    ```

Ces fonctions de casting sont utiles lorsque vous devez convertir une variable d'un type à un autre pour répondre aux exigences d'une opération ou d'une fonction spécifique.