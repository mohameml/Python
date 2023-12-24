#!/usr/bin/env python3


def nonzerodigit(char):
    assert (len(char) <= 1)
    return '1' <= char <= '9'


print(nonzerodigit(2))
