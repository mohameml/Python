#!/usr/bin/env python3

def pivote(tab,indice_pivot):
    l_sup=[]
    l_inf=[]
    for i in range(len(tab)):
        if tab[i]<=tab[indice_pivot] and i!=indice_pivot:
            l_inf.append(tab[i])
        if tab[i]>tab[indice_pivot]:
            l_sup.append(tab[i])
    return(l_inf,l_sup)

l=[3,0,10,1,6,9,5,3,9,0,5,8,9,8,4,2,0,9,6,2]


print(len(l))
#pivote(l,0)

L=[1,2,4,6,8,2,0]
indice=0
l_inf,l_sup=pivote(l,0)
n1=len(l_inf)
n2=len(l_sup)
l[0:n1]=l_inf
l[n1]=l[indice]
l[n1:n2]=l_sup
print(l,len(l))





