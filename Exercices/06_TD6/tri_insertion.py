def tri_insertion(L):
    "fonction qui trie les elements d'une liste par la methode insertion "
    for i in range(1,len(L)):
        val=L[i]   # on recupere la valeur L[i]
        j=i-1 
        while j>=0 and L[j]>val:
            L[j+1]=L[j]
            j-=1
        L[j+1]=val
    return L

" test de la fonction "
l=[12,2,4,5,13,1,8,0,2]
L=tri_insertion(l)
print(L)
" un autre mode d'affichage"
for i in L:
    print(i)












