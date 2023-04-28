prix=int(input("donnez le prix:"))

while prix!=42:
    if prix<42:
        prix=int(input("le prix est superiure:"))
    if prix>42:
        prix=int(input("le prix est inferiuer:"))

if prix==42:
    print("bravo")


