## Énoncé

Le mardi, c'est cryptographie (la rime fonctionne également avec quasiment tous les jours de la semaine).
Dans ce TP nous nous intéressons au chiffrement par décalage.
Cette méthode, aussi connue sous le nom de "chiffre de César" ou encore `rotx` était utilisée par l'empereur pour ne pas être "sniffé" par la poste impériale.

Le principe est très simple comme l'illustre le schéma ci-dessous.
Une lettre est transformée par un décalage / une rotation d'une certaine quantité (3 sur le schéma) vers la droite dans l'ordre alphabétique.
Lorsque l'on arrive à la fin de l'alphabet, c'est à dire sur `Z` on recommence au début, c'est à dire sur `A`.
Les minuscules restent des minuscules, et les majuscules restent des majuscules.

<br>
![exemple de décalage de 3](rot3.svg)

Les objectifs de ce TP sont les suivants :

- **s'entraîner** à la lecture de documentation d'interface de programmation ;
- **faire connaissance** avec monsieur ASCII et madame UNICODE ;
- **créer et écrire dans un fichier** depuis un programme python.

Votre travail consiste tout d'abord à implémenter les deux fonctions du module `rotx` dont le squelette vous est [fourni ici](rotx.py) et affiché ci dessous.

```python
"""Module d'encodage/décodage par rotation"""


def rot(decalage, lettre):
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractères de taille 1 ;
       - lettre est un soit une lettre majuscule
         soit une lettre minuscule.
    """
    # TODO
    ...


def rot13(lettre):
    """Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    # TODO
    ...
```

Nous vous demandons de vérifier les préconditions et de renvoyer `None` si celles-ci ne sont pas vérifiées.

Ensuite, vous devrez réaliser un programme `decodeur_nom_tp.py` qui effectue les opérations suivantes :

- demande à l'utilisateur de saisir un nom de fichier et crée un fichier portant ce nom dans le répertoire courant (écrasement si fichier déjà existant) ;
- utilise le module `rotx` pour décoder chacune des lettres du nom de ce TP (`nirPrfne`, encodé avec un décalage de 13) et écrit le résultat dans le fichier créé à l'étape précédente ;
- affiche sur la sortie standard votre prénom encodé par un décalage de `4` en utilisant **un seul appel** à la fonction `print`, c'est à dire en exploitant le fait que cette fonction puisse recevoir un nombre variable d'arguments. Comme nous l'avons vu dans le TD2, vous utiliserez le paramètre `sep` de la fonction `print` pour obtenir un affichage sans espaces entre les caractères encodés.

Vous aurez besoin de lire les pages d'aide concernant les mots clefs et les fonctions ci-dessous :

- `chr` aide disponible avec `help(chr)`
- `ord` aide disponible avec `help(ord)`
- `print` aide disponible avec `help(print)`
- `input` aide disponible avec `help(input)`
- `open` aide disponible avec `help(open)`

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
Voici le code d'une correction possible.

Fichier `rotx.py` :
```python
"""Module d'encodage/décodage par rotation"""


def rot(decalage, lettre):
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractères de taille 1 ;
       - lettre est un soit une lettre majuscule
         soit une lettre minuscule.
    """

    # Vérification des préconditions
    if len(lettre) != 1:
        return None
    code_ascii = ord(lettre)
    est_majuscule = code_ascii >= ord("A") and code_ascii <= ord("Z")
    est_minuscule = code_ascii >= ord("a") and code_ascii <= ord("z")
    if not (est_majuscule or est_minuscule):
        return None

    # On rotationne
    if est_majuscule:
        premiere_lettre = "A"
    else:
        premiere_lettre = "a"
    code_ascii_normalise = code_ascii - ord(premiere_lettre)
    code_ascii_rotatione = (code_ascii_normalise + decalage) % 26 + ord(premiere_lettre)

    # On renvoie le caractère correspondant au nouveau code
    return chr(code_ascii_rotatione)



def rot13(lettre):
    """Encode la lettre donnée par rotation de 13 caractères
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    return rot(13, lettre)
```

Fichier `decodeur_nom_tp.py` :
```python
#!/usr/bin/env python3
"""Décodeur du nom du tp"""

import rotx


def main():
    """point d'entrée du programme"""

    # On demande le nom du fichier à l'utilisateur
    nom_fichier = input(
        "Donnez le nom du fichier qui contiendra" ' le résultat puis taper "entrée":\n'
    )

    # On ouvre le fichier puis on écrit dedans
    # La version pythonique c'est "with open"
    # pour ne pas à avoir à faire close
    # mais ça cache plein de choses :
    #   - notion de context manager
    #   - surcharge de __enter()__
    #   - surcharge de __exit()__
    # et on ne veut rien cacher (pour le
    # moment au moins)
    fichier = open(nom_fichier, "w")
    fichier.write(rotx.rot13("n"))
    fichier.write(rotx.rot13("i"))
    fichier.write(rotx.rot13("r"))
    fichier.write(rotx.rot13("P"))
    fichier.write(rotx.rot13("r"))
    fichier.write(rotx.rot13("f"))
    fichier.write(rotx.rot13("n"))
    fichier.write(rotx.rot13("e"))

    # On ferme le fichier
    fichier.close()

    # On affiche l'encodage de son prénom
    # avec un rot 4 en utilisant un seul
    # appel à print et sans variable.
    # La fonction print accepte un nombre
    # variable d'arguments et un argument
    # optionnel sep
    print(
        rotx.rot(4, "M"), rotx.rot(4, "a"), rotx.rot(4, "n"), rotx.rot(4, "u"), sep=""
    )


main()

```

Une correction détaillée en vidéo est également disponible.
Attention, l'opérateur `with` de python est utilisé dans cette vidéo.
Cet opérateur, utilisé avec la fonction `open`, va se charger de garantir que le fichier sera fermé une fois que le flot de contrôle sortira du bloc associé.

<iframe src="https://videos.univ-grenoble-alpes.fr/video/12905-ensimag-bpi-correction-du-mini-projet-nirprfne/?is_iframe=true" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>
</details>
## Exercices

- [Unix is love](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/01-unixislove/index.html)
- [Monsieur propre](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/02-monsieur-propre/index.html)
- [L'âge du capitaine](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/03-age-du-capitaine/index.html)
- [0+0](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/04-somme/index.html)
- [Par où on rentre ?](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/05-par-ou-on-rentre/index.html)
- [Premier module](/1-bases/travaux-pratiques/01-premiers-programmes/exercices/06-modules/index.html)
- [Création de fichiers](/1-bases/travaux-pratiques/02-module-svg-and-co/exercices/01-ecriture-fichier/index.html)
- [Interpréteur interactif](/1-bases/travaux-pratiques/02-module-svg-and-co/exercices/05-interpreteur-interactif/index.html)
