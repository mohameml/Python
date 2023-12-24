#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator in prefix syntax
"""

import lexer
import sys

from parser import init_parser, parse_token, get_current, Error

###################
## the public function of the calculator

def parse(stream = sys.stdin):
    init_parser(stream)
    return parse_input([])

#########################
## parsing of input

def parse_input(l):
    print("@ATTENTION: pcalc.parse_input à corriger !") # LIGNE A SUPPRIMER
    n = parse_exp(l)
    return l+[n]


#########################
## parsing of expressions

def parse_exp(l):
    return parse_token(lexer.NAT)


#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in prefix syntax.")
    print("@ Type Ctrl-D to quit")
    l=parse()
    print("@ result = ", repr(l))
