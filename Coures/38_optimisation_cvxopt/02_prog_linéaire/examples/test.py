#!/usr/bin/env python3

"""
tester la fonction lp du biblo cvxopt.solvers

"""

from cvxopt import matrix , solvers
import numpy as np 

c= matrix([2.0 , 1.0])

A = np.array([[-1.0 , 1.0] , [-1.0 , -1.0] , [0.0 , -1.0] , [1.0, -2.0]])
print(A)


G =matrix([[-1.0 , -1.0 , 0.0 , 1.0] ,[1.0 , -1.0 , -1.0 , -2.0]])
print(G)

h= matrix([1.0 , -2.0 , 0.0 , 4.0])

G2= matrix(A)

print(G2)

sol = solvers.lp(c , G2 , h) 

print(f"Solution est : {sol['x']} ") # (0.5 , 1.5)

print(f"la valeur optimale est : {sol['primal objective']}") # 2.499999 -> 2.5 
