## Énoncé

Dans tous les langages de programmation impératifs, en plus de la possibilité d'arrêter une itération en plein milieu, il possible de sortir complètement de la boucle englobante la plus proche.
Pour cela, il faut utiliser l'opérateur `break`.

Vous devez maintenant (encore) reprendre le jeu du juste prix vu précédemment et étendre le code de correction, [disponible ici](../07-je-lache-l-affaire), pour ajouter le comportement ci-dessous à votre programme :

*Nouveau comportement* : si l'utilisateur n'a pas trouvé au bout de trois essais, on sort de la boucle et on lui indique qu'il a perdu.

Pour vous obliger à utiliser `break`, **on interdit de changer la condition d'arrêt de la boucle** `while` écrite dans la version précédente du jeu du juste prix.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

`je_lache_vraiment_l_affaire.py` :

```python
#!/usr/bin/env python3
"""Un exemple d'utilisation d'une boucle while avec break"""
def demande_prix():
    """Demande à l'utilisateur un prix"""
    print("Quel est votre proposition ?")
    return int(input())


prix_propose = demande_prix()

nb_essais = 0

# Tant que (== while en anglais, ça tombe bien)
# l'utilisateur n'a pas trouvé le juste prix
while prix_propose != 42:

    # L'utilisateur a déjà joué trois fois, c'est fini !
    if nb_essais == 3:
        break
    nb_essais += 1

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
# a trouvé ou a déjà fait trois propositions
if prix_propose == 42:
    print("c'est trouvé !")
else:
    print("perdu !")
```
</details>
