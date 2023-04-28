import random


fichier=open("pgm2.pgm","w+")
print("P2",file=fichier,sep="\n")
largeur=int(input("saisez la largeur d'image svp:" ))
hauteur=int(input("saisez la hauteur d'image svp:" ))
print(str(largeur),"  ", str(hauteur),file=fichier,sep="\n")
print("255\n",file=fichier,sep="\n")
x1=random.randint(0,largeur)
y1=random.randint(0,hauteur)
r1=random.randint(0,min(largeur-x1,hauteur-y1,x1,y1))

x2=random.randint(0,largeur)
y2=random.randint(0,hauteur)
r2=random.randint(0,min(largeur-x2,hauteur-y2,x2,y2))

for i in range(largeur):
    for j in range(hauteur):
        if (x1-i)**2+(y1-j)**2<=r1**2 or (x2-i)**2+(y2-j)**2<=r2**2:
            
            couleur=random.randint(0,254)
            print(str(couleur),file=fichier, end=" ")
        else:
            print(str(255),file=fichier, end=" ")


