
def tri_rapide(l):
    
    if len(l)<=1:
        return l
    
    else:
        pivot=l[0]
        val_inf,val_sup=[],[]
        for i in l[1:]:
            if i<pivot:
                val_inf.append(i)
            else:
                val_sup.append(i)
        
    return tri_rapide(val_inf) + [pivot] + tri_rapide(val_sup)

    
"test de la fonction"
l=[1,2,4,5,3,9,8,4,5]
L=tri_rapide(l)
print(L)
for i in L:
    print(i)

