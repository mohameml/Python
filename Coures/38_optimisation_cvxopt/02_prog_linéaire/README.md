# cour : **``Programmation linéaire avce cvxopt``**

## 1. **Definition:**

>La programmation linéaire (PL) est un type d'optimisation où l'objectif est de minimiser ou maximiser une fonction linéaire sous des contraintes linéaires.


$$ \text{Minimiser } c^T x$$
$$ \text{sous contraintes :}$$
$$ Gx \leq h$$
$$ Ax = b$$



- **Objectif :**
    Minimiser la fonction objective $c^T x$, où $c$ est un vecteur de coefficients, et $x$ est un vecteur de variables de décision que nous cherchons à optimiser.

- **Contraintes linéaires inégalités :**
    
    Les contraintes linéaires inégalités sont exprimées sous la forme $Gx \leq h$ .  La matrice $G$ représente les coefficients des variables de décision dans les contraintes, et $h$ est un vecteur qui spécifie le côté droit des inégalités.

- **Contraintes linéaires égalités :**

    Les contraintes linéaires égalités sont exprimées sous la forme $Ax = b$ . La matrice $A$ représente les coefficients des variables de décision dans les contraintes égalités, 
    et $b$ est un vecteur qui spécifie le côté droit des égalités.



- **Exemple Numérique :**

    Considérons un exemple numérique spécifique pour illustrer le problème. Supposons que nous ayons le problème suivant :

$$ \text{Minimiser } -2x_1 + 3x_2$$ 
$$ \text{sous contraintes :}$$ 
$$ 3x_1 + x_2 \leq 9$$ 
$$ x_1 + 2x_2 \leq 8$$ 
$$ x_1, x_2 \geq 0$$


Dans ce cas, le vecteur $c$ serait $[-2, 3]$, la matrice $G$ serait $\begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}$, le vecteur $h$ serait $[9, 8]$, 


la matrice $A$ serait  $\begin{bmatrix} 0 & 0 \end{bmatrix}$ (car il n'y a pas de contraintes égalités dans cet exemple),  et le vecteur $b$ serait $[0]$.




## 2. **la fonction ``cvxopt.solvers.lp``:**

- **Def:**
    
    >La fonction `cvxopt.solvers.lp` dans CVXOPT est utilisée pour résoudre des problèmes de programmation linéaire (PL). la fonction `cvxopt.solvers.lp` résout un problème de minimisation. Cela signifie que la fonction objective à optimiser est une fonction que vous essayez de minimiser.

    Si vous avez un problème de maximisation, vous devez ajuster le signe des coefficients de la fonction objective pour le rendre compatible avec la nature du problème. 
    


- **Synatxe:**

    ```python
    from cvxopt import solvers
    solvers.lp(c, G, h, A=None, b=None, solver=None, primalstart=None, dualstart=None, **kwargs)
    ```

    - `c` : Un vecteur colonne représentant la fonction objective à minimiser. Dans un problème de programmation linéaire, 
    
    - `G` : Une matrice représentant les coefficients des contraintes linéaires inégalités 
    

    - `h` : Un vecteur représentant le côté droit des contraintes linéaires inégalités ..

    - `A` : Une matrice représentant les coefficients des contraintes linéaires égalités . Chaque ligne de la matrice `A` correspond à une contrainte linéaire égalité. Par défaut, `A` est `None`, ce qui signifie qu'il n'y a pas de contraintes linéaires égalités.

    - `b` : Un vecteur représentant le côté droit des contraintes linéaires égalités . Par défaut, `b` est `None`.

    - `solver` : Paramètre optionnel pour spécifier le solveur à utiliser. Si ce paramètre est laissé à `None`, le solveur par défaut sera utilisé. Vous pouvez spécifier d'autres solveurs tels que `'glpk'` ou `'mosek'` si vous les avez installés et configurés.


- **valeur de retour:**

    - La fonction `cvxopt.solvers.lp` renvoie un dictionnaire contenant diverses informations sur la solution du problème de programmation linéaire (LP).
    
    - **Voici une description des principales clés de ce dictionnaire :**

        - **`'x'`** : C'est un vecteur contenant la solution optimale du problème. Les valeurs dans ce vecteur correspondent aux valeurs optimales des variables de décision qui minimisent (ou maximisent) la fonction objective.

        - **`'primal objective'`** : C'est la valeur optimale de la fonction objective. Cela indique la valeur minimale (ou maximale) atteinte par la fonction objective pour les valeurs optimales des variables de décision.

        - **`'status'`** : C'est une chaîne de caractères indiquant le statut de la solution du problème. Par exemple, `'optimal'` signifie que la solution est optimale, `'infeasible'` signifie que le problème est infaisable, et d'autres statuts peuvent inclure `'unbounded'`, `'unknown'`, etc.

        - **`'dual objective'`** : C'est la valeur optimale de la fonction duale associée au problème. Cette valeur est souvent utilisée pour évaluer la qualité de la solution et vérifier la dualité.

        - **`'primal slack'`** et **`'dual slack'`** : Ce sont des vecteurs indiquant les écarts (slack) primaires et duaux respectivement. Ils donnent des informations sur la distance entre les contraintes du problème et la solution optimale.


- **Exemple:**

    ```python
    import cvxopt

    c = cvxopt.matrix([-4.0, -5.0])
    G = cvxopt.matrix([[2.0, 1.0], [1.0, 2.0]])
    h = cvxopt.matrix([3.0, 3.0])

    sol = cvxopt.solvers.lp(c, G, h)

    print("Solution:")
    print(sol['x'])
    ```

    Dans cet exemple, le problème consiste à minimiser la fonction $c^T x = -4x_1 - 5x_2$  sous les contraintes linéaires inégalités $2x_1 + x_2 \leq 3$ et $x_1 + 2x_2 \leq 3$. La fonction `cvxopt.solvers.lp` renvoie un dictionnaire contenant la solution, y compris la valeur optimale de la fonction objectif et les valeurs optimales des variables. Vous pouvez accéder à la solution avec `sol['x']`.









