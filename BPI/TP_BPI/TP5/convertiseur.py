#!/usr/bin/env python3
"""Convertisseur de fichier texte de 1000 points vers SVG"""
import svg


def convertit():
    """Version avec 2 appels à input"""
    print(svg.genere_balise_debut_image(640, 480))
    print(svg.genere_balise_debut_groupe("black", "white", 2))
    for _ in range(1000):
        abscisse = int(input())
        ordonnee = int(input())
        point = svg.Point(abscisse, ordonnee)
        chaine_svg = svg.genere_cercle(point, 1)
        print(chaine_svg)
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())


convertit()