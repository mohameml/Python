#!/usr/bin/env python3
import sys

def print_line(line):
    "affichine une ligne des carres blanches et noirs selon le carectere "
    for carectere in line:
        for _ in range(5):
            if carectere==".":
                print("\u2588",end="")
            else:
                print(" ",end="")
    print("|") 

def print_state(state):
    "une fonction qui genere un grande tableau oui il ya des carres blanches et carres noires "
    print("\033c")
    print("     1    2    3    4    5   ")
    print("  +-------------------------+")
    line_index=0

    for line in state:
        print("  |",end="")
        print_line(line)

        print(chr(line_index +65),end="")
        print(" |",end="")
        print_line(line)

        print("  |",end="")
        print_line(line)
        line_index+=1
    print("  +-------------------------+")

def finsihed_jeu(state):

    for ligne in state:
        for caractere in ligne:
            if caractere!="_":
                return False
    return True 
def touch(ligne_index_1,car_index_1,ligne_index_2,car_index_2):
    if ligne_index_1==ligne_index_2 and car_index_1==car_index_2:
        return True
    if ligne_index_1==ligne_index_2 - 1 and car_index_1==car_index_2:
        return True
    if ligne_index_1==ligne_index_2 + 1 and car_index_1==car_index_2:
        return True
    if ligne_index_1==ligne_index_2 and car_index_1==car_index_2 - 1:
        return True
    if ligne_index_1==ligne_index_2 and car_index_1==car_index_2 + 1:
        return True
    return False

def played(state,player):
    ligne_index_player = ord(player[0]) - ord("A")
    car_index_player =  int(player[1]) - 1
    for ligne_index,ligne in enumerate(state):
        for car_index,car in enumerate(ligne):
            if touch(ligne_index_player,car_index_player,ligne_index,car_index):
                if car == "_":
                    state[ligne_index][car_index]="."
                else:
                    state[ligne_index][car_index]="_"

def main():
    """Point d'entree du programme"""
    state=[]
    with open(sys.argv[1]) as fichier:
        for ligne in fichier:
            cars=[]
            for car in ligne.strip():
                cars.append(car)
            state.append(cars)
    print_state(state)
    
    player_count=0

    while not finsihed_jeu(state):
        print("vous pouvez commencre a jouer:")
        player=input()
        player_count+=1
        played(state,player)
        print_state(state)
        
    print("felicitation vous gagner avec",player_count,"essaies")
main()

    















    
    





    











        
    










