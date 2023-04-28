## Énoncé

Jusqu'à présent, pour pouvoir utiliser notre module `svg`, nous avons copié le fichier `svg.py` à côté du programme utilisant le module.

Dans cet exercice, vous devez répondre aux questions suivantes :

- Quel est le problème de la copie ?
- Quel "outil" vu en Unix pouvez-vous utiliser pour éviter la copie ?
- Connaissez-vous une solution plus élégante à ce problème ?

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Le problème de la copie concerne la maintenance du code.
Dés lors que nous avons plus d'une version d'un même code quel qu'il soit, la correction d'un problème ou l'ajout d'une nouvelle fonctionnalité ne pourra plus se faire à un **unique** endroit.

Une solution "Unix" simple consiste à utiliser des liens symboliques (commande `ln -s`) afin d'avoir un fichier `svg.py` partout ou nous en avons besoin qui "pointe" sur l'unique fichier `svg.py` se situant ailleurs.

Enfin, la solution la plus propre consiste à utiliser la variable d'environnement `PYTHONPATH` pour indiquer à l'interprète où chercher les modules qui nous sont propres.
Par exemple, la commande suivante nous permet d'utiliser tous les modules se trouvant dans le répertoire `mes-modules-pythons` de notre home :

```console
[selvama@ensipc215]$ export PYTHONPATH=~/mes-modules-python
```
</details>

