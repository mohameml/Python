# les fonctions `ord()` et `chr()` :

En Python, les fonctions `ord()` et `chr()` sont utilisées pour convertir des caractères en leur valeur ASCII et vice versa.

## La fonction `ord()` :

La fonction `ord()` prend en entrée un caractère et retourne sa valeur ASCII correspondante. 

Par exemple, `ord('A')` renvoie 65, qui est la valeur ASCII du caractère 'A'. 

La fonction `ord()` est utile lorsque vous avez besoin de manipuler des caractères en utilisant leurs valeurs ASCII dans vos opérations.

Voici un exemple d'utilisation de la fonction `ord()` :

```python
caractere = 'A'
valeur_ascii = ord(caractere)
print(valeur_ascii)  # Affiche 65

```

## La fonction `chr()` :

La fonction `chr()` fait l'inverse de `ord()`. 

Elle prend en entrée une valeur ASCII et retourne le caractère correspondant. Par exemple, `chr(65)` renvoie le caractère 'A'.

Voici un exemple d'utilisation de la fonction `chr()` :

```python
valeur_ascii = 65
caractere = chr(valeur_ascii)
print(caractere)  # Affiche 'A'

```

Les fonctions `ord()` et `chr()` sont souvent utilisées en conjonction lorsque vous avez besoin de convertir entre les caractères et les valeurs ASCII dans vos programmes Python.

Il est important de noter que `ord()` et `chr()` fonctionnent uniquement pour les caractères ASCII standard, qui vont de 0 à 127. Si vous travaillez avec des caractères Unicode étendus, vous pouvez utiliser les fonctions `ord()` et `chr()` en combinaison avec les méthodes `encode()` et `decode()` pour effectuer les conversions appropriées.