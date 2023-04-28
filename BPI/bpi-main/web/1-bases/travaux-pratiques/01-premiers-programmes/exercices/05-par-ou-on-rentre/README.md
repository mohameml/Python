## Énoncé

L'objectif de cet exercice est de bien comprendre la notion de point d'entrée d'un programme.
Il est essentiel de savoir identifier quelle sera la première ligne exécutée par l'interpréteur lorsque notre programme sera lancé.

En fonction du langage utilisé il peut y avoir quelques différences concernant le point d'entrée, néanmoins celles-ci restent mineures.
Si vous arrivez à résoudre et comprendre cet exercice, vous serez donc en mesure d'identifier le point d'entrée d'un programme écrit dans n'importe quel langage ou dans le pire cas en mesure de vous poser les bonnes questions pour l'identifier.

Uniquement en lisant le code contenu dans le fichier `on_rentre_par_la.py` [disponible ici](on_rentre_par_la.py) et affiché ci dessous, c'est à dire **sans l'exécuter**, anticipez l'affichage engendré lorsque on exécute ce code :

```python
#!/usr/bin/env python3

"""Un programme pour comprendre la notion de point d'entrée en Python"""

def fait_un_bidule():
    """Affiche un message de bienvenue"""
    print("ترحيب  en BPI")


message = "bienvenue"

def fait_un_truc():
    """Affiche un message de bienvenue"""
    print(message + " à l'Ensimag")


print("on vous souhaite la " + message)

def fait_un_autre_truc():
    """Affiche un autre message de bienvenue"""
    print(message + "à Grenoble, la plus belle ville du monde")


def main():
    """LA fonction principale"""
    print("Je suis le MAIN, et j'appelle ... fait_un_autre_truc")
    fait_un_autre_truc()


message = "welcome"

fait_un_bidule()

fait_un_truc()
```

**Testez** votre conclusion en exécutant le programme.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici une version commentée de `on_rentre_par_la.py` :
```python
#!/usr/bin/env python3

"""Un programme pour comprendre la notion de point d'entrée en Python"""

# En Python, l'interpréteur commence par lire la première ligne, en ignorant
# les commentaires. Il va donc commencer par lire la ligne "def fait_un_bidule():"
# ci dessous. Comme cette ligne est une définition, le code n'est pas exécuté
# à ce moment là mais simplement "lu".
def fait_un_bidule():
    """Affiche un message de bienvenue"""
    print("ترحيب  en BPI")


# La première ligne vraiment exécutée est donc la ligne suivante qui
# crée la variable globale message
message = "bienvenue"

# Ici nous avons encore une définition donc rien à exécuter.
def fait_un_truc():
    """Affiche un message de bienvenue"""
    print(message + " à l'Ensimag")


# Ensuite, l'interpréteur appelle la fonction print. Le message
# associé va donc être affiché sur la sortie standard.
print("on vous souhaite la " + message)

# Ici nous avons encore une définition donc rien à exécuter.
def fait_un_autre_truc():
    """Affiche un autre message de bienvenue"""
    print(message + "à Grenoble, la plus belle ville du monde")


# Ici nous avons encore une définition donc rien à exécuter. Le fait que
# la fonction s'appelle main ne change rien. Cette fonction est donc une
# fonction comme les autres. A la différence de langages comme le C, où
# le point d'entrée du programme est identifié par une fonction s'appelant
# toujours main, en Python le point d'entrée est toujours la première ligne
# du fichier, quelle qu'elle soit.
def main():
    """LA fonction principale"""
    print("Je suis le MAIN, et j'appelle ... fait_un_autre_truc")
    fait_un_autre_truc()


# Ensuite l'interpréteur affecte une nouvelle valeur à la variable message
message = "welcome"

# L'interpréteur rencontre un appel de fonction, il va donc sauter à la
# première ligne de celle-ci, exécuter les lignes de cette fonction
# jusqu'à l'instruction return, puis se déplacer dans le code "juste après"
# l'appel de fonction. Une fonction ne disposant pas d'instruction return
# se comporte comme la même fonction à laquelle on ajoute en dernière ligne :
# return None
fait_un_bidule()
# On se trouve ici "juste après" l'appel fait_un_bidule()
# La dernière instruction à avoir été exécutée était le retour de fonction (ici,
# return None ajouté implicitement puisque la fonction ne retourne rien).

# Enfin, l'interpréteur rencontre un deuxième appel de fonction, qui est exécuté
# selon le même mécanisme que l'appel de fonction précédent.
fait_un_truc()
```
</details>
