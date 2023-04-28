def tri_selection(l):
    for i in range(len(l)):
        indice_min = i  # on cherche l'indice de l'element le plus petit
        for j in range(i+1, len(l)):
            if l[indice_min] > l[j]:
                indice_min = j
        l[indice_min], l[i] = l[i], l[indice_min]
    return l


l = [12, 2, 4, 5, 13, 1, 8, 0, 2]
print(tri_selection(l))
