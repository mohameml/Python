#!/usr/bin/env python3

"""
ceci est un mini projet : quiz 

"""
import subprocess
import time

def lecture_question(fichier , numero):
    """
    ENTREE : nom de fichier , et le numéro de question 
    SORTIE : un tuple = Question ,reponse    
    
    """

    fich = open(fichier,"r")
    ligne = fich.readline()
    while ligne[:2]!=f"Q{numero}":
        ligne=fich.readline()

    question = [ligne]
    ligne = fich.readline()
    while ligne[:7]!="Réponse":
        question.append(ligne)
        ligne= fich.readline()

    reponse = ligne.split(":")[1]
    
    return "".join(question),reponse[1]


    fich.close()


def score(reponse, fichier , numero , score):
    "fonction "

    reponse_corr = lecture_question(fichier,numero)[1]

    if reponse==reponse_corr :

        print(f"Bravo votre réponse est correcte :  ", end ="")
        print("\033[92mBravo\033[0m")

        score+=1
        print(f"----------------votre score mnt est:\033[92m{score}\033[0m ----------------")
        return score

    else : 

        print(f"Désole votre réponse n'est pas correcte : ", end ="")
        print("\033[91mX\033[0m")
        
        score-=1 
        print(f"----------------votre score mnt est : \033[91m{score}\033[0m-------------------")
        return score 


    
         


def affichage(fichier , numero):

    question = lecture_question(fichier , numero)[0]

    print(question)








def main():
    "fonction principale "
    score_test = 0 

    print("Bonjour Commancer le test de mnt")
    print(f"votre score mnt est : {score_test}")





    # Questions 

    for i in range(1,10):

        affichage("quiz.txt" , i)
        print("Donnez votre reponse [a,b,c,d] :",end ="")
        reponse = input("")

        score_test  = score(reponse, "quiz.txt" , i , score_test)

    









    
    



if __name__=="__main__":
    main()


                
