#!/usr/bin/env python3
"partie1: avec des fonctions seulement"

def calcul_numero_date(j,mois):

    "sert a clacule le numero  de date "
    l=[31,28,31,30,31,30,31,31,30,31,30,31]
    numero_date=j
    for i in range(mois-1):
        numero_date+=l[i]

    return numero_date


def convertit(l):
    " cette fonction sert a convrtit une liste de coulpes en une liste"
    l1=[]
    for tuple in l:
        numero_date=calcul_numero_date(tuple[0],tuple[1])
        l1.append(numero_date)

    return l1

def ecare_maximale(l):
    ecare=0
    indice_fiéres=0
    for i in range(len(l)-1):
        if abs(l[i+1]-l[i]) > ecare:
            ecare= abs(l[i+1]-l[i])
            indice_fiéres=i
    
    return ecare,indice_fiéres

joures_fériés =[(1,1),(9,4),(1,5),(8,5),(17,5),(4,6),(14,7),(15,8),(1,11),(11,11),(25,12)]
numeros_fériés=convertit(joures_fériés)
t=ecare_maximale(numeros_fériés)
i=t[1]
print(f'le deux fériés le plus eloigenes son {joures_fériés[i]} et {joures_fériés[i+1]} ')

"etape2 une autre methode par la clasee au lieu les fonctions"

class Date:

    def __init__(self,jour,mois):
        self.jour=jour
        self.mois=mois
        self.anne=[31,28,31,30,31,30,31,31,30,31,30,31]

    def converssion(self):
        s=+self.jour
        for i in range(self.mois -1):
            s+=self.anne[i]

        return s
    def differance(self, autre):
        return self.converssion() - autre.converssion()


l =[Date(1,1),Date(9,4),Date(1,5),Date(8,5),Date(17,5),Date(4,6),Date(14,7),Date(15,8),Date(1,11),Date(11,11),Date(25,12)]
ecare=0
indice=0
for i in range(len(l)-1):
    if abs(l[i].differance(l[i+1])) > ecare :
        ecare= abs(l[i].differance(l[i+1]))
        indice =i

print(f"les deux fériés le plus eloigenes son {(l[indice].jour,l[indice].mois)} et {(l[indice+1].jour,l[indice+1].mois)} ")
