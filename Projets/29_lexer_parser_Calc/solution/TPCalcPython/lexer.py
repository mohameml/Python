#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lexer for the various calculators of TL2
"""

import sys

###############################
# Definition of tokens and separators
# Update TOKEN_PREFIX here and add new names in order to add new tokens

SEP = {' ', '\n', '\t'}
TOKEN_PREFIX = ('?', '+', '-', '*', '/', '(', ')', '', '#', '')
TOKENS = tuple(range(len(TOKEN_PREFIX)))
QUEST, PLUS, MINUS, MULT, DIV, OPAR, CPAR, NAT, CALC, END = TOKENS

# A map from token prefixes to tokens without attribute (eg. no NAT or CALC)
# and without END (to avoid moving too far in the input stream)
TOKEN_MAP = {'?': QUEST}
for token in PLUS, MINUS, MULT, DIV, OPAR, CPAR, CALC:
    TOKEN_MAP[TOKEN_PREFIX[token]] = token


#################################
# private functions and variables of the lexer

def is_digit(char):
    return '0' <= char <= '9'

# Parsing functions returning an attributed token given which token we want
# They also take care of updating current_char (except for parse_END as there
# is no further character to read).
def parse_END():
    return (END, None)

def parse_digit():
    if not is_digit(current_char):
        raise expected_digit_error(current_char)
    value = ord(current_char) - ord('0')
    update_current()
    return value

def parse_NAT():
    value = parse_digit()
    while is_digit(current_char):
        d = parse_digit()
        value = value * 10 + d
    return (NAT, value)

def parse_CALC():
    update_current()
    if is_digit(current_char):
        (_, val) = parse_NAT()
        return (CALC, val)
    else:
        raise unknown_token_error(current_char)

# Parse any token which does not require computing an attribute
# (and consumme the corresponding character in the input stream)
def parse_others():
    tok = TOKEN_MAP[current_char]
    update_current()
    return (tok, None)

# parse_token parses a symbol from the input and returns its token,
# consumming all symbols from the input corresponding to that token
def get_token():
    if is_digit(current_char):
        return parse_NAT()
    elif current_char == TOKEN_PREFIX[END]:
        return parse_END()
    elif current_char == TOKEN_PREFIX[CALC]:
        return parse_CALC()
    else:
        return parse_others()

in_stream = sys.stdin
current_char = ''

def update_current():
    global current_char
    current_char = in_stream.read(1)
    # print("@", repr(current_char))  # decomment this line may help debugging

def init_current():
    global current_char
    if current_char == '':
        update_current()


#################################
# public functions of the lexer

# Error handling
class Error(Exception):
    pass

def expected_digit_error(char):
    return Error('Expected a digit, but found ' + repr(char))

def unknown_token_error(char):
    return Error('Unknown start of token ' + repr(char))


# Return a string representing an attributed token
def str_attr_token(token, value):
    s = TOKEN_PREFIX[token]
    if token in (NAT, CALC):
        assert isinstance(value, int) and value >= 0
        s += str(value)
    else:
        assert value is None
    return s


# Reinitializes the input stream
def reinit(stream=sys.stdin):
    global in_stream, current_char
    assert stream.readable()
    in_stream = stream
    current_char = ''


# Computes the next token in the input (and move current_char accordingly)
def next_token():
    init_current()
    # init current_char if 'reinit' has been called
    # (or a previous Error has closed in_stream)
    while current_char in SEP: # skip separators
        update_current()
    try:
        return get_token() # parse a token
    except KeyError:
        raise unknown_token_error(current_char)


if __name__ == "__main__":
    print("@ Testing the lexer. Just type tokens and separators")
    print("@ Each token should appear once by line")
    print("@ Type Ctrl-D to quit")
    while True:
        token, value = next_token()
        print("@", str_attr_token(token, value))
        if token == END:
            break
