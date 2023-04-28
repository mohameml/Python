## Énoncé

Nous avons vu dans l'exercice [unixislove](../01-unixislove) comment exécuter un programme Python enregistré dans un fichier `.py` soit en utilisant un shebang, soit en invoquant explicitement l'interpréteur Python.

Il est également possible d'exécuter du code python sans avoir à l'enregistrer dans un fichier.
Pour cela, il suffit de lancer l'interpréteur en mode interactif, simplement en ne spécifiant aucun fichier à exécuter :

```console
[selvama@ensipc215]$ python3
```

Une fois que vous avez lancé l'interpréteur en mode interactif, vous pouvez taper directement du code Python dans celui-ci et donc voir instantanément le résultat.
C'est très pratique lorsque l'on code, notamment en phase d'apprentissage du langage, pour s'assurer que ce que l'on fait est correct.
De plus, l'interpréteur interactif permet d'avoir accès à la documentation des fonctions standards, **sans avoir à aller sur internet**, c'est beau non ?

Essayez de jouer avec l'interpréteur interactif, et pensez à le lancer dès que vous avez besoin de faire un test sur une fonctionnalité particulière du langage ou pour obtenir de la documentation.

Voici un exemple d'utilisation de l'interpréteur interactif :

```console
>>> 42 + 42
84
>>> res_maths = (17, 9)
>>> res_maths[1]
9
>>> help(str)

>>> import random
>>> help(random.randint)

>>> def genere_entier_aleatoire():
...     return random.randint(0, 42)
...
>>> genere_entier_aleatoire()
22
>>>
```

Enfin, essayez d'importer le module `this` dans l'interpréteur interactif. Qu'en pensez-vous ?

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
```raw
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>
```
</details>
