## Énoncé

On considère le programme suivant :

```python
#!/usr/bin/env python3

"""Mystery code for recursivity."""

def mystery_function(first, second):
    """a mystery function"""
    print("mystery_function called with first =", first,
          "and second =", second)
    mystery_function(first + 1, "first")
    mystery_function(first + 1, "second")

def main():
    """Program's entry point."""
    mystery_function(23, "init")

if __name__ == "__main__":
    main()
```

Quel est son comportement ?

    - une exécution infinie avec des affichages qui ne varient pas.
      Dans ce cas, qu'affiche le terminal ?
    - rien ne se passe ;
    - une exécution infinie avec des affichages qui varient.
      Dans ce cas, qu'affiche le terminal ?
    - des affichages puis un "freeze" de la machine à cause de la mémoire ;
    - autre. Dans ce cas que se passe-t-il et pourquoi ?

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Dans ce programme, on va faire des appels récursifs indéfiniment.
En effet, la fonction `mystery_function` se rappelle elle même deux fois dans **tous les cas**.
Autrement dit, il n'y a pas de cas particulier permettant d'arrêter la récursion.

Afin d'éviter des problèmes de mémoire, l'interpréteur Python possède une limite quant au nombre maximum d'appels récursifs qui peuvent être fait.
Quand ce nombre est dépassé, une exception `RecursionError` est lancée.

La bonne réponse était donc la dernière, et voici la sortie du programme :

```console
...
mystery_function called with first = 1017 and second = first
Traceback (most recent call last):
  File "./stackoverflow.py", line 16, in <module>
    main()
  File "./stackoverflow.py", line 13, in main
    mystery_function(23, "init")
  File "./stackoverflow.py", line 8, in mystery_function
    mystery_function(first + 1, "first")
  File "./stackoverflow.py", line 8, in mystery_function
    mystery_function(first + 1, "first")
  File "./stackoverflow.py", line 8, in mystery_function
    mystery_function(first + 1, "first")
  [Previous line repeated 991 more times]
  File "./stackoverflow.py", line 7, in mystery_function
    print("mystery_function called with first =", first, "and second =", second)
RecursionError: maximum recursion depth exceeded while calling a Python object
```
</details>
