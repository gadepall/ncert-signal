#include<stdio.h>

int ap_values(int a, int n, int d){
    if(n >= 0){
        return a + n * d;
    }
    else{
        return 0;
    }
}

int main() {
    FILE *file = fopen("data1.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Discrete values for n
    for (int n = -3; n < 20; n++) {
        int k;
        k = ap_values(2, n, -6);
        if(n != 19){
            fprintf(file, "%d ", k);
        }
        else{
            fprintf(file, "%d", k);
            printf("%d\n", k); // Print k when n is 19
        }
    }
    
    fclose(file); // Don't forget to close the file
    return 0;
}

