# cour 1 : Introduction 

## 1. **Introduction:**


- **Définition: ``NumPy``**

    >NumPy est une bibliothèque open-source en Python qui fournit des outils pour travailler avec des tableaux multidimensionnels. Le nom NumPy vient de "Numeric Python". Cette bibliothèque est largement utilisée dans le domaine de la science des données, de l'apprentissage automatique, de la vision par ordinateur et dans d'autres domaines de la programmation scientifique et technique.


- **Avantages:**

    Comparé aux listes Python ordinaires, les `ndarray` de NumPy offrent plusieurs avantages significatifs :

    - **Performance améliorée** : NumPy est implémenté en C, ce qui le rend beaucoup plus rapide pour les calculs numériques que les listes Python.

    - **Mémoire efficace** : Les tableaux NumPy occupent moins de mémoire que les listes Python pour stocker des données volumineuses.

    - **Fonctionnalités de broadcasting** : NumPy prend en charge le broadcasting, ce qui permet d'effectuer des opérations entre des tableaux de formes différentes de manière transparente.

## 2. **Le type `ndarray`:**


- **Definition:**

    >L'un des composants centraux de NumPy est le type de données `ndarray`, qui est un tableau multidimensionnel homogène. Les tableaux `ndarray` peuvent contenir des éléments de même type et permettent d'effectuer des opérations efficaces sur les données, telles que des opérations mathématiques, des manipulations de tableau, et des opérations de filtrage et d'agrégation.



- **Vecteurs (1D array) :**

    ```python
    import numpy as np

    # Créer un vecteur à partir d'une liste
    vecteur = np.array([1, 2, 3, 4, 5])

    # Afficher le vecteur
    print("Vecteur :", vecteur)
    ```

- **Matrices (2D array) :**

    ```python
    import numpy as np

    # Créer une matrice à partir d'une liste de listes
    matrice = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

    # Afficher la matrice
    print("Matrice :")
    print(matrice)
    ```

- **Images RGB (3D array) :**

    ```python
    import numpy as np

    image_RGB = np.array(
        [
            [
                [1, 2 , 3] ,
                [4 , 5 , 6] ,
                [7 , 8 , 9]
            ] , 
            [
                [1, 2 , 3] ,
                [4 , 5 , 6] ,
                [7 , 8 , 9]
            ],
            [
                [1, 2 , 3] ,
                [4 , 5 , 6] ,
                [7 , 8 , 9]
            ]
        ]
    )
    ```





## 3. **constructeur de ``ndarray``:**

### 3.1 **``np.array :``**


- **Description :** 
    >Crée un tableau NumPy à partir d'une liste ou d'un tuple.

- **Syntaxe :** 
    ```py
    np.array(object)
    ```

- **Exemple :**
    ```python
    import numpy as np
    
    # Créer un tableau à partir d'une liste
    arr1 = np.array([1, 2, 3, 4, 5])
    
    # Créer un tableau à partir d'un tuple
    arr2 = np.array((1, 2, 3, 4, 5))
    
    print("Array 1 :", arr1)
    print("Array 2 :", arr2)
    ```

### 3.2 **``np.zeros  :``** 

- **Description :** 
    >Crée un tableau NumPy rempli de zéros.

- **Syntaxe :** 
    ```py
    np.zeros(shape)
    ```
    - avec ``shape`` est un tuple qui représente la dimension du ``ndarry`` .

- **Exemple :**
    ```python
    import numpy as np
    
    # Créer un tableau de forme (3, 4) rempli de zéros
    zeros_array = np.zeros((3, 4))
    
    print("Array rempli de zéros :")
    print(zeros_array)
    ```

### 3.3 **``np.ones  :``** 


- **Description :** 
    >Crée un tableau NumPy rempli de uns.

- **Syntaxe :** 

    ```py
    np.ones(shape)
    ```
    - avec ``shape`` est un tuple qui représente la dimension du ``ndarry`` .


- **Exemple :**
    ```python
    import numpy as np
    
    # Créer un tableau de forme (2, 3) rempli de uns
    ones_array = np.ones((2, 3))
    
    print("Array rempli de uns :")
    print(ones_array)
    ```

### 3.4 **``np.eye  :``** 

- **Description :** 
    >Crée une matrice identité.

- **Syntaxe :** 

    ```py
    np.eye(N)
    ```
    - avec ``(N,N)``  représente la dimension (shape) du ``ndarry`` .

- **Exemple :**
    ```python
    import numpy as np
    
    # Créer une matrice identité de taille 3x3
    identity_matrix = np.eye(3)
    
    print("Matrice identité :")
    print(identity_matrix)
    ```

