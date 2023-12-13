# Exercice :

L’objectif de cet exercice est de programmer une recherche dans une liste triée.


- **``TODO 1:``**
    
    - Il faut d’abord récupérer le ﬁchier texte **``noms.txt``** . 
    
    - Ce ﬁchier contient un mot par ligne. Il faut lire ce ﬁchier et construire une liste avec tous ces mot.

- **``TODO 2:``**

    - Construire une fonction qui vériﬁe que la liste chargée à la question précédente est triée.

- **``TODO 3:``**
    
    - Construire une fonction qui recherche un mot X dans la liste et qui retourne sa position ou -1 si ce mot n’y est pas. 
    
    - Cette fonction prend deux paramètres : la liste et le mot à chercher. Elle retourne un entier.  
    
    - Quels sont les positions des mots **UN** et **DEUX**



- Lorsqu’une liste est triée, rechercher un élément est beaucoup plus rapide. Si on cherche le mot X dans la liste, il suffit de le comparer au mot du milieu pour savoir si ce mot est situé dans la partie basse (X inférieur au mot du milieu), la partie haute (X supérieur au mot du milieu). S’il est égal,
le mot a été trouvé. Si le mot n’a pas été trouvé, on recommence avec la sous-liste inférieure ou supérieure selon les cas jusqu’à ce qu’on ait trouvé le mot ou qu’on soit sûr que le mot cherché n’y est pas.

- Le résultat de la recherche est la position du mot dans la liste ou -1 si ce mot n’a pas été trouvé. Cette recherche s’appelle une **``recherche dichotomique``**.

- Ecrire la fonction qui eﬀectue la recherche dichotomique d’un mot dans une liste triée de mots.
Vériﬁez que les deux fonctions retournent bien les mêmes résultats. Cette fonction peut être récursive
ou non. Elle prend au moins les deux mêmes paramètres que ceux de la question 3, si elle en a
d’autres, il faudra leur donner une valeur par défaut. On précise que les comparaisons entre chaînes
de caractères utilisent aussi les opérateu


- **``TODO 2:``**
- **``TODO 2:``**
- **``TODO 2:``**
- **``TODO 2:``**
- **``TODO 2:``**
