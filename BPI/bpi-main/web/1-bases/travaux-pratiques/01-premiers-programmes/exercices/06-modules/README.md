## Énoncé

L'objectif de cet exercice est de se familiariser avec la notion de découpage d'un programme en modules.
Dans n'importe quel langage de programmation, l'intérêt de découper un programme en modules concerne la factorisation du code.
En effet, un module va regrouper un ensemble cohérent de fonctions ainsi que de déclarations qui seront ensuite utilisées à différents endroits.
En python, un module est simplement un fichier `.py`.

Nous allons également utiliser cet exercice pour prendre de bonnes habitudes de programmation, à savoir **commencer** par écrire le code de test.

Le module à réaliser est `saisie_utilisateur.py` et fournira les fonctions suivantes :

```python
def demande_entier():
    """Demande gentiment un entier à l'utilisateur"""
    # TODO
    ...

def demande_chaine():
    """Demande gentiment une chaine de cractères à l'utilisateur"""
    # TODO
    ...
```

**Créez** le module `saisie_utilisateur.py` et recopiez y le code ci-dessus.
Bien que ne faisant rien, votre module est d'ores et déjà "utilisable" car c'est un programme syntaxiquement correct.
En effet, le symbole `...` appelé `Ellipsis` est valide en python.
Ce dernier n'a aucun effet lors de son exécution.
Il sert à indiquer au programmeur que le fichier qu'il regarde n'est pas un fichier python "normal".
Dans notre cas, `...` précédé du commentaire `#TODO` indique les endroits du code où vous devez intervenir.
Le symbole `pass` que vous connaissez peut être déjà est équivalent à `...` et peut également être utilisé pour les mêmes raisons.

**Écrivez** ensuite le programme principal `test_saisie_utilisateur.py` qui testera votre module en faisant quelques appels aux deux fonctions.
Vous pouvez d'ores et déjà exécuter votre programme de test sachant que le module, bien que pas encore implémenté, est syntaxiquement correct.
Néanmoins, en fonction de ce que votre programme `test_saisie_utilisateur.py` fait du résultat aux appels à `demande_entier` et `demande_chaine` vous allez peut-être rencontrer des erreurs.
Rappelez vous qu'une fonction qui n'a pas de `return` renvoie toujours `None`.

**Implémentez** ensuite votre module.

**Testez** votre implémentation en exécutant votre programme de test qui cette fois-ci doit avoir le comportement attendu.

**Exécutez** directement votre module comme programme principal, que se passe-t-il et pourquoi ?

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
`saisie_utilisateur.py` :
```python
#!/usr/bin/env python3

"""Un premier module fournissant deux fonctions"""


def demande_entier():
    """Demande gentiment un entier à l'utilisateur"""
    print("entrez un entier")
    return int(input())


def demande_chaine():
    """Demande gentiment une chaine de caractères à l'utilisateur"""
    print("entrez un message")
    return input()


def teste_module():
    """Teste les fonctions du module"""
    entier1 = demande_entier()
    entier2 = demande_entier()
    print("la somme vaut", entier1 + entier2)


# Quand l'interpréteur lit un fichier, ce dernier fait deux choses :
#    -1 il définit quelques variables spéciales
#    -2 il exécute le code se trouvant dans le fichier
#
# __name__ est l'une de ces variables spéciales. Celle-ci se voit affectée
# la valeur "__main__" lorsque le fichier est utilisé comme programme principal,
# c'est-à-dire lorsque celui-ci est donné directement en paramètre à l'interpréteur.

print("__name__ =", __name__)

# Lorsque le fichier est utilisé comme un module, c'est-à-dire lorsqu'il est importé
# depuis un autre fichier python, la variable __name__ se voit affectée le nom du module,
# c'est-à-dire le nom du fichier sans l'extension .py.
#
# Le code suivant permet donc d'exécuter la fonction `teste_module` uniquement lorsque
# ce fichier est utilisé comme programme principal et de ne rien faire lorsqu'il est
# importé en tant que module.
#
if __name__ == "__main__":
    teste_module()
```
`test_saisie_utilisateur.py` :
```python
#!/usr/bin/env python3

"""Un programme pour tester le module saisie_utilisateur.py"""

# On importe le module saisie_utilisateur
import saisie_utilisateur

# On appelle la fonction saisie_utilisateur du module saisie_utilisateur
entier = saisie_utilisateur.demande_entier()

# On appelle la fonction demande_chaine du module saisie_utilisateur
chaine = saisie_utilisateur.demande_chaine()

# On affiche le résultat
print(f"{chaine = } et {entier = }")
```
</details>
