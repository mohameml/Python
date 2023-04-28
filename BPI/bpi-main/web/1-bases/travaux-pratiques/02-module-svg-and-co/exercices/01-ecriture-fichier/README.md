## Énoncé

Dans les exercices précédents, nous avons utilisé la fonction `print` et des redirections pour générer des fichiers à partir de programmes Python.
L'objectif de cet exercice est de vous montrer qu'il est possible de créer directement des fichiers depuis un programme Python.

À l'aide de la fonction `open`, dont la documentation est donnée ci-dessous, écrivez un programme `i_am_a_file_master.py` qui effectue les opérations suivantes :

- crée un fichier `toto.txt` dans le répertoire courant  (si le fichier existe déjà, celui-ci est écrasé) ;
- écrit deux lignes de texte quelconques dans le fichier en utilisant la méthode `write` pour la première ligne et la fonction `print` pour la seconde. Les documentations pour `write` et `print` sont données ci-dessous. Attention, `write` est une méthode alors que `print` est une fonction. Autrement dit `write` doit être appelée sur un objet, par exemple `mon_fichier.write("blabla")`.
- ferme le fichier en appelant la méthode `close` sur le fichier renvoyé par la fonction `open`.

```console
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise IOError upon failure.

    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)

    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
      ========= ===============================================================

    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
```

```console
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

```console
write(text)
    Write string to stream.
    Returns the number of characters written (which is always equal to
    the length of the string).
```

**Testez** votre programme en vérifiant que le fichier `toto.txt` est bien créé et que son contenu est bien celui attendu.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>
`i_am_a_file_master.py` :

```python
#!/usr/bin/env python3

"""Un programme pour découvrir la manipulation de fichier en Python"""


def main():
    """Fonction principale."""

    # Création du fichier pour écriture avec écrasement si celui-ci existe
    # déjà grace au mode "w"
    fichier_toto = open("toto.txt", "w")

    # Écriture d'une première ligne dans le fichier à l'aide de la fonction
    # write.
    # "\n" signifie retour à la ligne.
    # Contrairement à la fonction print qui par défaut ajoute un retour
    # à la ligne après le texte affiché, write nécessite de le dire
    # explicitement.
    fichier_toto.write("une première ligne originale\n")

    # Écriture d'une deuxième ligne dans le fichier à l'aide de la fonction
    # print en utilisant le paramètre optionnel file.
    print("une seconde ligne un peu plus originale encore", file=fichier_toto)

    # Les fichiers sont des ressources fournies par le système d'exploitation
    # Il faut impérativement rendre ces ressources au système dès lors que
    # nous n'en avons plus besoin : c'est l'objectif du close ici.
    fichier_toto.close()


main()
```
</details>
