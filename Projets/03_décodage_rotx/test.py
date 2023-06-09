#!/usr/bin/env python3 

import rotx


# Test 1
print("---------- Test 1  ------------------")
chaine ="Oenib"
chaine_dec="".join([rotx.rot13(e) for e in chaine])
print("le decodage de la chaine 'Oenib' est : Bravo")
print("est Votre decodeur rotx return :",end="")
print(chaine_dec)


# Test 2
print("--- Test2 ---") 
chaine ="Oenib ibhf nirm grezvare   yr zvav cebwrg 03 "
chaine_dec ="".join([rotx.rot13(e) for e in chaine])
print("le decodage de la chaine 'Oenib ibhf nirm grezvare   yr zvav cebwrg 03' est : Bravo vous avez terminer   le mini projet 03")
print("est Votre decodeur rotx return :")
print(chaine_dec)