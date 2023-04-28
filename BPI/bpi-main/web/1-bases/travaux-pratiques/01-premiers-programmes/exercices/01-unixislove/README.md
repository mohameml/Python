## Énoncé


Cet exercice a pour but de créer un premier programme Python, et surtout de l'exécuter en faisant le lien avec le stage Unix.

Avant tout, et en vue de bien structurer les fichiers sur le semestre, créez un répertoire pour la
matière et un sous répertoire pour le TP1 dans votre dossier personnel (home).

Pour ce faire, ouvrez un nouveau terminal puis :

1. assurez vous que vous trouvez à la racine (répertoire `home` ou `~`) ;
2. créez un répertoire pour la matière : `mkdir BPI` (make directory) ;
3. déplacez vous dans le répertoire créé : `cd BPI` (change directory) ;
4. créez un répertoire pour le TP : `mkdir TP1` ;
5. déplacez vous dans le répertoire du TP : `cd TP1`.

À tout moment vous pouvez vérifier où vous vous trouvez avec la commande `pwd` (path working directory).
Et vous pouvez voir le contenu du répertoire courant avec la commande `ls` (list).
À chaque début de TP vous créerez de la même manière un nouveau répertoire.

Maintenant vous allez créer votre premier programme.
Pour ce faire :

1. ouvrez votre éditeur de texte favori pour créer un fichier `le_nom_que_vous_voulez.py` dans le répertoire TP1 ;
2. écrivez dans ce fichier un programme Python affichant ce qui vous passe par la tête sur la sortie standard ;
3. rendez le programme exécutable : `chmod u+x le_nom_que_vous_voulez.py` ;
4. exécutez le programme dans un terminal : `python le_nom_que_vous_voulez.py` ou directement `./le_nom_que_vous_voulez.py` si vous avez placé un `shebang` en première ligne de votre programme comme vu en TD.

Après l'exécution de votre programme, vous **devez voir** dans votre terminal le message qui vous est passé par la tête à l'étape 2.
Si ce n'est pas le cas, quelque chose s'est mal passé et il faut donc **comprendre** quel est le problème.

Enfin, effectuez une redirection vers un fichier à l'aide de l'une des deux commandes suivantes en fonction la présence ou non d'un `shebang` dans votre programme :
```console
[selvama@ensipc215 unixislove]$ python le_nom_que_vous_voulez.py > unixislove.log
[selvama@ensipc215 unixislove]$ ./le_nom_que_vous_voulez.py > unixislove.log
```

Quel est l'effet de cette redirection ?

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

Et oui, le stage Unix nous est **déjà** utile :)

Voici notre programme premier programme Python que nous avons décidé d'appeler `un_nom_qui_en_jette.py`.

```python
#!/usr/bin/env python3

"""Mon premier programme python."""

# La fonction print affiche la chaîne de caractères passée
# en paramètre sur la sortie standard.
print("On n'est pas bien là ?")
```

Pour exécuter ce programme :

1. Le fichier du programme doit être _exécutable_ (`chmod +x un_nom_qui_en_jette.py`) ;
2. On doit indiquer au système _quel interpréteur utiliser pour interpréter son contenu_.

C'est le rôle de la première ligne du fichier :

```python
#! /usr/bin/env python3
```

Cette ligne, aussi appelée _shebang_, indique au système d'exploitation que ce fichier exécutable n'est pas un fichier binaire, mais un script sous forme d'un fichier texte.
Par défaut, le système tentera de faire interpréter le contenu de ce script par l'interprète de commandes qui l'exécute.
Autrement dit, sans cette ligne, le contenu du fichier `un_nom_qui_en_jette.py` serait interprété par le shell qui exécute la commande :

```console
[selvama@ensipc215 unixislove]$ ./un_nom_qui_en_jette.py
```

Le contenu du fichier serait donc interprété comme étant un script shell, et plus un programme Python, ce qui au mieux, ferait n'importe quoi, à peu près.
Avec un shebang correct, l'exécution de `./un_nom_qui_en_jette.py` devient équivalente à lancer depuis le terminal la commande `/usr/bin/env python3 ./un_nom_qui_en_jette.py`.

Bien que cela soit moins pratique, il est également possible de lancer un programme Python en invoquant directement l'intrepréteur :

```console
[selvama@ensipc215 unixislove]$ python3 un_nom_qui_en_jette.py
```

Dans ce cas, même pas besoin de positionner les droits en exécution sur le fichier `un_nom_qui_en_jette.py`.

!!! info "Et /usr/bin/env, alors ?"
    Le shebang doit contenir **le chemin absolu** vers l'interpréteur à utiliser, par exemple en écrivant `#! /usr/bin/python3`.
    Mais comment faire pour exécuter notre script sur une machine où `python3` a été installé à un emplacement différent, par exemple `/opt/local/bin/python3` ?

    Les plus perspicaces d'entre vous auront remarqué la présence de la commande `/usr/bin/env` devant notre interpréteur Python préféré.
    Cette commande augmente la portabilité de notre script, en indiquant qu'on souhaite utiliser le programme `python3`, quel que soit son emplacement sur la machine.

    Côté utilisateur, il faut que le chemin où est installé `python3` se trouve dans `PATH`. Si ça ne vous dit rien, il est temps d'aller (re)lire un bout du stage Unix de rentrée : [section 8.5](http://systemes.pages.ensimag.fr/www-unix/html/index.html).


Concernant la redirection avec le symbole `>`, on observe que le message n'est plus affiché sur le terminal.
En effet, la redirection `> unixislove.log` remplace la sortie standard "terminal" par le fichier `unixislove.log`.
Le message donné en argument de l'appel de fonction `print` est donc "imprimé" dans le fichier `unixislove.log`.
Il suffit d'ouvrir ce fichier avec un éditeur de texte, celui que l'on préfère, pour s'en convaincre.

</details>
