#include <stdio.h>
#include <stdlib.h>

int somme(int longueur, int tableau[longueur]) {
    int somme = 0;
    for (int i = 0; i < longueur; i++) {
        somme += tableau[i];
    }
    return somme;
}

int somme_indices_pairs(int longueur, int tableau[longueur]) {
    int somme = 0;
    for (int i = 0; i < longueur; i+=2) {
        somme += tableau[i];
    }
    return somme;
}

int main(){
    int* tab = malloc(5 * sizeof(int));
    tab[0] = 1;
    tab[1] = 2;
    tab[2] = 3;
    tab[3] = 4;
    tab[4] = 5;
    printf("somme = %d\n", somme(5, tab));
    printf("somme indices pairs = %d\n", somme_indices_pairs(5, tab));
    return 0;
}
