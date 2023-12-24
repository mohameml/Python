
" exo1:"
print("-----------exo1-------------------")
# question1: une fonction qui retourn la frequence de chaque lettre d'un mot
print("----------Q1:---------------------")
def frequence_mot(chaine):
    d={}

    for c in chaine:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    return d

chaine="NebileeMohamed "
print(frequence_mot(chaine))

# question2 : une fonction qui permet verifie que deux mots sont anagrammes
print("-------------Q2----------------------")
" deux mots sont anagrammes:si ils sont composees des meme lettres  "

def est_anagrame(m1,m2):
    d1=frequence_mot(m1)
    d2=frequence_mot(m2)
    

    return d1.keys()==d2.keys()

print(est_anagrame("nebil","eebiiln"))


" exo2 :"

print("------------Exo2----------------------")

# Question1: une fonction qui calcule n! d'une maniere non recursive

print("--------------Q1:-----------------------")

def factoirlle_bon_recursive(n):
    s=n

    if n==0 or n==1:
        return 1
    
    while n-1!=0   :
        s=s*(n-1)
        n=n-1

    return s

print(factoirlle_bon_recursive(3))