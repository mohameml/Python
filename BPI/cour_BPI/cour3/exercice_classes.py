class Voiture:

    def __init__(self, p_couleur, p_marque, p_vitesse = 0):
        self.couleur = p_couleur
        self.marque = p_marque
        self.vitesse = p_vitesse

    def accelerer(self, p_vitesse):
        self.vitesse += p_vitesse

    def freiner(self, p_vitesse):
        self.vitesse -= p_vitesse
        if self.vitesse < 0:
            self.vitesse = 0

voiture_bleu = Voiture('bleu', 'Peugeot', 20)
voiture_rouge = Voiture('rouge', 'BMW')

print(voiture_bleu.couleur)
print(voiture_bleu.marque)
print(voiture_bleu.vitesse)
print('-'*8)
print(voiture_rouge.couleur)
print(voiture_rouge.marque)
print(voiture_rouge.vitesse)

print('-'*8)
print(voiture_bleu.vitesse)
voiture_bleu.accelerer(20)
print(voiture_bleu.vitesse)
voiture_bleu.freiner(10)
print(voiture_bleu.vitesse)
voiture_bleu.freiner(50)
print(voiture_bleu.vitesse)
