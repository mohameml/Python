"""
  Une cellule doublement chainee
"""

class Cellule:
    """
      Une cellule est constituee :
      - d'une valeur
      - d'un pointeur vers la cellule precedente
      - d'un pointeur vers la cellule suivante
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, val, prec, suiv):
        """
          Constructeur
        """
        self.val = val
        self.prec = prec
        self.suiv = suiv

    def __str__(self):
        """ Afficheur """
        return f"{self.val} <-> "
