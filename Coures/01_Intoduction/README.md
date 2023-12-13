# cour 01 : Introduction


## 1. **C'est quoi Python ?:**

Python est un langage de programmation polyvalent créé en 1989 par Guido van Rossum aux Pays-Bas , La première version publique de Python a été publiée en 1991.
 

Voici quelques caractéristiques importantes de Python :

1. **Multiplateforme :** Python fonctionne sur divers systèmes d'exploitation, y compris Windows, Mac OS X, Linux, Android, iOS, des mini-ordinateurs comme le Raspberry Pi aux supercalculateurs.

2. **Gratuit :** Python est un logiciel libre et gratuit. Il peut être installé sur autant d'ordinateurs que nécessaire.

3. **Langage de Haut Niveau :** Python est un langage de haut niveau, ce qui signifie qu'il offre une abstraction élevée par rapport au fonctionnement interne de l'ordinateur.

4. **Langage Interprété :** Les scripts Python n'ont pas besoin d'être compilés avant l'exécution, ce qui simplifie le processus de développement et de test.

5. **Orienté Objet :** Python prend en charge la programmation orientée objet, permettant aux développeurs de créer des entités qui représentent des objets du monde réel avec des règles spécifiques et des interactions.

6. **Facilité d'Apprentissage :** Python est réputé pour sa simplicité et sa lisibilité du code, ce qui le rend accessible aux débutants.

7. **Utilisé en Bioinformatique et Analyse de Données :** Python est largement utilisé dans des domaines tels que la bioinformatique et l'analyse de données en raison de ses bibliothèques riches et de sa flexibilité.

