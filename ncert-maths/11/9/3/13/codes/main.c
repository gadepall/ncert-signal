#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    int n = 5; // Number of terms in the GP
    int a = 3; // First term
    int r = 3; // Common ratio
    int sum = 0;
    int i;
    int x_n;

    fp = fopen("gp_sum.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    for (i = 0; i < n; i++) {
        sum += a;
        x_n=pow(r,i+1);
        fprintf(fp, "%d %d %d\n", i+1, x_n, sum);
        a *= r;
    }

    fclose(fp);
    
    
    fp = fopen("terms.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    for (i = 0; i < n; i++) {
        x_n=pow(r,i+1);
        fprintf(fp, "%d  %d\n", i+1, x_n);
     
    }

    fclose(fp);
    return 0;

}