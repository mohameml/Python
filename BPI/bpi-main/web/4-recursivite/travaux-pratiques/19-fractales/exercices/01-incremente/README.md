## Énoncé

Implémenter la fonction suivante de façon **récursive** :

```python
def incremente(number, increment):
    """Renvoie number + increment."""
```

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

```python
#!/usr/bin/env python3
"""Une première fonction récursive."""

def incremente(number, increment):
    """Renvoie number + increment."""

    # Cas de base
    if increment == 0:
        return number

    # cas général
    return 1 + incremente(number, increment - 1)

def teste():
    """Teste la fonction ci-dessus."""
    print("incremente(0, 0) =", incremente(0, 0))
    print("incremente(42, 0) =", incremente(42, 0))
    print("incremente(0, 42) =", incremente(0, 42))
    print("incremente(42, 42) =", incremente(42, 42))
    print("incremente(-42, 42) =", incremente(-42, 42))

if __name__ == "__main__":
    teste()
```

</details>
