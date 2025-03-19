# Cour : **Introduction `PF`:**

# 🔥 **Introduction à la Programmation Fonctionnelle (PF)**

La **programmation fonctionnelle (PF)** est un **paradigme de programmation** basé sur l'utilisation de **fonctions pures** et sur l'absence d'effets de bord. Ce paradigme est utilisé dans des langages comme **Haskell, Lisp, OCaml**, mais aussi dans des langages multi-paradigmes comme **Python, JavaScript, Scala**.

---

## 📌 **1. Définition de la Programmation Fonctionnelle**

La programmation fonctionnelle est un **style de programmation** où les calculs sont exprimés sous forme d'**applications de fonctions**. Contrairement aux approches **impératives** ou **orientées objet**, la PF se base sur des **fonctions mathématiques pures**, l'**immuabilité des données**, et l'**évaluation paresseuse**.

**Exemple simple de PF :**

```python
# Fonction pure : pas de modification d'état global
def carre(x):
    return x ** 2

# Utilisation de map() pour appliquer la fonction sur une liste
nombres = [1, 2, 3, 4]
resultat = list(map(carre, nombres))  # [1, 4, 9, 16]
```

---

## 🎯 **2. Principes Clés de la Programmation Fonctionnelle**

| Principe                       | Description                                                                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Fonctions pures**            | Une fonction **pure** retourne toujours le même résultat pour les mêmes entrées et **n’a pas d’effets de bord**.                    |
| **Immutabilité**               | Les variables ne changent pas après leur initialisation. On privilégie la création de nouvelles valeurs plutôt que la modification. |
| **Absence d'effets de bord**   | Une fonction ne modifie pas de variables globales, n’imprime rien, ne modifie pas un fichier.                                       |
| **Évaluation paresseuse**      | Un calcul n'est effectué que lorsqu’il est **nécessaire** (ex. générateurs).                                                        |
| **Composabilité**              | On assemble des fonctions simples pour en créer de plus complexes.                                                                  |
| **Transparence référentielle** | Une expression peut être remplacée par son résultat sans changer le comportement du programme.                                      |

---

## 🔑 **3. Mots-clés et Concepts Importants**

1. **`lambda` (fonctions anonymes)**
    ```python
    carre = lambda x: x ** 2
    print(carre(5))  # 25
    ```
2. **`map()` (Application d’une fonction sur un iterable)**
    ```python
    nombres = [1, 2, 3]
    print(list(map(lambda x: x ** 2, nombres)))  # [1, 4, 9]
    ```
3. **`filter()` (Filtrage basé sur une condition)**
    ```python
    pairs = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
    print(pairs)  # [2, 4]
    ```
4. **`reduce()` (Accumulation successive d'un calcul)**
    ```python
    from functools import reduce
    somme = reduce(lambda x, y: x + y, [1, 2, 3, 4])
    print(somme)  # 10
    ```
5. **Immuabilité avec `namedtuple` et `dataclass(frozen=True)`**
    ```python
    from collections import namedtuple
    Point = namedtuple("Point", ["x", "y"])
    p = Point(1, 2)
    # p.x = 3  # Erreur car immutable
    ```
6. **Décorateurs (`@decorator`)**

    ```python
    def decorateur(f):
        def wrapper():
            print("Avant")
            f()
            print("Après")
        return wrapper

    @decorateur
    def dire_hello():
        print("Hello !")

    dire_hello()
    ```

---

## ⚖️ **4. Différences entre PF, Programmation Impérative et POO**

| Critère                  | Programmation Fonctionnelle                                 | Programmation Impérative                                                   | Programmation Orientée Objet (POO)                                 |
| ------------------------ | ----------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Modèle**               | Basée sur les **fonctions pures** et l’**immuabilité**.     | Basée sur les **instructions séquentielles** (modification d'état global). | Basée sur la **modélisation d'objets avec des états et méthodes**. |
| **Mutation des données** | **Évitée** (les données sont immuables).                    | **Fréquente** (les variables sont modifiées directement).                  | **Utilisée**, mais avec encapsulation.                             |
| **Effets de bord**       | **Évités autant que possible**.                             | **Fréquents** (ex: `print()`, modifier un fichier).                        | Peuvent être contrôlés par l'encapsulation.                        |
| **Évaluation**           | **Laziness possible** (calcul à la demande).                | **Évaluation immédiate**.                                                  | **Évaluation immédiate**.                                          |
| **Exécution parallèle**  | **Facilitée** (pas d’état mutable, donc moins de conflits). | **Difficile** (risque de conflits sur les variables).                      | **Possible**, mais nécessite des verrous et synchronisation.       |

---

## 🚀 **5. Avantages et Inconvénients de la Programmation Fonctionnelle**

✅ **Avantages :**

-   📌 **Code plus prévisible** (grâce aux fonctions pures).
-   ⚡ **Moins de bugs liés aux effets de bord**.
-   🔄 **Facilité de parallélisation**.
-   🏗 **Réutilisation et modularité** (composabilité des fonctions).

❌ **Inconvénients :**

-   📚 **Courbe d'apprentissage plus complexe**.
-   🔄 **Performance parfois moins bonne** (ex: trop de créations de copies d’objets).
-   🏗 **Difficile à implémenter dans des langages conçus pour la POO (ex: Java)**.

---

## 🎯 **6. Quand utiliser la Programmation Fonctionnelle ?**

📌 **Idéale pour :**

-   🚀 **Traitement de données** (Big Data, Machine Learning).
-   ⏳ **Calcul parallèle et concurrence** (sans risque d’état partagé).
-   📈 **Modélisation mathématique et finance** (ex: fonctions analytiques).
-   🔧 **Développement Backend** (ex: transformation de données).

📌 **Moins efficace pour :**

-   🏗 **Modélisation d'objets complexes** (POO est plus adaptée).
-   🔄 **Développement nécessitant des changements d'état fréquents**.

---

## 🎯 **7. Python et la Programmation Fonctionnelle**

Python **n'est pas un langage purement fonctionnel**, mais il **supporte bien** ce paradigme. Il combine **impératif, POO et fonctionnel**.

📌 **Outils Python pour la PF :**

-   **`map()`, `filter()`, `reduce()`** (opérations sur collections)
-   **`lambda`** (fonctions anonymes)
-   **`functools`** (`partial`, `lru_cache`, `reduce()`)
-   **`itertools`** (traitement paresseux des données)
-   **Générateurs (`yield`)** (évaluation paresseuse)
-   **Décorateurs (`@decorator`)** (modification de fonction)

---

## 🚀 **Conclusion**

La **programmation fonctionnelle** est un paradigme puissant qui permet d'écrire **du code plus modulaire, prévisible et parallèle**. Bien que Python ne soit pas un langage 100% fonctionnel, il **intègre de nombreux outils** pour exploiter ce paradigme.

👉 **Si tu veux approfondir, veux-tu un exercice avancé en Python pour pratiquer la PF ?** 🚀
