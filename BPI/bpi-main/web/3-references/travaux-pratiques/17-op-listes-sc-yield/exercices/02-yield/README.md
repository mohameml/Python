## Énoncé

Écrire un générateur permettant d'itérer sur tous les nombres premiers compris entre `1` et un nombre `maxi` donnée en paramètre.

Pour ce faire, vous compléterez le fichier `premiers.py` [disponible ici](premiers.py) et affiché ci-dessous.

```python
#!/usr/bin/env python3

"""Générateur des premiers nombres premiers"""

import sys
import math


def est_premier(number):
    """La complexité n'est pas le sujet ici, donc on a fait ça
    naïvement."""
    for diviseur in range(2, int(math.sqrt(number)) + 1):
        if (number % diviseur) == 0:
            return False
    return True


def genere_premiers():
    """Générateur infini de nombres premiers.

    La complexité n'est pas le sujet ici, donc on a fait ça
    naïvement. Et donc, attention à ne pas tester avec un maxi trop
    grand pour ne pas attendre trop longtemps, et surtout user la
    planète avec des calculs inutiles.
    """
    # 2 est premier,on le sait, alors on le renvoie directement
    # pour le plaisir, et voir que yield peut s'utiliser en dehors
    # d'une boucle
    yield 2

    # Ensuite on itère à l'infini, Python est génial !
    # TODO
    ...


def test():
    """Teste le générateur des premiers nombres premiers"""

    # L'utilisateur donne maxi
    if len(sys.argv) == 1:
        print("Usage :", sys.argv[0], "maxi")
        return
    maxi = int(sys.argv[1])

    # On affiche
    gen_premiers = genere_premiers()
    nb_affiche = 0
    while nb_affiche < maxi:
        print(next(gen_premiers))
        nb_affiche += 1


if __name__ == "__main__":
    test()
```

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Grâce au transfert du flot de contrôle effectué par le `yield`, on peut en Python écrire des boucles infinies qui n'en sont pas vraiment.

Voici donc le code de correction :

```python
#!/usr/bin/env python3

"""Générateur des premiers nombres premiers"""

import sys
import math


def est_premier(number):
    """La complexité n'est pas le sujet ici, donc on a fait ça
    naïvement."""
    for diviseur in range(2, int(math.sqrt(number)) + 1):
        if (number % diviseur) == 0:
            return False
    return True


def genere_premiers():
    """Générateur infini de nombres premiers.

    La complexité n'est pas le sujet ici, donc on a fait ça
    naïvement. Et donc, attention à ne pas tester avec un maxi trop
    grand pour ne pas attendre trop longtemps, et surtout user la
    planète avec des calculs inutiles.
    """
    # 2 est premier,on le sait, alors on le renvoie directement
    # pour le plaisir, et voir que yield peut s'utiliser en dehors
    # d'une boucle
    yield 2

    # Ensuite on itère à l'infini, Python est génial !
    number = 3
    while True:
        if est_premier(number):
            # Plutôt que de construire une list (== un vecteur) avec
            # tous les nombres premiers, on rend la main dès qu'on
            # en trouve un
            yield number
        number += 1


def test():
    """Teste le générateur des premiers nombres premiers"""

    # L'utilisateur donne maxi
    if len(sys.argv) == 1:
        print("Usage :", sys.argv[0], "maxi")
        return
    maxi = int(sys.argv[1])

    # On affiche
    gen_premiers = genere_premiers()
    nb_affiche = 0
    while nb_affiche < maxi:
        print(next(gen_premiers))
        nb_affiche += 1


if __name__ == "__main__":
    test()
```
</details>
