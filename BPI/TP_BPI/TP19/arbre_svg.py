#!/usr/bin/env python3

import svg
from svg import Point
import sys
import math
import random

"""Génération récursive d'arbre en svg"""

BACKGROUND_COLOR = "black"
TREE_COLOR = "#59330d"
TREE_SECOND_COLOR = "#006600"
WIDTH = 1000
HEIGHT = 800
# WIDTH = 1584
# HEIGHT = 396
TREE_DEPTH = 8


def tree_rec(file, iteration, start, angle, trunk_size, color,  total_iteration, color_2):
    if iteration == 0:
        return

    # generate trunk :
    end = Point(start.x + trunk_size * math.cos(math.radians(angle)),
                start.y - trunk_size * math.sin(math.radians(angle)))

    current_color = color
    if color_2 != "#":
        current_color = svg.get_color_between(
            color, color_2, (total_iteration-iteration)/total_iteration)

    # Stroke width : 3
    file.write(svg.generate_line(start, end, current_color, 3))

    # branches :
    # Generate between 2 and 3 branches for each iteration
    for i in range(random.randint(2, 3)):
        # Compute start of new branch, in the upper 45% of the trunk
        start_ratio = 1 - (random.randint(0, 45) / 100)
        new_x = start.x + start_ratio*(end.x-start.x)
        new_y = start.y + start_ratio*(end.y-start.y)
        new_start = Point(new_x, new_y)

        # Compute new trunk size
        reduction_ratio = random.randint(
            65, 75) / 100  # Keeping a size between 65% and 75% of the trunk
        new_trunk_size = trunk_size * reduction_ratio

        # Compute new angle
        # Can rotate between -45° and 45°
        new_angle = angle + random.randint(-45, 45)

        # branch:
        tree_rec(file, iteration-1, new_start,
                 new_angle, new_trunk_size, color,  total_iteration, color_2)


def generate_tree(filename, background_color, tree_color, width, height, depth, second_color="#"):

    with open(filename+".svg", "w") as picture:
        picture.write(svg.genere_balise_debut_image(width, height))
        picture.write(svg.generate_rectangle(
            0, 0, width, height, background_color))

        # tree:
        tree_rec(picture, depth, Point(
            width//2, height * 0.9), 90, height*0.3, tree_color, depth, second_color)
        tree_rec(picture, depth, Point(
            width*(1/7), height * 0.9), 90, height*0.1, tree_color, depth, second_color)
        tree_rec(picture, depth, Point(
            width*(2/7), height * 0.9), 90, height*0.15, tree_color, depth, second_color)
        tree_rec(picture, depth, Point(
            width*(3/7), height * 0.9), 90, height*0.2, tree_color, depth, second_color)
        tree_rec(picture, depth, Point(
            width*(4/7), height * 0.9), 90, height*0.25, tree_color, depth, second_color)
        tree_rec(picture, depth, Point(
            width*(5/7), height * 0.9), 90, height*0.3, tree_color, depth, second_color)
        tree_rec(picture, depth, Point(
            width*(6/7), height * 0.9), 90, height*0.35, tree_color, depth, second_color)

        picture.write(svg.genere_balise_fin_image())


def generate_trees(filename, N, background_color, tree_color, width, height, depth, second_color="#"):
    for i in range(N):
        generate_tree(sys.argv[1]+"_"+str(i), background_color,
                      tree_color, width, height, depth, second_color)


def main():
    """Teste la fonction ci-dessus."""

    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], " nom_fichier")
        sys.exit(1)

    generate_trees(sys.argv[1], 1, BACKGROUND_COLOR,
                   TREE_COLOR, WIDTH, HEIGHT, TREE_DEPTH, TREE_SECOND_COLOR)


if __name__ == "__main__":
    main()
