import random
from  math import cos,sin



def triangle_aleatoire(A,B):
    points=str(random.randint(A[0],A[1]))
    for i in range(0,5):
        if i%2==0:
            points= points + "," +  str(random.randint(B[0],B[1]))
        else:
              points= points + " " +  str(random.randint(A[0],A[1]))

    return points
def tourne_triangle_autour(triangle,centre,angle):
    l=triangle.split(" ")
    points=""
    for i in range(len(l)):
        l[i]=l[i].split(",")
    
    for pt in l:
        x=(int(pt[0])-centre.x)*cos(angle)-(int(pt[1])-centre.y)*sin(angle)+centre.x
        y=(int(pt[0])-centre.x)*sin(angle)+(int(pt[1])-centre.y)*cos(angle)+centre.y

        points= points+ str(x) + "," + str(y) + " "

    return points

