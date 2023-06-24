#!/usr/bin/env python3

"test de la module ppm"

import ppm

def main():
    ppm.genere_en_tete(400,400)
    ppm.genere_background("blanc", 400 , 400)
    

    # ppm.genere_segement(ppm.Point(0,0),ppm.Point(200,200 ), 400 , 400)
    
main()