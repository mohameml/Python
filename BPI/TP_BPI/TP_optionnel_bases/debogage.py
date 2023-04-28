import pdb


def addition(a, b):
    result = a + b
    return result


pdb.set_trace()
x = input("Saisissez un nombre : ")
y = input("Saisissez un autre nombre : ")
som = addition(int(x), int(y))
print(som)
