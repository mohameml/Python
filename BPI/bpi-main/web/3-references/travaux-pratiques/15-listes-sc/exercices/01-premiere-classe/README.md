## Énoncé

Dans cet exercice nous allons créer notre première classe : `Cellule`.
Celle-ci sera utilisée tout au long du chapitre `3- Références` comme élément de base d'une liste chaînée.
Il est donc fondamentale de bien comprendre cet exercice.

Néanmoins, nous ne ferons pas de programmation orientée objet en BPI.
Nous utiliserons la classe `Cellule` de la même manière que nous avons utilisé des `namedtuple` jusqu'ici.
La différence fondamentale concerne la **mutabilité**.
En effet, les **instances** de notre classe `Cellule` sont des objets modifiables : leurs attributs peuvent être modifiés.

Écrire une classe `Cellule` composée de deux attributs :

- `valeur` ;
- `suivant`.

On rappelle que les attributs d'une instance sont toujours des références.
La `valeur` sera donc une référence vers un nombre entier ou flottant et `suivant` une référence vers une autre cellule (utilisée par la suite pour implémenter des listes chaînées).
Voici un exemple d'une classe `Point` pour vous aider.

```python
#!/usr/bin/env python3

"""Un exemple de classe : point"""

class Point:
    """Un point dans le plan 2D.

    Un point possède une abscisse et une ordonnée.
    __str__ est une "fonction" spéciale, utilisée par l'interpréteur
    entre autre lorsqu'un point doit être affiché sur la sortie
    standard au travers d'un appel à la fonction print.
    """

    def __init__(self, x, y):
        self.abscisse = x
        self.ordonnee = y

    def __str__(self):
        return 'point_(' + str(self.abscisse) + ',' + str(self.ordonnee) + ')'

def main():
    """Test de notre classe Point"""

    # Création de deux points
    point1 = Point(17, 23)
    point2 = Point(5, 7)

    # Affichage de la somme des abscisses
    # __str__ est automatiquement appelé par l'interpréteur
    # pour savoir comment afficher un point.
    somme1 = point1.abscisse + point2.abscisse
    print("Somme de l'abscisse de", point1, "et de l'abscisse de", point2, "=", somme1)

    # Les points sont modifiables.
    point1.abscisse = 3
    somme1 = point1.abscisse + point2.abscisse
    print("Somme de l'abscisse de", point1, "et de l'abscisse de", point2, "=", somme1)

if __name__ == "__main__":
    main()
```

Comme dans l'exemple des points ci-dessus, penser à **tester** votre classe en créant des instances et en jouant avec.
