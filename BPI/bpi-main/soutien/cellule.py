"""
  La classe Cellule
"""

class Cellule:
    """
      Une cellule est composee d'une valeur et d'un pointeur vers la
        cellule suivante (ou None s'il n'y a pas de suivant)
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, val, suiv):
        """
          Constructeur
        """
        self.val = val
        self.suiv = suiv

    def __str__(self):
        """
          Afficheur
        """
        return f"{self.val} -> "
