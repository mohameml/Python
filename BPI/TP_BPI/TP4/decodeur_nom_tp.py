import codageRotx
fichier =input("donner le nom du ficiher:")
file1=open (fichier,"w+")
nom_tp="nirPrfne"

for lettre in nom_tp:
    print(codageRotx.rot13(lettre),file=file1)

file1.close()

prenom="mohamedlemine"

for lettre in prenom:
    print(codageRotx.rot(4,lettre))


