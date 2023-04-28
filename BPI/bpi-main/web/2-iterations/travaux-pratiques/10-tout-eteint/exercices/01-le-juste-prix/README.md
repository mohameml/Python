## Énoncé

Le juste prix est `42`, mais votre utilisateur ne le sait pas et il doit le deviner.

Écrivez un programme qui demande un nombre à l'utilisateur jusqu'à ce que celui-ci trouve `42`.
Votre programme doit indiquer pour chaque proposition de l'utilisateur si il se trouve au dessus, en dessous ou au juste prix.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

`juste_prix.py` :

```python
#!/usr/bin/env python3
"""Un exemple d'utilisation d'une boucle while"""

def demande_prix():
    """Demande un prix à l'utilisateur"""
    print("Quel est votre proposition ?")
    return int(input())


def main():
    """Point d'entrée du programme."""
    prix_propose = demande_prix()

    # Tant que (== while en anglais, ça tombe bien)
    # l'utilisateur n'a pas trouvé le juste prix
    while prix_propose != 42:

        # On lui indique de quel côté il
        # se situe
        if prix_propose > 42:
            print("c'est moins !")
        else:
            print("c'est plus !")

        # On lui demande de faire une
        # nouvelle proposition
        prix_propose = demande_prix()

    # Quand on arrive ici, l'utilisateur
    # a trouvé
    print("c'est trouvé !")


if __name__ == "__main__":
    main()
```
</details>
