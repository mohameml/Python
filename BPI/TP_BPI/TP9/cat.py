#!/usr/bin/env python3

import sys 
arg=sys.argv
fichier=open(arg[1],"r")

print(fichier.readlines())

fichier.close()




