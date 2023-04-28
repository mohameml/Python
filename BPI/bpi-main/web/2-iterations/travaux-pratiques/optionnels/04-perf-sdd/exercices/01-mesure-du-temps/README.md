## Énoncé

Quel que soit le langage de programmation que l'on utilise, il est fréquent d'avoir besoin de mesurer le temps écoulé entre deux points du programme pour différentes raisons. Par exemple, dans un jeu on peut vouloir indiquer à l'utilisateur le temps qu'il a pris pour effectuer un coup. Ou alors, au cours du développement d'une application, le programmeur peut souhaiter mesurer le temps d'exécution de deux implémentations différentes d'une même fonctionnalité pour choisir la meilleure.

En Python, la façon la plus simple de mesurer le temps consiste à utiliser le module standard `time`.

Lancer l'interpréteur interactif Python.

```console
[selvama@ensipc215]$ python3
```

Importer le module `time` et afficher l'aide à propos de ce module `help(time)`.

Parcourir cette documentation, notamment la section qui concerne les fonctions fournies par ce module.

Mesurer le temps qui s'écoule lorsque l'on "endort" notre programme Python pour 10 secondes.
Pour information, dans l'interpréteur interactif il est possible d'exécuter plusieurs "instructions" sur une même ligne en les séparant par des points virgules.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Les fonctions du module `time` qui nous intéressent dans cet exercice sont :

- `time.time()` qui renvoie sur des machines Unix le nombre de secondes écoulé depuis le premier janvier 1970 à 0 heure 0 minute 0 seconde ;

- `time.sleep(nb_sec)` qui permet d'endormir l'appelant pendant `nb_sec` secondes.

Pour mesurer le temps entre deux points du programme, il faut donc appeler la fonction `time.time()` au premier point puis au deuxième point et faire une soustraction.

```console
>>> import time
>>> start = time.time(); time.sleep(10); end = time.time()
>>> print(str(end - start) + " secondes se sont écoulées")
10.001639366149902 secondes se sont écoulées
```
</details>
