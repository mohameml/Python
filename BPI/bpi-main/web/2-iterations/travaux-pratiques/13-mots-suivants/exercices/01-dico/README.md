## Qu'est-ce qu'un dictionnaire ?

Qu'est-ce qu'un dictionnaire dans la terminologie des langages de programmation ?
C'est un **type abstrait** permettant d'associer des valeurs à des clés, et dans laquelle une clé n'apparaît qu'une seule fois.
Les clefs elles mêmes peuvent être de n'importe quel type (enfin presque en Python).
Le terme de **tableau associatif** est un synonyme de dictionnaire.

En Python, le type standard `dict` est une implémentation du type abstrait _dictionnaire_, c'est donc une structure de données.
Dans le cadre de BPI, nous **utiliserons** les `dict` de Python sans se préoccuper de savoir comment ils sont implémentés.
Tout ce que nous devons savoir pour le moment est le fait que ces `dict` sont très efficaces : les opérations d'insertion et de recherche s'effectuent en temps constant quelque soit le nombre d'éléments dans le `dict`.
Sachons néanmoins que cette structure de données est une _table de hachage_, que nous étudierons en détails au second semestre dans le cours d'algorithme pour comprendre comment ces coûts constants sont possibles.

Comme une image vaut mille mots, regardons à nouveau le document [TA et SDD](../../../../adt_sdd.pdf) pour bien voir où se situent `dict` et dictionnaire.

L'utilisation d'un dictionnaire est triviale en Python :

```console
>>> dico = {}
>>> dico["manu"] = 42
>>> dico["sophie"] = 17
>>> dico["éric"] = 45
>>> print(dico["sophie"])
17
```

## Travail demandé

Rien du tout, c'était facile non ?
L'objectif de cet exercice était simplement de vous rappeler ce qu'est un dictionnaire est ce qu'est un `dict` Python.

