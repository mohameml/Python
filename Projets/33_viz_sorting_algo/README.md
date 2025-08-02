# 🧠 viz_sorting — Visualisation interactive des algorithmes de tri en Python

**viz_sorting** est un mini-projet éducatif développé en Python pour visualiser l'exécution étape par étape de différents algorithmes de tri. Le but est de permettre une compréhension intuitive et interactive du fonctionnement interne de ces algorithmes à travers une interface animée.

---

## 🎯 Objectifs du projet

-   Implémenter **12 algorithmes de tri** classiques et avancés.
-   Développer une **interface graphique (GUI)** en Python avec **Tkinter**.
-   Afficher les **étapes d'exécution** des algorithmes de tri sous forme de **barres animées**.
-   Permettre à l'utilisateur de **choisir l'algorithme**, **contrôler la vitesse**, et **générer un nouveau tableau à trier**.

---

## 🧩 Structure du projet

Le projet est divisé en plusieurs étapes pour faciliter la conception et la lisibilité :

### ✅ Étape 1 — Interface Graphique (Tkinter)

-   📦 `main.py` : Point d’entrée de l’application.
-   Utilisation de **Tkinter** pour :

    -   Créer la fenêtre principale.
    -   Ajouter des **widgets** : boutons, menus déroulants, sliders, canvas.
    -   Permettre à l’utilisateur de :

        -   Choisir l’algorithme de tri.
        -   Lancer / Réinitialiser le tri.
        -   Régler la vitesse d’animation.
        -   Générer de nouvelles données aléatoires.

### ✅ Étape 2 — Génération et affichage des données

-   Génération aléatoire d’un tableau d’entiers.
-   Chaque entier est représenté par une **barre verticale** sur un `Canvas`.
-   Les barres sont dessinées avec différentes couleurs pendant le tri pour indiquer :

    -   Les éléments comparés.
    -   Les éléments échangés.
    -   Les éléments déjà triés.

### ✅ Étape 3 — Implémentation des algorithmes de tri

-   Chaque algorithme est implémenté dans un fichier ou fonction séparé(e) sous forme de **générateur Python** (avec `yield`) pour pouvoir être visualisé pas à pas.
-   Liste des algorithmes à implémenter :

    1. Bubble Sort [link](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles)
    2. Selection Sort
    3. Insertion Sort
    4. Merge Sort
    5. Quick Sort
    6. Heap Sort
    7. Shell Sort
    8. Radix Sort
    9. Counting Sort
    10. Cocktail Shaker Sort
    11. Comb Sort
    12. Gnome Sort

### ✅ Étape 4 — Animation & Visualisation

-   Boucle principale qui utilise `after()` de Tkinter pour animer les étapes.
-   Chaque `yield` renvoie une nouvelle itération de l’état du tableau.
-   Mise à jour du canvas à chaque étape avec les nouvelles couleurs et hauteurs.

### ✅ Étape 5 — Optimisation et ergonomie

-   Ajout d’un contrôle de **vitesse (slider)**.
-   Réduction du **flickering** via une bonne gestion du `Canvas`.
-   Ajout d’un **label** indiquant le nom de l’algorithme sélectionné et l’état du tri.
-   Gestion d’erreurs pour éviter les conflits entre les boutons/actions.

---

## 📁 Organisation des fichiers

```bash
viz_sorting/
│
├── main.py               # Point d’entrée de l’application
├── gui.py                # Construction de l’interface Tkinter
├── algorithms/
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   └── ... (autres algorithmes)
├── utils/
│   ├── draw.py           # Fonctions utilitaires pour dessiner les barres
│   └── data.py           # Génération aléatoire de tableaux
├── README.md             # Documentation du projet
└── requirements.txt      # Dépendances (facultatif, ici seulement Tkinter est requis)
```

---

## ▶️ Lancement du projet

```bash
python main.py
```

---

## 🔧 Prérequis

-   Python 3.8+
-   Aucune dépendance externe (Tkinter est inclus par défaut)

---

## 🌱 Idées futures

-   Exporter les animations en `.gif` ou `.mp4`.
-   Ajouter un mode "pas-à-pas" manuel.
-   Intégrer d’autres algorithmes (Bitonic Sort, TimSort…).
-   Version Web avec PyScript ou Streamlit.
