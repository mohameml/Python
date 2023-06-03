Le projet est à réaliser **individuellement** et sera **terminé le 7/12/2021 à 23h59**.

Vous travaillerez avec `git`, donc rendez-vous ici [https://gitlab.ensimag.fr](https://gitlab.ensimag.fr) dans votre dépôt `projet_bpi_xxx` **une fois que vous aurez lu attentivement cette page jusqu'au bout**.

## Description haut niveau

Le programme que vous allez écrire, qui se décomposera en deux fichiers Python, doit :

- calculer une valeur approximative de π à l'aide d'une simulation de Monte-Carlo ;
- générer une image animée représentant la simulation comme ci-dessous.

![Image animée](pi-sujet.gif)

Pour calculer une approximation de π à l'aide d'une simulation de Monte-Carlo en tirant `n` points aléatoires (comme au casino), l'algorithme simple que vous utiliserez est le suivant :

- initialiser un compteur à 0 ;
- pour `i` allant de `1` à `n` :
    + générer un point aléatoire `(x,y)` dans un carré de longueur 2 et de centre `(0,0)`. Pour cela il suffit de générer `x`  dans `[-1,1]` et `y` dans `[-1,1]` ;
    + si le point est dans le cercle de centre `(0,0)` et de rayon `1`, ajouter 1 au compteur ;
- l'estimation de π/4 est la valeur du compteur divisée par le nombre `n`.

Pour en savoir plus sur le sujet, nous nous référerons au très clair [billet de  Bruno Tuffin](https://interstices.info/la-simulation-de-monte-carlo/) sur le site [interstices.info](https://interstices.info/https://www.interstices.info).

Pour la création de l'image animée, nous générerons des images au format `PPM` puis nous les agrégerons comme expliqué dans la prochaine section.

## Travail à réaliser

Le travail à réaliser se décompose en deux parties.

### Première partie : cœur de la simulation

La première partie du projet consiste à écrire un module Python `approximate_pi.py` qui sera le cœur de notre simulation.
Autrement dit, ce module se charge uniquement du travail en lien avec le calcul d'une approximation de π sans se préoccuper des questions de visualisation sous forme d'image.

Le module `approximate_pi.py` doit fournir au programme `draw.py` décrit ci-dessous :

- les points aléatoires tirés avec `x`  appartenant à `[-1,1]` et `y` appartenant à `[-1,1]` pour tous les points ;
- l'information indiquant si un point aléatoire est dans le cercle unitaire ou non.

Il est demandé que le module `approximate_pi.py` soit également un programme exécutable permettant de donner une approximation de π en utilisant un nombre de points donné sur la ligne de commande tel qu'illustré ci-dessous :

```console
[selvama@ensipc215 projet_bpi]$ ./approximate_pi.py 100000000
3.14152532
```

### Deuxième partie : génération d'images `PPM` puis d'un `GIF`

Nous allons maintenant utiliser `approximate_pi.py` comme un module pour passer aux choses sérieuses, c'est à dire à la génération de notre image animée représentant une simulation.
Le travail demandé consiste à écrire un programme Python `draw.py` qui :

- reçoit 3 arguments **dans l'ordre suivant** depuis la ligne de commande :
    + la taille de l'image en pixels, qui est carrée donc un seul entier qui devra être supérieur ou égale à 100 ;
    + le nombre de point `n` à utiliser dans la simulation, qui devra être supérieur à 100 ;
    + le nombre de chiffres après la virgule à utiliser dans l'affichage de la valeur approximative de π, qui devra être compris entre 1 et 5.
- implémente une fonction `generate_ppm_file(...)` qui génère une image au [format PPM](https://en.wikipedia.org/wiki/Netpbm#File_formats). L'image doit montrer les points qui sont à l'intérieur du cercle d'une certaine couleur, les points qui sont à l'extérieur du cercle d'une autre couleur et la valeur approchée de π  comme l'illustre l'image animée ci-dessus. La couleur de fond de l'image, blanc sur l'image ci-dessus, peut également être n'importe quoi d'autre. Le nom de l'image doit être au format `img0_3-13776.ppm` : `0` indique le numéro de l'image dans la simulation totale (`0` en l'occurrence, donc la première image) et `3-13776` correspond à l'approximation courante de π en utilisant le nombre de chiffres après la virgule spécifié sur la ligne de commande (5 en l'occurrence). La signature de la fonction n'est volontairement pas donnée pour que chacun puisse réaliser sa propre solution ;
- génère une image `PPM`, en utilisant la fonction `generate_ppm_file`,  représentant l'état courant de la simulation à chaque fois qu'un dixième du nombre total de points a été tiré. Dix images seront donc générées. On le répète, les points doivent êtres fournis par le module `approximate.py`. Comme ce dernier s'occupe uniquement du cœur de la simulation et n'a donc pas connaissance de la taille de l'image, la conversion des points avec `x`  appartenant à `[-1,1]` et `y` appartenant à `[-1,1]` vers des pixels dans l'image doit se faire dans `draw.py`;
- utilise le programme `convert` pour créer une image animée au format `GIF` à partir des dix images `PPM`.

Si plusieurs point tirés par `approximate_pi.py` "tombent" sur le même pixel alors que certains points sont dans le cercle et d'autres non (ce peut arriver pour les points à la frontière du cercle), alors `draw.py` doit dessiner le pixel de la couleur associée au **dernier** point tiré correspondant au pixel.

### Consignes à respecter

**Il est demandé de respecter scrupuleusement les consignes suivantes :**

- respecter précisément les noms des fichiers Python et images indiqués ci-dessus ;
- votre programme `draw.py` doit lancer une exception sans l'attraper si une ou plusieurs entrées incorrectes sont données par l'utilisateur sur la ligne de commande. Autrement dit, si l'utilisateur lance le programme avec `./draw.py tutu 10000 4` ou avec `./draw.py -800 100000 4` il doit voir dans son terminal une erreur indiquant l'exception qui a été lancée ainsi que la pile d'appels. L'interpréteur se charge de tout cet affichage pour nous quand on lance une exception et que celle-ci n'est jamais attrapée et donc remonte jusqu'au sommet de la pile d'appels ;
- utiliser des `f-string` quand cela est pertinent ;
- ne PAS lancer `eog` automatiquement depuis votre programme python ;
- votre programme `draw.py` doit créer les images dans le répertoire courant et non pas dans un sous dossier ;
- utiliser le module `subprocess` pour générer l'image animée `GIF` à partir des images `PPM` ;
- il est interdit d'utiliser `numpy` ;
- il est interdit d'utiliser un module externe pour rajouter le texte de π par dessus votre image. Autrement dit l'objectif est de coder cet affichage *à la main* en pensant à l'afficheur 7 segments de votre gadget électronique préféré ;
- idéalement,  la taille du texte de π par dessus votre image s'adapte à la taille de l'image.

## Tests automatiques

Des tests automatiques seront lancés régulièrement sur la dernière version de votre code afin d'évaluer les critères ci-dessous. Les résultats de ces tests sont [disponibles ici](https://bpi-prof.pages.ensimag.fr/projet_bpi_eval_overview/).

Critères :

- justesse du code : le programme réalise bien ce qui est demandé
- respect des consignes ci-dessus ;
- qualité du code : utilisation d'au moins deux modules tel que demandé ci-dessus et utilisation de `pylint`. Le fichier de configuration pour `pylint`  est [disponible ici](pylint-config). Ce fichier doit être placé à la racine de votre répertoire personnel et doit être nommé `.pylintrc`;
- performance (temps et utilisation mémoire) du programme ;
- complexité en calcul du programme en fonction des entrées ;
- complexité en mémoire du programme en fonction des entrées ;
- le poids des images `PPM` générées (c'est à dire le nombre d'octets sur le disque dur) ;
- respect des consignes ci-dessous.

## Rendu

À la fin du projet, dans votre dépôt git vous devez avoir :

- votre code, c'est à dire **uniquement** vos fichiers Python (attention aux fichiers cachés dont le nom commence par `.`) ;
- un rapport de **deux pages maximum**.

**Ne pas mettre votre nom ni dans le rapport ni dans les fichiers Python.**

Dans le rapport vous présenterez, en argumentant, l'état de votre programme vis à vis des critères ci-dessus.
Comme le rapport est limité à deux pages, **il ne faut surtout pas reprendre le sujet** mais présenter directement vos arguments.

## Correction
<details markdown="1">
<summary>Cliquez ici pour révéler la correction.</summary>

### `approximate_pi.py`

Les points clés sont les suivants :

- la fonction génératrice `get_points(nb_points)` renvoie un itérateur permettant de tirer aléatoirement `nb_point` points `(x, y)` avec x dans `[-1, 1]` et y dans `[-1, 1]`. En plus du point courant, l'itérateur renvoie un booléen indiquant si le point courant est dans le cercle ou non ainsi que le nombre de points déjà tirés appartenant au cercle ;

- lorsque `approximate_pi.py` est utilisé comme programme principal, on crée simplement un itérateur avec la fonction génératrice `get_points(nb_points)` puis on le parcours entièrement sans rien faire juste pour récupérer le nombre total de points dans le cercle. Avec cette valeur on calcul l'approximation de π. La complexité spatiale du programme est donc constante et la complexité temporelle est une fonction linéaire du nombre de points.

```python
#!/usr/bin/env python3


"""Heart of the simulation.

This module provides:

- a Point type made of two integers called x and y
- a function to fix the randomness of point generation
- a function to generate a random point
- a function to approximate the value of PI from points
"""

import math

import random
import collections
import sys

# A point in a 2D plane
Point = collections.namedtuple("Point", ["x", "y"])


def fix_points_from_random(number):
    """Fix the random number generation for reproductibility.

    The generated sequence of points is the same every time
    this function is called with the same number before the
    first call to create_random_point.
    """
    random.seed(number)


def create_random_point():
    """Return a new random point.

    The point is in a square of size 2 centered at (0, 0),
    hence point.x ∈ [-1, 1] and point.y ∈ [-1, 1].
    """
    x_coord = random.uniform(-1, 1)
    y_coord = random.uniform(-1, 1)
    return Point(x_coord, y_coord)


def get_points(nb_points):
    """Generator function for the simulation.

    Returns an iterator of tuples made of :
        - a point
        - a boolean telling if the point
          is in the unit circle or not
        - the number of points in the circle
          up to now
    """
    nb_points_in_circle = 0
    for _ in range(nb_points):
        point = create_random_point()
        in_circle = is_in_circle(point)
        nb_points_in_circle += int(in_circle)
        yield point, in_circle, nb_points_in_circle


def is_in_circle(point):
    """Return True if the point is in the unit circle and False otherwise."""
    dist_from_center = math.sqrt((point.x - 0.0) ** 2 + (point.y - 0.0) ** 2)
    return dist_from_center <= 1


def main():
    """Program's entry point."""

    # Program's inputs is given on the command line
    if len(sys.argv) != 2:
        print("utilisation ./simulator.py nb_points")
        sys.exit(-1)
    nb_points = int(sys.argv[1])
    if nb_points <= 0:
        raise ValueError("all parameters must be integers " "strictly greater than 0")

    # Fix random in the simulator
    fix_points_from_random(42)

    # Main simulation loop using generator function
    # We now that nb_points > 0, so we say it to pylint
    # pylint: disable=undefined-loop-variable
    for last in get_points(nb_points):
        pass
    # We only care about the number of points in the circle
    _, _, nb_points_in_circle = last

    # Approximate the value of PI from the points
    pi_approx = 4 * nb_points_in_circle / nb_points
    print(pi_approx)


if __name__ == "__main__":
    main()
```

### `draw.py`

Voici ci-dessous trois propositions de correction.
D'autres solutions faisant des choix différents impliquant éventuellement des complexité mémoire et temps de calcul différentes, néanmoins toutes aussi raisonnables sont possibles.
N'hésitez pas à contacter vos enseignants si vous voulez discuter d'une solution particulière.

Les trois solutions proposées génère des images `PPM` au format binaire, qui est le format le plus compact.

#### Solution 1 : utilisation d'un `bytearray`
La première solution stocke toute l'image en mémoire sous la forme d'un `bytearray` et écrit directement les pixels au format binaire dans ce `bytearray`.
La complexité temporelle est quadratique en fonction de la largeur de l'image et linéaire en fonction du nombre de points.
La complexité spatiale est quadratique en fonction de la largeur de l'image et constante en fonction du nombre de points.

```python
#!/usr/bin/env python3


"""Monte Carlo simulation to approximate π."""

# Imports from standard library
import collections
import subprocess
import sys

# Then, imports from our own modules
import approximate_pi

# Type for digit bars used to draw the "text"
# of the π approximation as in a 7 segments
# digital screen.
# A digit bar is a rectangle inside a slot,
# hence its coordinate are defined considering (0,0)
# is the top left of the slot.
# A slot is where a single number is drawn.
DigitBar = collections.namedtuple("DigitBar", ["top_left", "width", "height"])

# Type for representing a pixel
Pixel = collections.namedtuple("Pixel", ["line", "col", "in_circle"])


def is_in_bar(line, col, barr):
    """Return True if (line, col) is in barr else False."""
    if (
        barr.top_left.col <= col <= barr.top_left.col + barr.width
        and barr.top_left.line <= line <= barr.top_left.line + barr.height
    ):
        return True
    return False


def is_in_bars(line, col, bars):
    """Return True if (line, col) is in one of the bar in bars else False."""
    for barr in bars:
        if is_in_bar(line, col, barr):
            return True
    return False


def get_pi_rectangle(image_size):
    """ "Return the rectangle in the image where to draw PI text."""

    # The PI rectangle depends on image's size
    # The height is height_prop of the image size
    # The width is width_prop of the image size
    pi_rect_height_prop = 1 / 12
    pi_rect_width_prop = 1 / 6
    pi_rect_top_left = Pixel(
        int(image_size * (1 - pi_rect_height_prop) / 2),  # line
        int(image_size * (1 - pi_rect_width_prop) / 2),  # col
        False,
    )
    pi_rect_width = int(image_size * pi_rect_width_prop)
    pi_rect_height = int(image_size * pi_rect_height_prop)
    return pi_rect_top_left, pi_rect_width, pi_rect_height


def get_pi_pixels_it(pi_approx_s, image_size):
    """Return an iterator over the pixels to draw in black for PI text.

    The pixels are returned sorted by line first and then by column.
    pi_approx_s is the string representation of the pi approximation.
    The given rectangle is the location where to draw the text.
    The text is made of a number of digits plus a dot such as :
        d1.d2d3d4d5 ...
    """

    top_left, width, height = get_pi_rectangle(image_size)

    line_stroke_p = 5
    line_stroke = int(height * line_stroke_p / 100)
    margin_between_slots = line_stroke
    point_slot_width = line_stroke * 2
    slot_width = width // (len(pi_approx_s) - 1) - margin_between_slots
    slot_height = height

    # First two slots are always present. They correspond
    # to "3." in the pi_approx string
    slots = [
        (0, slot_width),
        (
            1 * slot_width + 1 * margin_between_slots,
            1 * slot_width + 1 * margin_between_slots + point_slot_width,
        ),
    ]

    # Then comes "pi_precision" digits after the dot
    precision_digits_slots = [
        (
            i * slot_width + (i + 1) * margin_between_slots + point_slot_width,
            (i + 1) * slot_width + (i + 1) * margin_between_slots + point_slot_width,
        )
        for i in range(1, len(pi_approx_s) - 1)
    ]
    slots.extend(precision_digits_slots)

    # Define the bars of the digital numbers :)
    h_top_bar = DigitBar(Pixel(0, 0, False), slot_width, line_stroke)
    h_middle_bar = DigitBar(
        Pixel(slot_height // 2 - line_stroke // 2, 0, False), slot_width, line_stroke
    )
    h_bottom_bar = DigitBar(
        Pixel(slot_height - line_stroke, 0, False), slot_width, line_stroke
    )
    v_top_left_bar = DigitBar(Pixel(0, 0, False), line_stroke, slot_height // 2)
    v_top_right_bar = DigitBar(
        Pixel(0, slot_width - line_stroke, False), line_stroke, slot_height // 2
    )
    v_bottom_left_bar = DigitBar(
        Pixel(slot_height // 2, 0, False), line_stroke, slot_height // 2
    )
    v_bottom_right_bar = DigitBar(
        Pixel(slot_height // 2, slot_width - line_stroke, False),
        line_stroke,
        slot_height // 2,
    )

    # Define the bars for all numbers between 0 and 9
    zero_bars = (
        h_top_bar,
        h_bottom_bar,
        v_top_left_bar,
        v_top_right_bar,
        v_bottom_left_bar,
        v_bottom_right_bar,
    )
    one_bars = (v_top_right_bar, v_bottom_right_bar)
    two_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_left_bar,
    )
    three_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
    )
    four_bars = (h_middle_bar, v_top_right_bar, v_bottom_right_bar, v_top_left_bar)
    five_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_left_bar,
        v_bottom_right_bar,
    )
    six_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_bottom_right_bar,
        v_top_left_bar,
        v_bottom_left_bar,
    )
    seven_bars = (v_top_right_bar, v_bottom_right_bar, h_top_bar)
    eight_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
        v_top_left_bar,
        v_bottom_left_bar,
    )
    nine_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
        v_top_left_bar,
    )

    # Map caracters to bars
    car_to_bars = {
        "0": zero_bars,
        "1": one_bars,
        "2": two_bars,
        "3": three_bars,
        "4": four_bars,
        "5": five_bars,
        "6": six_bars,
        "7": seven_bars,
        "8": eight_bars,
        "9": nine_bars,
    }

    # Yield pixels line by line
    slot = 0
    for line in range(height):
        for slot_idx, slot in enumerate(slots):
            for col in range(slot[0], slot[1]):
                current_car = pi_approx_s[slot_idx]
                if current_car in car_to_bars:
                    if is_in_bars(line, col - slot[0], car_to_bars[current_car]):
                        yield Pixel(line + top_left.line, col + top_left.col, False)
                elif current_car == ".":
                    if line > height - point_slot_width:
                        yield Pixel(line + top_left.line, col + top_left.col, False)
                else:
                    assert False, "Should not be here !"


def create_ppm_file(image_size, pi_approx_s, image_count):
    """Create and return the PPM file whit its header.

    Return also the max color value to be used when
    drawing in the file.
    The file MUST be closed by the caller.
    """

    # Create the PPM file
    ppm_file = open(f"img{image_count}_{pi_approx_s.replace('.', '-')}.ppm", "wb")

    # Magic number
    ppm_file.write("P6\n".encode("ascii"))
    # Image's size
    ppm_file.write(f"{image_size} {image_size}\n".encode("ascii"))
    # Image's max color value
    ppm_file.write("1\n".encode("ascii"))

    return ppm_file


def generate_ppm_file(image, image_size, pi_approx_s, image_count):
    """Generate the PPM image in the given file."""

    ppm_file = create_ppm_file(image_size, pi_approx_s, image_count)

    # Add the PI text in a copy of the image
    # so that next time we don't have this
    # PI value.
    image = bytearray(image)
    pi_pixels_it = get_pi_pixels_it(pi_approx_s, image_size)
    for pi_pixel in pi_pixels_it:
        pixel = (pi_pixel.line * image_size + pi_pixel.col) * 3
        image[pixel] = 255
        image[pixel + 1] = 255
        image[pixel + 2] = 255

    # Write the image into the file
    ppm_file.write(image)

    # Don't forget to close the file
    ppm_file.close()


def generate_ppm_files(image_size, nb_points, pi_precision):
    """Algorithm that have all the image in memory."""

    # Where are we in the simulation ?
    ten_percent = nb_points // 10
    image_count = 0

    # The image is a list of list
    # image = [[None] * image_size for _ in range(image_size)]
    image = bytearray([0] * (image_size * image_size * 3))

    # Main simulation loop
    half_image_size = image_size // 2
    for i, simulator_state in enumerate(approximate_pi.get_points(nb_points)):

        # Add the current point as a pixel in the image.
        # The mapping of points to pixel is done here since
        # the simulator must not deal with any "drawing" stuff,
        # hence it does not know the image size.
        point, in_circle, nb_in_circle = simulator_state
        pixel_line = int(point.y * half_image_size + half_image_size)
        pixel_col = int(point.x * half_image_size + half_image_size)
        pixel = (pixel_line * image_size + pixel_col) * 3
        if in_circle:
            image[pixel] = 0
            image[pixel + 1] = 0
            image[pixel + 2] = 1
        elif image[pixel] == 0:
            image[pixel] = 1
            image[pixel + 1] = 0
            image[pixel + 2] = 1

        # Every 10 percents of the simulation
        # generate an image
        if (i + 1) % ten_percent == 0:

            # Approximate the value of PI from the points
            pi_approx = 4 * nb_in_circle / (i + 1)
            pi_approx_s = f"{pi_approx:.{pi_precision}f}"
            print(pi_approx_s)

            # Draw the image
            generate_ppm_file(image, image_size, f"{pi_approx_s}", image_count)
            image_count += 1


def main():
    """Program's entry point"""

    # Program's inputs are given on the command line
    # and we must have 3 arguments
    if len(sys.argv) < 4:
        print("utilisation ./approximate_pi.py " "image_size nb_points pi_precision")
        return

    # Convert the 3 arguments to integers.
    # If any of the 3 conversion fails because
    # argument is not a valid integer, the `int`
    # function will throw a ValueError for us.
    # We don't catch it, so that it flows up to
    # the top of the execution stack as specified
    # in the project's requirements.
    image_size = int(sys.argv[1])
    nb_points = int(sys.argv[2])
    pi_precision = int(sys.argv[3])

    # We must also raise an exception if any of
    # the 3 argument is not strictly positive.
    if not all(param > 0 for param in (image_size, nb_points, pi_precision)):
        raise ValueError("all parameters must be " "integers strictly greater than 0")

    # Fix random in the simulator
    # Uncomment the following line for debug.
    approximate_pi.fix_points_from_random(42)

    # Generate the PPMs
    generate_ppm_files(image_size, nb_points, pi_precision)

    # Generate the GIF
    cmd = ["convert", "-delay", "100", "-loop", "0", "img*.ppm", "pi.gif"]
    process = subprocess.Popen(cmd)
    process.wait()


if __name__ == "__main__":
    main()
```

#### Solution 2 : utilisation d'un dictionnaire
La second solution stocke les pixels associés aux points tirés aléatoirement dans un dictionnaire.
La complexité temporelle est quadratique en fonction de la largeur de l'image et linéaire en fonction du nombre de points.
La complexité spatiale est constante en fonction de la largeur de l'image et linéaire en fonction du nombre de points.

```python
#!/usr/bin/env python3


"""Monte Carlo simulation to approximate π."""

# Imports from standard library
import collections
import subprocess
import sys

# Then, imports from our own modules
import approximate_pi

# Type for digit bars used to draw the "text"
# of the π approximation as in a 7 segments
# digital screen.
# A digit bar is a rectangle inside a slot,
# hence its coordinate are defined considering (0,0)
# is the top left of the slot.
# A slot is where a single number is drawn.
DigitBar = collections.namedtuple("DigitBar", ["top_left", "width", "height"])

# Type for representing a pixel
Pixel = collections.namedtuple("Pixel", ["line", "col", "in_circle"])


def is_in_bar(line, col, barr):
    """Return True if (line, col) is in barr else False."""
    if (
        barr.top_left.col <= col <= barr.top_left.col + barr.width
        and barr.top_left.line <= line <= barr.top_left.line + barr.height
    ):
        return True
    return False


def is_in_bars(line, col, bars):
    """Return True if (line, col) is in one of the bar in bars else False."""
    for barr in bars:
        if is_in_bar(line, col, barr):
            return True
    return False


def get_pi_rectangle(image_size):
    """ "Return the rectangle in the image where to draw PI text."""

    # The PI rectangle depends on image's size
    # The height is height_prop of the image size
    # The width is width_prop of the image size
    pi_rect_height_prop = 1 / 12
    pi_rect_width_prop = 1 / 6
    pi_rect_top_left = Pixel(
        int(image_size * (1 - pi_rect_height_prop) / 2),  # line
        int(image_size * (1 - pi_rect_width_prop) / 2),  # col
        False,
    )
    pi_rect_width = int(image_size * pi_rect_width_prop)
    pi_rect_height = int(image_size * pi_rect_height_prop)
    return pi_rect_top_left, pi_rect_width, pi_rect_height


def get_pi_pixels_it(pi_approx_s, image_size):
    """Return an iterator over the pixels to draw in black for PI text.

    The pixels are returned sorted by line first and then by column.
    pi_approx_s is the string representation of the pi approximation.
    The given rectangle is the location where to draw the text.
    The text is made of a number of digits plus a dot such as :
        d1.d2d3d4d5 ...
    """

    top_left, width, height = get_pi_rectangle(image_size)

    line_stroke_p = 5
    line_stroke = int(height * line_stroke_p / 100)
    margin_between_slots = line_stroke
    point_slot_width = line_stroke * 2
    slot_width = width // (len(pi_approx_s) - 1) - margin_between_slots
    slot_height = height

    # First two slots are always present. They correspond
    # to "3." in the pi_approx string
    slots = [
        (0, slot_width),
        (
            1 * slot_width + 1 * margin_between_slots,
            1 * slot_width + 1 * margin_between_slots + point_slot_width,
        ),
    ]

    # Then comes "pi_precision" digits after the dot
    precision_digits_slots = [
        (
            i * slot_width + (i + 1) * margin_between_slots + point_slot_width,
            (i + 1) * slot_width + (i + 1) * margin_between_slots + point_slot_width,
        )
        for i in range(1, len(pi_approx_s) - 1)
    ]
    slots.extend(precision_digits_slots)

    # Define the bars of the digital numbers :)
    h_top_bar = DigitBar(Pixel(0, 0, False), slot_width, line_stroke)
    h_middle_bar = DigitBar(
        Pixel(slot_height // 2 - line_stroke // 2, 0, False), slot_width, line_stroke
    )
    h_bottom_bar = DigitBar(
        Pixel(slot_height - line_stroke, 0, False), slot_width, line_stroke
    )
    v_top_left_bar = DigitBar(Pixel(0, 0, False), line_stroke, slot_height // 2)
    v_top_right_bar = DigitBar(
        Pixel(0, slot_width - line_stroke, False), line_stroke, slot_height // 2
    )
    v_bottom_left_bar = DigitBar(
        Pixel(slot_height // 2, 0, False), line_stroke, slot_height // 2
    )
    v_bottom_right_bar = DigitBar(
        Pixel(slot_height // 2, slot_width - line_stroke, False),
        line_stroke,
        slot_height // 2,
    )

    # Define the bars for all numbers between 0 and 9
    zero_bars = (
        h_top_bar,
        h_bottom_bar,
        v_top_left_bar,
        v_top_right_bar,
        v_bottom_left_bar,
        v_bottom_right_bar,
    )
    one_bars = (v_top_right_bar, v_bottom_right_bar)
    two_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_left_bar,
    )
    three_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
    )
    four_bars = (h_middle_bar, v_top_right_bar, v_bottom_right_bar, v_top_left_bar)
    five_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_left_bar,
        v_bottom_right_bar,
    )
    six_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_bottom_right_bar,
        v_top_left_bar,
        v_bottom_left_bar,
    )
    seven_bars = (v_top_right_bar, v_bottom_right_bar, h_top_bar)
    eight_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
        v_top_left_bar,
        v_bottom_left_bar,
    )
    nine_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
        v_top_left_bar,
    )

    # Map caracters to bars
    car_to_bars = {
        "0": zero_bars,
        "1": one_bars,
        "2": two_bars,
        "3": three_bars,
        "4": four_bars,
        "5": five_bars,
        "6": six_bars,
        "7": seven_bars,
        "8": eight_bars,
        "9": nine_bars,
    }

    # Yield pixels line by line
    slot = 0
    for line in range(height):
        for slot_idx, slot in enumerate(slots):
            for col in range(slot[0], slot[1]):
                current_car = pi_approx_s[slot_idx]
                if current_car in car_to_bars:
                    if is_in_bars(line, col - slot[0], car_to_bars[current_car]):
                        yield Pixel(line + top_left.line, col + top_left.col, False)
                elif current_car == ".":
                    if line > height - point_slot_width:
                        yield Pixel(line + top_left.line, col + top_left.col, False)
                else:
                    assert False, "Should not be here !"


def create_ppm_file(image_size, pi_approx_s, image_count):
    """Create and return the PPM file whit its header.

    The file MUST be closed by the caller.
    """

    # Create the PPM file
    ppm_file = open(f"img{image_count}_{pi_approx_s.replace('.', '-')}.ppm", "wb")

    # Header
    ppm_file.write("P6\n".encode("ascii"))
    ppm_file.write(f"{image_size} {image_size}\n".encode("ascii"))
    ppm_file.write("1\n".encode("ascii"))

    return ppm_file


def generate_ppm_file(pixels, image_size, pi_approx_s, image_count):
    """Generate the PPM image in the given file."""

    ppm_file = create_ppm_file(image_size, pi_approx_s, image_count)

    # Get the first pixel corresponding to the PI text
    pi_pixels_it = get_pi_pixels_it(pi_approx_s, image_size)
    pi_pixel = next(pi_pixels_it, None)

    # Draw pixels line by line
    for line in range(image_size):
        for col in range(image_size):

            # The current pixel correspond to a point that is in
            # the point list and in the unit circle
            pixel = (line, col)
            in_circle = pixels.get(pixel, None)
            if in_circle is not None:
                if in_circle:
                    pixelc_red = 0
                    pixelc_green = 0
                    pixelc_blue = 1

                # The current pixel correspond to a point that is in
                # the point list and not in the unit circle
                else:
                    pixelc_red = 1
                    pixelc_green = 0
                    pixelc_blue = 1

            # The point is not in the point list
            # draw it black
            else:
                pixelc_red = 0
                pixelc_green = 0
                pixelc_blue = 0

            # The current pixel is in the PI points,
            # override it with white.
            if pi_pixel and pi_pixel.line == line and pi_pixel.col == col:
                pixelc_red = 255
                pixelc_green = 255
                pixelc_blue = 255
                pi_pixel = next(pi_pixels_it, None)

            # write the pixel value in the PPM file
            ppm_file.write(bytes((pixelc_red, pixelc_green, pixelc_blue)))

    # Don't forget to close the file
    ppm_file.close()


def generate_ppm_files(image_size, nb_points, pi_precision):
    """Algorithm that saves chosen pixels in sets."""

    # Where are we in the simulation ?
    ten_percent = nb_points // 10
    image_count = 0

    # Set containing all the pixels of the image that have been
    # randomly chosen by the simulator module up to now and
    # that are in the circle
    pixels = {}

    # Main simulation loop
    half_image_size = image_size // 2
    for i, simulator_state in enumerate(approximate_pi.get_points(nb_points)):

        # Add the current point to the sets.
        # The mapping of points to pixel is done here since
        # the simulator must not deal with any "drawing" stuff,
        # hence it does not know the image size.
        point, in_circle, nb_in_circle = simulator_state
        pixel_line = int(point.y * half_image_size + half_image_size)
        pixel_col = int(point.x * half_image_size + half_image_size)
        pixel_pos = (pixel_line, pixel_col)
        pixels[(pixel_pos)] = in_circle
        # if in_circle:
        #     pixels_in_circle_set.add(pixel_pos)
        # elif not in_circle:
        #     pixels_not_in_circle_set.add(pixel_pos)

        # Every 10 percents of the simulation
        # generate an image
        if (i + 1) % ten_percent == 0:

            # Approximate the value of PI from the points
            pi_approx = 4 * nb_in_circle / (i + 1)
            pi_approx_s = f"{pi_approx:.{pi_precision}f}"
            print(pi_approx_s)

            # Draw the image
            generate_ppm_file(pixels, image_size, f"{pi_approx_s}", image_count)
            image_count += 1


def main():
    """Program's entry point"""

    # Program's inputs are given on the command line
    # and we must have 3 arguments
    if len(sys.argv) < 4:
        print("utilisation ./approximate_pi.py " "image_size nb_points pi_precision")
        return

    # Convert the 3 arguments to integers.
    # If any of the 3 conversion fails because
    # argument is not a valid integer, the `int`
    # function will throw a ValueError for us.
    # We don't catch it, so that it flows up to
    # the top of the execution stack as specified
    # in the project's requirements.
    image_size = int(sys.argv[1])
    nb_points = int(sys.argv[2])
    pi_precision = int(sys.argv[3])

    # We must also raise an exception if any of
    # the 3 argument is not strictly positive.
    if not all(param > 0 for param in (image_size, nb_points, pi_precision)):
        raise ValueError("all parameters must be " "integers strictly greater than 0")

    # Fix random in the simulator
    # Uncomment the following line for debug.
    approximate_pi.fix_points_from_random(42)

    # Generate the PPMs
    generate_ppm_files(image_size, nb_points, pi_precision)

    # Generate the GIF
    cmd = ["convert", "-delay", "100", "-loop", "0", "img*.ppm", "pi.gif"]
    process = subprocess.Popen(cmd)
    process.wait()


if __name__ == "__main__":
    main()
```

#### Solution 3 : utilisation de la méthode `seek`

La seconde solution ne stocke rien du tout car les pixels sont directement écrit au bon endroit dans le fichier `PPM` à l'aide de la méthode `seek` (dont le coût est constant).
La complexité temporelle est constante (en théorie mais la pratique semble dire le contraire, peut-être que `truncate` est linéaire) en fonction de la largeur de l'image et linéaire en fonction du nombre de points.
La complexité spatiale est constante en fonction de la largeur de l'image et constante en fonction du nombre de points.

```python
#!/usr/bin/env python3


"""Monte Carlo simulation to approximate π."""

# Imports from standard library
import collections
import shutil
import subprocess
import sys

# Then, imports from our own modules
import approximate_pi

# Type for digit bars used to draw the "text"
# of the π approximation as in a 7 segments
# digital screen.
# A digit bar is a rectangle inside a slot,
# hence its coordinate are defined considering (0,0)
# is the top left of the slot.
# A slot is where a single number is drawn.
DigitBar = collections.namedtuple("DigitBar", ["top_left", "width", "height"])

# Type for representing a pixel by its position in
# the binary file
Pixel = collections.namedtuple("Pixel", ["pos", "color"])
# Type for representing a pixel by its line and col
PixelLineCol = collections.namedtuple("PixelLineCol", ["line", "col"])


def is_in_bar(line, col, barr):
    """Return True if (line, col) is in barr else False."""
    if (
        barr.top_left.col <= col <= barr.top_left.col + barr.width
        and barr.top_left.line <= line <= barr.top_left.line + barr.height
    ):
        return True
    return False


def is_in_bars(line, col, bars):
    """Return True if (line, col) is in one of the bar in bars else False."""
    for barr in bars:
        if is_in_bar(line, col, barr):
            return True
    return False


def get_pi_rectangle(image_size):
    """ "Return the rectangle in the image where to draw PI text."""

    # The PI rectangle depends on image's size
    # The height is height_prop of the image size
    # The width is width_prop of the image size
    pi_rect_height_prop = 1 / 12
    pi_rect_width_prop = 1 / 6
    pi_rect_top_left = PixelLineCol(
        int(image_size * (1 - pi_rect_height_prop) / 2),  # line
        int(image_size * (1 - pi_rect_width_prop) / 2),
    )  # col
    pi_rect_width = int(image_size * pi_rect_width_prop)
    pi_rect_height = int(image_size * pi_rect_height_prop)
    return pi_rect_top_left, pi_rect_width, pi_rect_height


def get_pi_pixels_it(pi_approx_s, image_size):
    """Return an iterator over the pixels to draw in black for PI text.

    The pixels are returned sorted by line first and then by column.
    pi_approx_s is the string representation of the pi approximation.
    The given rectangle is the location where to draw the text.
    The text is made of a number of digits plus a dot such as :
        d1.d2d3d4d5 ...
    """

    top_left, width, height = get_pi_rectangle(image_size)

    line_stroke_p = 5
    line_stroke = int(height * line_stroke_p / 100)
    margin_between_slots = line_stroke
    point_slot_width = line_stroke * 2
    slot_width = width // (len(pi_approx_s) - 1) - margin_between_slots
    slot_height = height

    # First two slots are always present. They correspond
    # to "3." in the pi_approx string
    slots = [
        (0, slot_width),
        (
            1 * slot_width + 1 * margin_between_slots,
            1 * slot_width + 1 * margin_between_slots + point_slot_width,
        ),
    ]

    # Then comes "pi_precision" digits after the dot
    precision_digits_slots = [
        (
            i * slot_width + (i + 1) * margin_between_slots + point_slot_width,
            (i + 1) * slot_width + (i + 1) * margin_between_slots + point_slot_width,
        )
        for i in range(1, len(pi_approx_s) - 1)
    ]
    slots.extend(precision_digits_slots)

    # Define the bars of the digital numbers :)
    h_top_bar = DigitBar(PixelLineCol(0, 0), slot_width, line_stroke)
    h_middle_bar = DigitBar(
        PixelLineCol(slot_height // 2 - line_stroke // 2, 0), slot_width, line_stroke
    )
    h_bottom_bar = DigitBar(
        PixelLineCol(slot_height - line_stroke, 0), slot_width, line_stroke
    )
    v_top_left_bar = DigitBar(PixelLineCol(0, 0), line_stroke, slot_height // 2)
    v_top_right_bar = DigitBar(
        PixelLineCol(0, slot_width - line_stroke), line_stroke, slot_height // 2
    )
    v_bottom_left_bar = DigitBar(
        PixelLineCol(slot_height // 2, 0), line_stroke, slot_height // 2
    )
    v_bottom_right_bar = DigitBar(
        PixelLineCol(slot_height // 2, slot_width - line_stroke),
        line_stroke,
        slot_height // 2,
    )

    # Define the bars for all numbers between 0 and 9
    zero_bars = (
        h_top_bar,
        h_bottom_bar,
        v_top_left_bar,
        v_top_right_bar,
        v_bottom_left_bar,
        v_bottom_right_bar,
    )
    one_bars = (v_top_right_bar, v_bottom_right_bar)
    two_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_left_bar,
    )
    three_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
    )
    four_bars = (h_middle_bar, v_top_right_bar, v_bottom_right_bar, v_top_left_bar)
    five_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_left_bar,
        v_bottom_right_bar,
    )
    six_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_bottom_right_bar,
        v_top_left_bar,
        v_bottom_left_bar,
    )
    seven_bars = (v_top_right_bar, v_bottom_right_bar, h_top_bar)
    eight_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
        v_top_left_bar,
        v_bottom_left_bar,
    )
    nine_bars = (
        h_top_bar,
        h_bottom_bar,
        h_middle_bar,
        v_top_right_bar,
        v_bottom_right_bar,
        v_top_left_bar,
    )

    # Map caracters to bars
    car_to_bars = {
        "0": zero_bars,
        "1": one_bars,
        "2": two_bars,
        "3": three_bars,
        "4": four_bars,
        "5": five_bars,
        "6": six_bars,
        "7": seven_bars,
        "8": eight_bars,
        "9": nine_bars,
    }

    # Yield pixels line by line
    slot = 0
    for line in range(height):
        for slot_idx, slot in enumerate(slots):
            for col in range(slot[0], slot[1]):
                current_car = pi_approx_s[slot_idx]
                pixel_pos = (
                    (line + top_left.line) * image_size + col + top_left.col
                ) * 3 + 13
                if current_car in car_to_bars:
                    if is_in_bars(line, col - slot[0], car_to_bars[current_car]):
                        yield Pixel(pixel_pos, bytes((255, 255, 255)))
                elif current_car == ".":
                    if line > height - point_slot_width:
                        yield Pixel(pixel_pos, bytes((255, 255, 255)))
                else:
                    assert False, "Should not be here !"


def create_ppm_file(image_size):
    """Create and return the PPM file whit its header.

    Return also the name of the file.
    The file MUST be closed by the caller.
    """

    ppm_file = open("temp.ppm", "wb")
    # Magic number
    ppm_file.write("P6\n".encode("ascii"))
    # Image's size
    ppm_file.write(f"{image_size} {image_size}\n".encode("ascii"))
    # Image's max color value
    ppm_file.write("1\n".encode("ascii"))
    # Truncate the file to have zeros, hence black until
    # the end. 13 is the size of the header
    last_pos = (image_size * image_size) * 3 + 13
    ppm_file.seek(last_pos)
    ppm_file.truncate()

    return ppm_file


def generate_ppm_files(image_size, nb_points, pi_precision):
    """Algorithm that have all the image in memory."""

    # Where are we in the simulation ?
    ten_percent = nb_points // 10
    image_count = 0

    # Create the first image file
    ppm_file_points = create_ppm_file(image_size)

    # Main simulation loop
    half_image_size = image_size // 2

    for i, simulator_state in enumerate(approximate_pi.get_points(nb_points)):

        # Draw the current point in the image.
        # The mapping of points to pixel is done here since
        # the simulator must not deal with any "drawing" stuff,
        # hence it does not know the image size.
        point, in_circle, nb_in_circle = simulator_state
        pixel_line = int(point.y * half_image_size + half_image_size)
        pixel_col = int(point.x * half_image_size + half_image_size)
        pixel_pos = (pixel_line * image_size + pixel_col) * 3 + 13
        if in_circle:
            color = (0, 0, 1)
        else:
            color = (1, 0, 1)
        ppm_file_points.seek(pixel_pos)
        ppm_file_points.write(bytes(color))

        # Every 10 percents of the simulation
        # generate an image
        if (i + 1) % ten_percent == 0:

            # Approximate the value of PI from the points
            pi_approx = 4 * nb_in_circle / (i + 1)
            pi_approx_s = f"{pi_approx:.{pi_precision}f}"
            print(pi_approx_s)

            # Copy the file with points in a file wich name
            # contains the pi approx
            ppm_file_name = f"img{image_count}_{pi_approx_s.replace('.', '-')}.ppm"
            image_count += 1
            shutil.copyfile("temp.ppm", ppm_file_name)
            ppm_file = open(ppm_file_name, "rb+")

            # Write the pi pixels in white
            pi_pixels_it = get_pi_pixels_it(pi_approx_s, image_size)
            for pi_pixel in pi_pixels_it:
                ppm_file.seek(pi_pixel.pos)
                ppm_file.write(pi_pixel.color)

            # Don't forget to close the file
            ppm_file.close()


def main():
    """Program's entry point"""

    # Program's inputs are given on the command line
    # and we must have 3 arguments
    if len(sys.argv) < 4:
        print("utilisation ./approximate_pi.py " "image_size nb_points pi_precision")
        return

    # Convert the 3 arguments to integers.
    # If any of the 3 conversion fails because
    # argument is not a valid integer, the `int`
    # function will throw a ValueError for us.
    # We don't catch it, so that it flows up to
    # the top of the execution stack as specified
    # in the project's requirements.
    image_size = int(sys.argv[1])
    nb_points = int(sys.argv[2])
    pi_precision = int(sys.argv[3])

    # We must also raise an exception if any of
    # the 3 argument is not strictly positive.
    if not all(param > 0 for param in (image_size, nb_points, pi_precision)):
        raise ValueError("all parameters must be " "integers strictly greater than 0")

    # Fix random in the simulator
    # Uncomment the following line for debug.
    approximate_pi.fix_points_from_random(42)

    # Generate the PPMs
    generate_ppm_files(image_size, nb_points, pi_precision)

    # Generate the GIF
    cmd = ["convert", "-delay", "100", "-loop", "0", "img*.ppm", "pi.gif"]
    process = subprocess.Popen(cmd)
    process.wait()


if __name__ == "__main__":
    main()
```
</details>
