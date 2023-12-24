#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator in infix syntax
"""

import sys
import lexer

from parser import init_parser, parse_token, get_current

###################
## the public function of the calculator

def parse(stream=sys.stdin):
    init_parser(stream)
    l = parse_input()
    parse_token(lexer.END)
    return l


#########################
## parsing of input

def parse_input():
    return parse_inputX( [] )

def parse_inputX(l):
    if (get_current() == lexer.END) :
        return l
    n=parse_E2(l)
    parse_token(lexer.QUEST)
    return parse_inputX(l.append(n))

def parse_E2(l):

    n1=parse_E1(l)
    return parse_E2X(l,n1)


def parse_E2X(l,n1):
    



#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in infix syntax.")
    print("@ Type Ctrl-D to quit")
    print("@ result = ", repr(parse()))
