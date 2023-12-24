#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TP TL1: implémentation des automates
"""

import sys

###############
# Cadre général

V = set(('.', 'e', 'E', '+', '-')
        + tuple(str(i) for i in range(10)))

class Error(Exception):
    pass

INPUT_STREAM = sys.stdin
END = '\n' # WARNING: test_tp modifies the value of END.

# Initialisation: on vérifie que END n'est pas dans V
def init_char():
    if END in V:
        raise Error('character ' + repr(END) + ' in V')

# Accès au caractère suivant dans l'entrée
def next_char():
    global INPUT_STREAM
    ch = INPUT_STREAM.read(1)
    # print("@", repr(ch))  # decommenting this line may help debugging
    if ch in V or ch == END:
        return ch
    raise Error('character ' + repr(ch) + ' unsupported')


############
# Question 1 : fonctions nonzerodigit et digit

def nonzerodigit(char):
    assert (len(char) <= 1)
    return '1' <= char <= '9'

def digit(char):
    assert (len(char) <= 1)
    return '0' <= char <= '9'


############
# Question 2 : integer et pointfloat sans valeur

def integer_Q2():
    init_char()
    return integer_Q2_state_0()


def integer_Q2_state_0():
    ch = next_char()
    print("@ATTENTION: integer_Q2_state_0 à finir !") # LIGNE A SUPPRIMER


def integer_Q2_state_1():
    ch = next_char()
    print("@ATTENTION: integer_Q2_state_1 à finir !") # LIGNE A SUPPRIMER


def integer_Q2_state_2():
    ch = next_char()
    print("@ATTENTION: integer_Q2_state_2 à finir !") # LIGNE A SUPPRIMER


def pointfloat_Q2():
    init_char()
    return pointfloat_Q2_state_0()

# Définir ici les fonctions manquantes


############
# Question 5 : integer avec calcul de la valeur
# si mot accepté, renvoyer (True, valeur)
# si mot refusé, renvoyer (False, None)

# Variables globales pour se transmettre les valeurs entre états
int_value = 0
exp_value = 0

def integer():
    print("@ATTENTION: integer à finir !") # LIGNE A SUPPRIMER


def integer_state_0():
    global int_value
    ch = next_char()
    print("@ATTENTION: integer_state_0 à finir !") # LIGNE A SUPPRIMER


def integer_state_1():
    global int_value
    ch = next_char()
    print("@ATTENTION: integer_state_1 à finir !") # LIGNE A SUPPRIMER


def integer_state_2():
    global int_value
    ch = next_char()
    print("@ATTENTION: integer_state_2 à finir !") # LIGNE A SUPPRIMER


############
# Question 7 : pointfloat avec calcul de la valeur

def pointfloat():
    global int_value
    global exp_value
    init_char()
    int_value = 0.
    exp_value = 0
    return pointfloat_state_0()


# Définir ici les fonctions manquantes


############
# Question 8 : exponent, exponentfloat et number

# La valeur du signe de l'exposant : 1 si +, -1 si -
sign_value = 0



########################
#####    Projet    #####
########################


V = set(('.', 'e', 'E', '+', '-', '*', '/', '(', ')', ' ')
        + tuple(str(i) for i in range(10)))


############
# Question 10 : eval_exp

def eval_exp():
    print("@ATTENTION: eval_exp à finir !") # LIGNE A SUPPRIMER
    ch = next_char()
    if ch == '+':
        n1 = eval_exp()
        n2 = eval_exp()
        return n1 + n2


############
# Question 12 : eval_exp corrigé

current_char = ''

# Accès au caractère suivant de l'entrée sans avancer
def peek_char():
    global current_char
    if current_char == '':
        current_char = INPUT_STREAM.read(1)
    ch = current_char
    # print("@", repr(ch))  # decommenting this line may help debugging
    if ch in V or ch in END:
        return ch
    raise Error('character ' + repr(ch) + ' unsupported')

def consume_char():
    global current_char
    current_char = ''


def number_v2():
    print("@ATTENTION: number_v2 à finir !") # LIGNE A SUPPRIMER


def eval_exp_v2():
    print("@ATTENTION: eval_exp_v2 à finir !") # LIGNE A SUPPRIMER


############
# Question 14 : automate pour Lex

operator = set(['+', '-', '*', '/'])

def FA_Lex():
    print("@ATTENTION: FA_lex à finir !") # LIGNE A SUPPRIMER


############
# Question 15 : automate pour Lex avec token

# Token
NUM, ADD, SOUS, MUL, DIV, OPAR, FPAR = range(7)
token_value = 0



def FA_Lex_w_token():
    print("@ATTENTION: FA_lex_w_token à finir !") # LIGNE A SUPPRIMER



# Fonction de test
if __name__ == "__main__":
    print("@ Test interactif de l'automate")
    print("@ Vous pouvez changer l'automate testé en modifiant la fonction appelée à la ligne 'ok = ... '.")
    print("@ Tapez une entrée:")
    try:
        ok = integer_Q2() # changer ici pour tester un autre automate sans valeur
        # ok, val = integer() # changer ici pour tester un autre automate avec valeur
        # ok, val = True, eval_exp() # changer ici pour tester eval_exp et eval_exp_v2
        if ok:
            print("Accepted!")
            # print("value:", val) # décommenter ici pour afficher la valeur (question 4 et +)
        else:
            print("Rejected!")
            # print("value so far:", int_value) # décommenter ici pour afficher la valeur en cas de rejet
    except Error as e:
        print("Error:", e)
