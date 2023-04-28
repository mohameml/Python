 #!/usr/bin/env python3



import random



def dans_disque(x,y,x_g,y_g,r):
    if (x-x_g)**2+(y-y_g)**2<=r**2:
        return True
    else:
        return False


print("P3")
print("400 400")
print("255")



for i in range(400):
    for j in range(400):
        x=random.uniform(0,399)
        y=random.uniform(0,399)
        if dans_disque(i,j,200,200,200):
            if i==int(x) and j==int(y) :
                print('255 0 255')
            else:
                print("255 255 255")


        else:
            print('255 255 255')
          




