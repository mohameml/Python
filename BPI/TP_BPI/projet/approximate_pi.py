#!/usr/bin/env python3

import sys
import random

n=int(sys.argv[1])
cmp=0

def gener_point():
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    return x,y

def dans_disque(x,y,r):
    if x**2+y**2<=r**2:
        return True
    else:
        return False

    
    
for i in range(1,n):
    x,y=gener_point()
    if dans_disque(x,y,1):
        cmp+=1
if __name__=='__main__':
    n=int(sys.argv[1])
    pi=4*(cmp/n)

    print(pi)


    
