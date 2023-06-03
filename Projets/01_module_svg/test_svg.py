#!/usr/bin/env python3
# START CORRECTION
"""Un programme pour tester notre module svg"""

# On importe le module sys pour accéder à la sortie standard
import sys

# On importe tout le contenu du module svg
import svg

def teste_module_svg():
    """Fonction de test du module svg."""
    # Création de trois points
    c1 = svg.Point(10, 10)
    c2 = svg.Point(100, 100)
    c3 = svg.Point(180, 50)

    # On utilise un booléen pour choisir entre print
    # sur la sortie standard ou dans un fichier.
    # Il suffit donc de changer cette variable pour
    # contrôler la sortie du programme de test.
    SORTIE_STANDARD = True

    # On choisit où est-ce que l'on va faire nos prints
    if SORTIE_STANDARD:
        out = sys.stdout
    else:
        out = open("mon_image.svg", "w")

    # Print d'une image SVG avec 3 cercles sur la sortie standard ou dans
    # un fichier.
    # Pour pouvoir visualiser l'image il faudra donc utiliser une redirection
    # si l'on utilise la sortie standard :
    #   ./test_svg.py > mes-cercles.svg
    # Une fois l'image SVG enregistrée dans un fichier texte, on peut la
    # visualiser à l'aide de n'importe quel programme supportant ce format
    # d'image :
    #   eog mon-triangle.svg
    #   firefox mon-triangle.svg
    #   double-clic sur le fichier dans un explorateur de fichiers
    print(svg.genere_balise_debut_image(200, 200), file=out)
    print(svg.genere_balise_debut_groupe("black", "red", 5), file=out)
    print(svg.genere_cercle(c1, 30), file=out)
    print(svg.genere_balise_fin_groupe(), file=out)
    print(svg.genere_balise_debut_groupe("red", "black", 5), file=out)
    print(svg.genere_cercle(c2, 60), file=out)
    print(svg.genere_cercle(c3, 10), file=out)
    print(svg.genere_balise_fin_groupe(), file=out)
    print(svg.genere_balise_fin_image(), file=out)

    # On ferme le fichier si il a été créé
    if not SORTIE_STANDARD:
        out.close()

teste_module_svg()
# END CORRECTION