8. **Communauté Active :**   [La Python Software Foundation](https://www.python.org/psf-landing/) (PSF) est une organisation à but non lucratif créée pour soutenir et promouvoir le développement du langage de programmation Python. Fondée en 2001, la PSF joue un rôle central dans l'écosystème Python en facilitant la croissance, la diffusion et l'adoption du langage.



## 2.  **Guide d'Installation de Python sur Unix (Linux), macOS et Windows :**

### 2.1  Unix (Linux) :

1. **Ouvrez le Terminal :** Utilisez le terminal de votre distribution Linux.

2. **Vérifiez si Python est déjà installé :**
   ```bash
   python3 --version
   ```
   Si Python n'est pas installé, vous verrez un message d'erreur.

3. **Installez Python :**
   - Sur Ubuntu ou Debian :
     ```bash
     sudo apt-get update
     sudo apt-get install python3
     ```


4. **Vérifiez l'Installation :**
   ```bash
   python3 --version
   ```

### 2.2 macOS :

1. **Ouvrez le Terminal :** Utilisez l'application Terminal.

2. **Vérifiez si Python est déjà installé :**
   ```bash
   python3 --version
   ```
   Si Python n'est pas installé, vous verrez un message d'erreur.

3. **Installez Homebrew (si non installé) :**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
   ```

4. **Installez Python avec Homebrew :**
   ```bash
   brew install python
   ```

5. **Vérifiez l'Installation :**
   ```bash
   python3 --version
   ```

### 2.3 Windows :

1. **Téléchargez le Programme d'Installation :**
   - Accédez au site officiel de Python : [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Téléchargez le programme d'installation pour Windows.

2. **Lancez le Programme d'Installation :**
   - Exécutez le programme d'installation téléchargé.
   - Assurez-vous de cocher l'option **Add Python to PATH** pendant l'installation.

3. **Terminez l'Installation :**
   - Suivez les instructions de l'installateur.

4. **Vérifiez l'Installation :**
   - Ouvrez le "Command Prompt" ou "PowerShell" et entrez :
     ```bash
     python --version
     ```

### 2.4 Vérification de l'Installation sur tous les Systèmes :

1. **Lancez l'Interpréteur Python :**
   - Ouvrez le terminal ou l'invite de commande.
   - Tapez :
     ```bash
     python3
     ```
     ou
     ```bash
     python
     ```

2. **Vérifiez la Version :**
   - Vous devriez voir le prompt Python (>>>). Vérifiez la version affichée.

3. **Quittez l'Interpréteur :**
   - Tapez `exit()` ou utilisez Ctrl + D (sur Unix) ou Ctrl + Z (sur Windows) pour quitter l'interpréteur.

Félicitations ! Python est maintenant installé sur votre système. Vous pouvez commencer à écrire et exécuter des scripts Python.


## 3. **Un éditeur de code :``VSCode``**

Un éditeur de code est un outil logiciel qui vous permet d'écrire, de modifier et de visualiser du code source. Microsoft Visual Studio Code (VSCode) est un éditeur de code source gratuit et très populaire développé par Microsoft. Voici un guide d'installation de VSCode :



### 3.1 Pour Windows :

1. **Téléchargez le Programme d'Installation :**
   - Accédez au site officiel de VSCode : [https://code.visualstudio.com/](https://code.visualstudio.com/).
   - Téléchargez le programme d'installation pour Windows.

2. **Lancez le Programme d'Installation :**
   - Exécutez le programme d'installation téléchargé.
   - Suivez les instructions de l'installateur.

3. **Options d'Installation (Optionnel) :**
   - Assurez-vous de cocher l'option **Add to PATH** pendant l'installation pour pouvoir exécuter VSCode depuis le terminal ou l'invite de commande.

4. **Terminez l'Installation :**
   - Cliquez sur "Finish" pour terminer l'installation.

### 3.2  Pour macOS :

1. **Téléchargez le Programme d'Installation :**
   - Accédez au site officiel de VSCode : [https://code.visualstudio.com/](https://code.visualstudio.com/).
   - Téléchargez le programme d'installation pour macOS.

2. **Lancez le Programme d'Installation :**
   - Ouvrez le fichier téléchargé (généralement un fichier `.dmg`).
   - Faites glisser l'icône de VSCode vers le dossier "Applications".

3. **Installation via Homebrew (Optionnel) :**
   - Si vous utilisez Homebrew, vous pouvez également installer VSCode avec la commande :
     ```bash
     brew install --cask visual-studio-code
     ```

### 3.3  Pour Linux :

1. **Téléchargez le Programme d'Installation :**
   - Accédez au site officiel de VSCode : [https://code.visualstudio.com/](https://code.visualstudio.com/).
   - Téléchargez le programme d'installation pour Linux.

2. **Extrayez l'Archive :**
   - Ouvrez le terminal.
   - Naviguez jusqu'au répertoire où vous avez téléchargé l'archive.
   - Extrayez le contenu avec la commande :
     ```bash
     tar -xzf nom_de_l_archive.tar.gz
     ```

3. **Lancez VSCode :**
   - Naviguez dans le répertoire extrait.
   - Exécutez VSCode avec la commande :
     ```bash
     ./code
     ```


## 4 **Mon premier programme :**

- Voici un exemple simple pour vous aider à démarrer. C'est un programme Python de base qui demande à l'utilisateur son nom, puis lui donne un message de bienvenue. Vous pouvez l'exécuter dans un environnement Python, comme le terminal ou l'IDE VSCode.

```python

nom_utilisateur = input("Entrez votre nom : ")

print("Bienvenue, " + nom_utilisateur + " ! C'est votre premier programme en Python.")

```

Le programme vous demandera d'entrer votre nom, puis affichera un message de bienvenue personnalisé. C'est une introduction simple, mais cela montre comment utiliser l'entrée utilisateur, les variables et l'affichage dans Python.


## 5. **Le shebang:** 


- Le shebang, également appelé hashbang, est un caractère spécial suivi d'une séquence de caractères que l'on place au début d'un fichier script exécutable pour spécifier l'interpréteur qui doit être utilisé pour exécuter le script. Le shebang est suivi du chemin complet ou de la commande de l'interpréteur.

- En général, le shebang est utilisé dans les scripts shell (comme ceux en Bash, Python, Perl, etc.) et dans d'autres types de scripts interprétés. C'est une directive destinée au système d'exploitation pour lui indiquer comment exécuter le script.


- Voici comment il fonctionne :

    1. Lorsque vous exécutez un script qui contient un shebang, le système d'exploitation utilise l'interpréteur spécifié après le shebang pour exécuter le script.

    2. Par exemple, si votre script Python commence par `#!/usr/bin/env python3`, cela indique au système d'utiliser l'interpréteur Python 3 pour exécuter le script.

    3. Le shebang est ignoré lorsque vous exécutez un script dans un environnement qui n'interprète pas les scripts (comme lorsque vous ouvrez le fichier dans un éditeur de texte).

- Exemple de shebang dans un script Python (`script.py`) :

    ```python
    #!/usr/bin/env python3

    print("Hello, World!")
    ```

    Cela dit au système d'utiliser l'interpréteur Python 3 pour exécuter ce script. Vous pouvez ensuite rendre le script exécutable avec `chmod +x script.py` et l'exécuter directement avec `./script.py`.




- Voici une explication détaillée  :

    1. **Shebang dans le fichier `main.py` :**
    Ajoutez la ligne suivante au début de votre fichier `main.py` :
    ```python
    #!/usr/bin/env python3
    ```
    Cela spécifie le chemin vers l'interpréteur Python 3 à utiliser pour exécuter le script.

    2. **Rendre le fichier exécutable :**
    Utilisez la commande `chmod` pour rendre le fichier exécutable :
    ```bash
    chmod u+x main.py
    ```

    3. **Exécution du script :**
    Vous pouvez maintenant exécuter le script directement à partir du terminal :
    ```bash
    ./main.py
    # ou :
    python3 main.py 
    ```
    Si le chemin du fichier est inclus dans la variable d'environnement `PATH`, vous pouvez également exécuter le script sans spécifier le chemin complet :
    ```bash
    main.py
    ```
