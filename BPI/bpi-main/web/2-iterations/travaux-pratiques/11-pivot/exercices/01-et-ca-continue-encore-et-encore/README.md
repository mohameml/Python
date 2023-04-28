## Énoncé

Dans tous les langages de programmation impératifs, il est possible de s'arrêter en plein milieu d'une itération d'une boucle et de passer directement à la suivante, que ce soit dans une boucle `for` ou `while`.
L'opérateur à utiliser pour ça est `continue`.

Vous devez maintenant reprendre le jeu du juste prix vu précédemment et ajouter le comportement ci-dessous à votre programme, uniquement à l'aide de 4 lignes de codes supplémentaires au début de la boucle. C'est à dire **sans changer aucune ligne** du code de correction du juste prix [disponible ici.](../../../10-tout-eteint/exercices/01-le-juste-prix)

*Nouveau comportement* : si l'utilisateur propose un prix négatif, ne lui indiquez pas où il se situe mais répondez lui "Comment ? Vous me pensez assez tordu pour avoir choisi un prix négatif ???".

<details markdown="1">
<summary>Cliquez ici pour révéler un indice.</summary>
## Indice
Il faut utiliser le mot clef `continue` ^^
<br>
</details>

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

`je_lache_l_affaire.py` :

```python
#!/usr/bin/env python3
"""Un exemple d'utilisation d'une boucle while avec continue"""
def demande_prix():
    """Demande à l'utilisateur un prix"""
    print("Quel est votre proposition ?")
    return int(input())


prix_propose = demande_prix()

# Tant que (== while en anglais, ça tombe bien)
# l'utilisateur n'a pas trouvé le juste prix
while prix_propose != 42:

    # Traitement spécial si le prix proposé est négatif
    if prix_propose < 0:
        print(
            "Comment ? Vous me pensez assez tordu pour avoir choisi un prix négatif ???"
        )
        prix_propose = demande_prix()
        continue

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
```
</details>
