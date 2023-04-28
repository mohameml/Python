"tout d'abord une fonction qui fusion deux liste trieès"
def fusion(l1,l2):
    l=[]
    i1,i2=0,0
    while i1<len(l1) and i2<len(l2):
        if l1[i1]<l2[i2]:
            l.append(l1[i1])
            i1+=1
        else:
            l.append(l2[i2])
            i2+=1
    if i1<len(l1):
        for i in range(i1,len(l1)):
            l.append(l1[i])
    else:
        for i in range(i2,len(l2)):
            l.append(l2[i])
    return l

"test du primere fonction fusion"
l1=[1,3,5,6,9]
l2=[2,4,7,8]
l=fusion(l1,l2)
print(l)
for i in l:
    print(i)

"fonction qui tri une liste par methode fusion   "

def tri_fusion(l):
    if len(l)<=1:
        return l
    else:
        m=len(l)//2
        return  fusion(tri_fusion(l[m:]),tri_fusion(l[:m]))

"test de la fonction tri_fusion "
l=[1,4,2,6,7,3,2]
L=tri_fusion(l)
print(L)


            