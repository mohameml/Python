class Etudiant:

    def __init__(self, p_nom, p_prenom):
        self.nom = p_nom
        self.prenom = p_prenom
        self.notes = []

    def moyenne(self):
        return sum(self.notes) / len(self.notes)

    def imprimer_moyenne(self):
        if len(self.notes) == 0:
            print(f"L'étudiant {self.nom} n'as pas encore fait d'examens")
        else:
            print(f"La moyenne de l'étudiant est {self.moyenne()}")

etudiant_paul = Etudiant('Paul', 'Legrand')
etudiant_paul.imprimer_moyenne()
etudiant_paul.notes.append(18)
etudiant_paul.notes.append(20)
etudiant_paul.imprimer_moyenne()
etudiant_paul.notes.append(1)
etudiant_paul.imprimer_moyenne()
        