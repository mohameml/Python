#!/usr/bin/env python3

"""
Analyse syntaxique LL(1) de la BNF G1 du chapitre 3 :


 (1) S|w -> O|w1 c    w=w1.a              |  Dic(1)={a,b,c}
 -----------------------------------------|------------------
 (2) O|w -> P|w1      w=w1.c              |  Dic(2)={a,b}
 (3)       | epsilon    w=epsilon         |  Dic(3)={c}
 -----------------------------------------|-------------------
 (4) P|w -> b                             |  Dic(4)={b}
 (5)       | aP|w1 c P|w2   w=b.w1.c.a.w2 |  Dic(5)={a}
 -----------------------------------------|---------------
    
"""

import io

#################################
# lexer


TOKENS = tuple(range(4))
a, b, c, END = TOKENS  # END = token spécial de fin de fichier
TOKEN_NAME = 'a', 'b', 'c', ''


SWITCH = {'': END,
          'a': a,
          'b': b,
          'c': c}


def next_token():
    return SWITCH[stream.read(1)]


#################################
# generic functions of LL(1) parsing


def init_parser(txt: str):
    global current, stream
    stream = io.StringIO(txt)
    current = next_token()


class Error(Exception):
    pass


def parse_token(token):
    global current
    if current != token:
        raise Error('found token ' + repr(TOKEN_NAME[current]) +
                    ' but expected ' + repr(TOKEN_NAME[token]))
    if current != END:
        current = next_token()
# version 1 (without select and mkrules)


def parse_v1(txt: str):
    init_parser(txt)
    w = parse_S_v1()
    parse_token(END)
    return w


def parse_S_v1():
    w1 = parse_O_v1()
    parse_token(c)
    return w1 + "a"


def parse_O_v1():
    if current in [a, b]:
        w1 = parse_P_v1()
        return w1 + "c"
    else:
        return ""


def parse_P_v1():
    if current == b:
        parse_token(b)
        return ""
    else:
        parse_token(a)
        w1 = parse_P_v1()
        parse_token(c)
        w2 = parse_P_v1()
        return "b" + w1 + "ca" + w2
# tests


def check(txt: str, result: str):
    assert len(txt) == len(result)
    s = {'a': 'b', 'b': 'c', 'c': 'a'}
    for i, c in enumerate(txt):
        assert s[c] == result[i]


def test(parse, txt: str, ok: bool = True):
    print("@ input:", txt)
    try:
        w = parse(txt)
        print("@ result:", w)
        print()
        assert ok
        check(txt, w)
    except Error as e:
        print("@ error:", e)
        print()
        assert not ok


def exec_tests(parse):
    print("@@@@@@ test: ", parse)
    test(parse, "ca", False)
    test(parse, "ac", False)
    test(parse, "abc", False)
    test(parse, "abcb", False)
    test(parse, "c")
    test(parse, "bc")
    test(parse, "abcbc")
    test(parse, "abcabcbc")
    test(parse, "aabcbcbc")


exec_tests(parse_v1)