### 3.5 **``np.linspace  :``** 

- **Description :** 
    >Crée un tableau de valeurs uniformément réparties sur un intervalle spécifié.

- **Syntaxe :** 
    
    ```python
    np.linspace(start, stop, num)
    ```
    - return 1D Array .

- **Exemple :**
    ```python
    import numpy as np
    
    # Créer un tableau de 5 valeurs entre 0 et 10
    values = np.linspace(0, 10, 5)
    
    print("Valeurs espacées régulièrement :")
    print(values)
    ```

### 3.6.  **``np.arange  :``**  

- **Description :** 
    >Crée un tableau de valeurs espacées régulièrement dans un intervalle spécifié.

- **Syntaxe :** 
    
    ```python
    np.arange(start, stop, step)
    ``` 
    - return 1D Array .


- **Exemple :**
    ```python
    import numpy as np
    
    # Créer un tableau de valeurs de 0 à 9
    values = np.arange(10)
    
    print("Valeurs espacées régulièrement :")
    print(values)
    ```

### 3.7. **``np.random.randn :``**

- **Description :**
    >Génère un tableau de valeurs aléatoires à partir d'une distribution normale standard.

- **Syntaxe :** ``
    ```python
    np.random.randn(m ,n)
    ```
    - avce (m,n) = shape of the ``ndarry`` . 

- **Exemple :**
    ```python
    import numpy as np
    
    # Générer un tableau de 3x3 de valeurs aléatoires
    random_array = np.random.randn(3, 3)
    
    print("Tableau de valeurs aléatoires :")
    print(random_array)
    ```

## 4. **Attributs:**

### 4.1  **`ndim`:**

- **Description :** 
    >Cet attribut renvoie le nombre de dimensions de l'array.

- **Exemple :**

    ```python
    import numpy as np

    # Créer un array unidimensionnel
    arr_1d = np.array([1, 2, 3])
    print("Nombre de dimensions de l'array 1D :", arr_1d.ndim)  # Output: 1

    # Créer un array bidimensionnel
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("Nombre de dimensions de l'array 2D :", arr_2d.ndim)  # Output: 2
    ```

### 4.2 **`size`:**

- **Description :** 
    >Cet attribut renvoie le nombre total d'éléments présents dans l'array.

- **Exemple :**

    ```python
    import numpy as np

    # Créer un array de forme (3, 4)
    arr = np.zeros((3, 4))
    print("Taille totale de l'array :", arr.size)  # Output: 12 (3*4 = 12 éléments)
    ```

### 4.3. **`shape`**


- **Description :** 
    >Cet attribut renvoie un tuple qui décrit la taille de l'array le long de chaque dimension.

- **Exemple :**

    ```python
    import numpy as np

    # Créer un array de forme (3, 4)
    arr = np.zeros((3, 4))
    print("Forme de l'array :", arr.shape)  # Output: (3, 4) (3 lignes, 4 colonnes)
    ```

### 4.4 **`dtype:`**

- **Description :** 
    
    >L'attribut `dtype` renvoie le type de données des éléments contenus dans un tableau NumPy. Ce type de données peut être un type NumPy intégré (comme `numpy.int32`, `numpy.float64`, etc.) ou un type de données standard de Python (comme `int`, `float`, etc.).
    
    - On peut aussi spécifier le type de données dans un tableau ndarray avec cet attribut dans n'importe quel constructeur.


- **Exemple :** 

    ```python
    import numpy as np

    # Créer un array d'entiers
    arr_int = np.array([1, 2, 3])
    print("Type de données de l'array d'entiers :", arr_int.dtype)  # Output: int64

    # Créer un array de nombres à virgule
    arr_float = np.array([1.0, 2.0, 3.0])
    print("Type de données de l'array de nombres à virgule :", arr_float.dtype)  # Output: float64

    # ou spécifier un dtype partuciler :
    A = np.linspace(0 , 10  , 20 , dtype = np.float64);
    ```


#### RQ : 

- **Précision :** en augmentant le nombre de bits dans le type de données ( ``dtype`` ), vous pouvez obtenir une meilleure précision pour les calculs. Par exemple, un `float64` fournira une précision supérieure à un `float32`.

- **Performance :**  Des types de données avec moins de bits (comme `float32` au lieu de `float64`) peuvent être plus rapides à manipuler, car ils nécessitent moins de mémoire et peuvent être traités plus efficacement par le processeur. Cependant, cela peut se faire au détriment de la précision des calculs.

