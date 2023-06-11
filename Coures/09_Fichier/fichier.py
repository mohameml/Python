#!/usr/bin/env python3

"cour 7 :  traitement de fichier en python"

print("---------- 1. Lectrue dans un fichier ---------------")
print()
print("---------- 1.1 la méthode : .readlines -------------------")
print()

# On ouvrir le fichier avec le mode "r"
fichier =  open("zoo.txt","r")



# La méthode readlines() return une liste contient les lignes de fichier
lignes = fichier.readlines()


#On remarque que à la fin de chaque ligne on '\n' qui indique le retiue à la ligne
print(lignes)



for line in lignes:
    print(line)

fichier.close()


print()
print()

print("---------- 1.2 la méthode : .read -------------------")
print()

# La méthode read lit tout le contenu d'un fichier et renvoie une chaine des caractéres unique


fichier = open("zoo.txt","r")

chaine = fichier.read()

print(chaine)


fichier.close()


print()
print()


print("---------- 1.3 la méthode : .readline -------------------")
print()

# la méthode readline : lit une ligne d'un fichier et la
# renvoie sous formed'une chaine de chai e des carcatéres
# a chaque apple de readline() , la ligne suivant erst renvoyée


# Exemple 1 :


def lecture_ligne(fich_test):
    "cette fait la lectrure d'une ligne "
    chaine_test = fich_test.readline()
    
    return chaine_test.replace("\n","")


def lecture_totale(fichier_test):
    
    "cette fonction fait la lecture totale de la fichier "
    file_test = open(fichier_test,"r")
    
    ligne_test = lecture_ligne(file_test)
    
    while ligne_test!="":
        
        # la fin de fichier est indique  par : '' ligne vide
        
        print(ligne_test)
        ligne_test = lecture_ligne(file_test)
        
    file_test.close()
    
lecture_totale("zoo.txt")
    
print()
print()
    
    


print("---------- 1.4 l'instruction : with  -------------------")
print()

# l'instruction with permet d'ouvrir et feremer un fichier d'une maniére efficace
# l'instruction with garantit la fermeture du fichier 

with open("zoo.txt","r") as fichier :
    
    # l'instruction with donne un iterable "fichier" 
    
    for ligne in fichier :
        if ligne == "\n":
            pass
        
        else:
            print(ligne.replace("\n",""))
        

# une fois sorti du bloc d'indentation , Python fermera automatiquement le fichier 


print("---------- 2. écriture dans un fichier ---------------")
print()

print("---------- 2.1. la méthode : write()--------------------")

# Pour ouvrir en fichier en mode écriture On utilise le mode "w"
#   Attention :mode "w" écrasse ce qui dans le fichier 

phrase = ["sidi ", "va " , "à " , "l'école "]

with open("exemple.txt","w") as file :
    
    for  mot in phrase :
        file.write(mot)
        
    file.write("\n")
    
    
# Remarque la méthode .write(): return le nombre d'octets écrits dans le fichier 

fichier = open("exemple2.txt","w")

nb = fichier.write("chat")
print(f'le nombre d \' octets écritent dans le fichier  est : {nb}')

fichier.close()
print()


print("---------- 2.2. écriture avec print --------------------")
print()
# On peut écrire dans fichier avec print en utilisant "file"

with open("exemple3.txt","w") as fich :
    
    # mais attention avce print il y'a un retour a la ligne par défaut: 
    print("Bonjour !!!! ", file=fich )
    

# Reamrque avce la méthode with on peut ovrir plusieres fichier a mémé temps 

with open("zoo.txt","r") as file1 , open("exemple4.txt","w") as file2 :
    
    for ligne in file1 :
        
        if ligne!="\n" :
            print("*",ligne,file=file2 , end="")
            
    file2.write("\n")
            

