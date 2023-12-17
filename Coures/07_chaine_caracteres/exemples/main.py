#!/usr/bin/env python3


from time import sleep

chiane = (
    "sidi va à l'école "
    "aprés sa bien "
)


print(chiane)

   
unicode_utf16 = "\u03A9"  # Ω
 
unicode_utf32 = "\U0001F602"  # 😂


print(unicode_utf16)
print(unicode_utf32)

texte = "Ceci est une ligne 1.\rCeci est une autre ligne 2."

print(texte)


# Afficher un timer qui s'écoule 

for i in range(10):
    print(f"\r00:0{i}" , end=" ")
    sleep(1)
    # print(f"\r00:0{i+1}" , end="")  
else :
    print("")


chemin = "C:\\utilisateurs\\utilisateur\\documents"
print(chemin)