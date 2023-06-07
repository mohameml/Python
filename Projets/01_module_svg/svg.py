"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

from collections import namedtuple

# Definition de la structure Point composée de deux attributs x et y
Point = namedtuple("Point", "x y")



def genere_balise_debut_image(largeur, hauteur):
  
  """
  Retourne la chaîne de caractères correspondant à la balise ouvrante pour
  décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
  sont des entiers.

  Remarque : l'origine est en haut à gauche et l'axe des Y est orienté vers le
  bas.
    
  """
  
  return f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{largeur}" height="{hauteur}">'


def genere_balise_fin_image():
  """
  Retourne la chaîne de caractères correspondant à la balise svg fermante.
  Cette balise doit être placée après tous les éléments de description de
  l'image, juste avant la fin du fichier.
  """
  return "</svg>"



def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage,epaisseur_ligne):
  """
    Retourne la chaîne de caractères correspondant à une balise ouvrante
    définissant un groupe d'éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l'image.

    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).

    Le paramètre d'épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    
  """
  return f'<g fill="{couleur_remplissage}" stroke="{couleur_ligne}" stroke-width="{epaisseur_ligne}">'


def genere_balise_fin_groupe():
  """
    Retourne la chaîne de caractères correspondant à la balise fermante pour un
    groupe d'éléments.
    """
  
  return "</g>"


# À implémenter dans 'TP2. Module SVG'
def genere_cercle(centre, rayon):
  """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).

    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
  
  """
  
  return f'<circle cx="{centre.x}" cy="{centre.y}" r="{rayon}" />'



def genere_segment(dep, arr):
  """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un segment. Ce segment relie les points dep et arr.
  """
  
  return f'<line x1="{dep.x}" y1 = "{dep.y}" x2="{arr.x}" y2 ="{arr.y}" />'



def genere_rectangle(top_left, width, height):
  """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant un rectangle.
  
  """
  return f'<rect x="{top_left.x}" y="{top_left.y}" width="{width}" height="{height}" />'



def genere_polygone(points):
  """
    Retourne la chaîne de caractères correspondant à un élément SVG
    représentant un polygone. `points` est un tableaux de points.
  
  """
  
  chaine ="".join([f'{point.x},{point.y} ' for point in  points])
  
  return f'<polygon points="{chaine}" />'
  
  



def genere_balise_debut_groupe_transp(niveau_opacite):
  """
    Retourne la chaîne de caractères correspondant à une balise ouvrant un
    groupe d'éléments qui, dans son ensemble, sera partiellement transparent.
    Les éléments qui composent le groupe se masquent les uns les autres dans
    l'ordre d'apparition (ils ne sont pas transparents entre eux).
    `niveau_opacite` doit être un nombre entre 0 et 1. Ce groupe doit être
    refermé de la même manière que les groupes définissant un style.
    
  """
  
  return f'<g fill-opacity="{niveau_opacite}">'




def genere_zone_colorie(x_min, y_min, largeur, hauteur, couleur_remplissage):
  """
    Retourne la chaîne de caractères correspondant à un élément qui colorie une
    zone rectangulaire de la couleur indiquée
    
  """
  
  return f'<rect x="{x_min}" y="{y_min}" width="{largeur}" height="{hauteur}" fill="{couleur_remplissage}" />'
  


def genere_texte(x_min, y_bas, contenu, hauteur):
  """
    Retourne la chaîne de caractères correspondant à un élément SVG représentant
    un texte. Place le texte à la position indiquée. x_min est l'abscisse du
    début du texte. y_bas est l'ordonnée de la ligne de base du texte (le bas
    d'une lettre telle que “n”). Attention, ce n'est pas l'ordonnée maximale
    puisque certaines lettres descendent sous cette ligne (g, j, p, q, y). Le
    paramètre hauteur définit la taille de police (c'est-à-dire la hauteur d'une
    ligne de texte)
    
  """
  
  #  <text x="0" y="15" fill="red">I love SVG!</text>
  return f'<text x="{x_min}" y="{y_bas}"  height="{hauteur}"  > {contenu} </text>'


