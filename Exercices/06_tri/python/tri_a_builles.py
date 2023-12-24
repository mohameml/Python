#
"""
principe consiste a comparer chaque element par l'element qui le suit et permuter si ne respecte 
pas l'ordre

"""

def tri_bulle(l):
    permission = True
    n= len(l)
    while permission :
        permission=False

     
        for i in range(n-1):
           if l[i]>l[i+1]:
               l[i],l[i+1]=l[i+1],l[i]
               permission=True
        n=n-1 # car a  la fin de chaque etape le plus grand element et bien place a la bon place donc on dumine n en fin de dimunier la complexite
    
    return l

l=[10,23,2,4,5,7,1,4,5,9]
print(tri_bulle(l))


