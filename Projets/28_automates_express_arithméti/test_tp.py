#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test des fonctions du TP
"""

import io
import tp
import math

# NOM des fonctions à tester:
#  - une chaîne vide pour ne pas tester
#  - le nom de la fonction à tester sinon

test_integer_Q2    = "tp.integer_Q2"
test_pointfloat_Q2 = "" # à remplacer par "tp.pointfloat_Q2"
test_integer       = "" # à remplacer par "tp.integer"
test_pointfloat    = "" # à remplacer par "tp.pointfloat"
test_exponent      = "" # à remplacer par "tp.exponent"
test_exponentfloat = "" # à remplacer par "tp.exponentfloat"
test_number        = "" # à remplacer par "tp.number"


# Le caractère de fin est \0, et non \n
tp.END = ''

# DRIVERS de tests avec et sans valeur calculée

def test_single_wo_val(function_to_test, expected_result, test_input):
    """function_to_test = name of the function to test
       expected_result = True or False or None (where None means tp.Error expected)
       test_input = string in input"""
    print("@ ", function_to_test, "on", repr(test_input), "expect:",  expected_result)
    tp.INPUT_STREAM = io.StringIO(test_input)
    try:
        found_result = eval(function_to_test+"()")
        assert expected_result != None, ("an exception is expected instead of normally return " + repr(found_result))
        assert expected_result == found_result, ("found " + repr(found_result))
    except tp.Error as e:
        assert expected_result == None, ("unexpected " + repr(e))


def test_all_wo_val(function_to_test, expected_result, test_inputs):
    for i in test_inputs:
        test_single_wo_val(function_to_test, expected_result, i)
    print("@---- ", function_to_test, "=>", expected_result, " PASSED!")
    print()



def test_single(function_to_test, expected_result, test_input):
    """function_to_test = name of the function to test
       expected_result = True or False or None (where None means tp.Error expected)
       test_input = string in input"""
    print("@ ", function_to_test, "on", repr(test_input), "expect:",  expected_result)
    if expected_result:
        if function_to_test == "tp.exponent":
            actual_input = float(test_input[1:])
        else:
            actual_input = float(test_input)
        assert math.isfinite(actual_input),\
            ("please remove this irrelevant test ('{0}' is float '{1}' which is not finite)".format(test_input, actual_input))
    tp.INPUT_STREAM = io.StringIO(test_input)
    try:
        ok, result = eval(function_to_test+"()")
        assert expected_result != None,\
            ("an exception is expected instead of normally return " + repr((ok, result)))
        if expected_result:
            assert ok==True and float(result) == actual_input,\
                   ("found " + repr((ok, result)))
        else:
            assert (not ok) and result == None,\
                   ("found " + repr((ok, result)))
    except tp.Error as e:
        assert expected_result == None, ("unexpected " + repr(e))


def test_all(function_to_test, expected_result, test_inputs):
    for i in test_inputs:
        test_single(function_to_test, expected_result, i)
    print("@---- ", function_to_test, "=>", expected_result, " PASSED!")
    print()


# Les tests proprement dits.

# D'abord, sans valeurs
if test_integer_Q2:
    test_all_wo_val(test_integer_Q2, True, 
                    ["1234567890098700", "203", "0000", 
                     "0", "1","2","3","4","5","6","7","8","9"])
    test_all_wo_val(test_integer_Q2, False, 
                    ["01","","123e","000e","2.5",".5","0.0","3.", "1e5", "2e+5", "1e-5", "-25"])
    test_all_wo_val(test_integer_Q2, None, ["a2","0a0","1a0"])

if test_pointfloat_Q2:
    test_all_wo_val(test_pointfloat_Q2, True, 
                    ["4.", "5.4", ".5", "0123.", ".123", "678.876", 
                     "0.", "000.000", ".0"])
    test_all_wo_val(test_pointfloat_Q2, False, 
                    ["123", "0", "1", ".", ".123e5", "1.e+5", "2e5", "1.5e+6", "",
                     "-.5"])
    test_all_wo_val(test_pointfloat_Q2, None, ["1.a2","0.a0","1a."])

# Ensuite, avec valeurs
if test_integer:
    test_all(test_integer, True, 
             ["1234567890098700", "203", "0000", 
              "0", "1","2","3","4","5","6","7","8","9"])
    test_all(test_integer, False, 
             ["01","","123e","000e","2.5",".5","0.0","3.", "1e5", "2e+5", "1e-5", "-25"])
    test_all(test_integer, None, ["a2","0a0","1a0"])

if test_pointfloat:
    test_all(test_pointfloat, True, 
             ["4.", "5.4", ".5", "0123.", ".123", "678.876", 
              "0.", "000.000", ".0"])
    test_all(test_pointfloat, False, 
             ["123", "0", "1", ".", ".123e5", "1.e+5", "2e5", "1.5e+6", "", 
              "-.5"])
    test_all(test_pointfloat, None, ["1.a2","0.a0","1a."])

if test_exponent:
    test_all(test_exponent, True, 
             ["e5", "e+5", "e-5", "e1234567890098700", "E203", "e+125", "e-3", 
              "E+4","e0","E0", "e+0", "e-0", "E+0", "E-0", "e6", "e-5", 
              "e7","e8","E+9","e-1", "e+4321", "E-67", "E+124", "E+12", 
              "e-98500", "e12", "e-1"])
    test_all(test_exponent, False, 
             ["", "e", "E", "+", "-", "e+", "e-", "E", "1e5", "1", "2.", 
              "ee5", "e+-5", "E++5", "E-+5", "e+3+"])
    test_all(test_exponent, None, [ "a2","e+a0","e1a0" ])

if test_exponentfloat:
    test_all(test_exponentfloat, True, 
             ["1e5", "1e+5", "1e-5", "1234567890098700e-1234567890098700",
               "1234e123", "203E203", "000e+125", "0e-3", "1E+4","2e0","3E0","4e6",
              "5e-5","6e7","7e8","8E+9","9e-1", "4.e+43", "5.4E-67",
              ".5e0", "0123.e-0", ".123E+0", "678.876E-0", "0.e+124",
              "000.000E+12", ".0e-98500"])
    test_all(test_exponentfloat, False, 
             ["1ee5", "1", "2.", "1e", "e", "+", "-", "1e+-5", "e5", 
              "e+5", "+1e5", "-1e5", "", "1e+"])
    test_all(test_exponentfloat, None, ["1.a2","0.ae0","1e+a0","1e1a0"])

if test_number:
    test_all(test_number, True, 
             ["1234567890098700", "203", "0000", 
              "0", "1","2","3","4","5","6","7","8","9",
              "4.", "5.4", ".5", "0123.", ".123", "678.876",
              "0.", "000.000", ".0",
              "1e5", "1e+5", "1e-5", "1234567890098700e-1234567890098700",
              "1234567890098700e123",
              "203E203", "000e+125", "0e-3", "1E+4","2e0","3E0","4e6",
              "5e-5","6e7","7e8","8E+9","9e-1", "4.e+43", "5.4E-67",
              ".5e0", "0123.e-0", ".123E+0", "678.876E-0", "0.e+124",
              "000.000E+12", ".0e-98500"])
    test_all(test_number, False,
             ["1ee5", "1e-", "2.E+", "1e", "e", "+", "-", "1e+-5", "e5", 
              "e+5", "+1e5", "-1e5", "", "1e+"])
    test_all(test_number, None, 
             ["a2","0a0","1a0","1.a2","0.a0","1a.","2e+a0","1e1a0"])

print()
print("@ all tests OK !")
