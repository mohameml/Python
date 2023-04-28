## Énoncé

Dans cet exercice, nous allons voir comment utiliser le débogueur python standard `pdb`.
Le débogueur est un outil nous permettant d'exécuter un programme ligne par ligne, tout en offrant la possibilité d'inspecter la valeur des variables du programmes.

Pour lancer le débogueur sur votre programme `prog.py` il faut utiliser la commande suivante.

```console
python3 -m pdb prog.py
```

Dans cet exercice, vous devez utiliser le débogueur pour exécuter pas à pas le programme `un_petit_bug.py` [disponible ici](un_petit_bug.py) et affiché ci-dessous :

```python
#!/usr/bin/env python3
"""Un petit programme pour jouer avec le débogueur"""


def main():
    """Point d'entrée du programme"""

    age_du_capitaine = bool(input("Veuillez entrer l'age du capitaine:\n"))
    jusque_2042 = 2042 - 2020
    age_en_2042 = age_du_capitaine + jusque_2042
    print("En 2042 le capitaine aura", age_en_2042, "ans")


if __name__ == "__main__":
    main()
```

Une fois le débogueur lancé, votre programme sera arrêté sur la première ligne.
Vous pouvez utiliser la commande `help` pour obtenir la liste de toutes les commandes du débogueur.
Vous pouvez ensuite obtenir de l'aide concernant une commande particulière, par exemple `step` à l'aide de `help step`.

Vous utiliserez en particulier les commandes `step`, `next` et `print`.

Pour plus d'information concernant `pdb` vous pouvez consulter la page [https://docs.python.org/3.6/library/pdb.html](https://docs.python.org/3.10/library/pdb.html).

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Au démarrage du débogueur, le programme en cours de débogage est _interrompu_, et
se place en attente de commandes de l'utilisateur.

Quelques commandes utiles :

- `list` affiche le code source en cours de débogage, "autour" de là où s'est
arrêté le débogueur. Par exemple :

```
(Pdb) list
  5         """Point d'entrée du programme"""
  6
  7         age_du_capitaine = bool(input("Veuillez entrer l'age du capitaine:\n"))
  8         jusque_2042 = 2042 - 2020
  9         age_en_2042 = age_du_capitaine + jusque_2042
 10  ->     print("En 2042 le capitaine aura", age_en_2042, "ans")
 11
 12     if __name__ == "__main__":
 13         main()
```
La flèche indique **la prochaine ligne** qui sera exécutée.

- `step` permet d'exécuter une ligne de code puis d'interrompre l'exécution du
programme juste après. Dans le cas où la ligne à exécuter contient un appel de
fonction, `step` entre dans le code de cette fonction.

- `next` se comporte comme `step`, à ceci près qu'on n'entre pas dans le code
des fonctions appelées.

- `continue` reprend l'exécution du programme jusqu'à sa terminaison, ou jusqu'à
tomber sur un point d'arrêt.

- `var` affiche la valeur de la variable var. Par exemple :

```
(Pdb) age_en_2042
23
```

- `break` place un point d'arrêt dans le programme. S'utilise soit avec un nom
de fonction, soit avec un numéro de ligne (possiblement avec un nom de fichier).
Par exemple :

```
> python3 -m pdb ./un_petit_bug.py
> 12-debogueur-python/un_petit_bug.py(2)<module>()
-> """Un petit programme pour jouer avec le débogeur"""
(Pdb) list
  1     #!/usr/bin/env python3
  2  -> """Un petit programme pour jouer avec le débogeur"""
  3
  4     def main():
  5         """Point d'entrée du programme"""
  6
  7         age_du_capitaine = bool(input("Veuillez entrer l'age du capitaine:\n"))
  8         jusque_2042 = 2042 - 2020
  9         age_en_2042 = age_du_capitaine + jusque_2042
 10         print("En 2042 le capitaine aura", age_en_2042, "ans")
 11
(Pdb) break 9
Breakpoint 1 at 12-debogueur-python/un_petit_bug.py:9
(Pdb) continue
Veuillez entrer l'age du capitaine:
47
> 12-debogueur-python/un_petit_bug.py(9)main()
-> age_en_2042 = age_du_capitaine + jusque_2042
(Pdb)
```

- `quit` ferme le debugger.
</details>
