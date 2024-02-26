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
    FILE *file = fopen("data2.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = -3; n <= 20; n++) {
        int k = ap_values(10000, n, 500);
        if(n != 20){
            fprintf(file, "%d ", k);
        }
        else{
            fprintf(file, "%d", k);
        }
    }
    
    fclose(file); 
}

