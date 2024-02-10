#include <stdio.h>
#include <math.h>

#define a 21
#define x 1.2

int main() {
    FILE *fp;
    int n[a];
    double X[a];

    for (int i = 0; i < a; i++) {
        n[i] = i;
        X[i] = pow(x, 2 * i + 3);
    }

    fp = fopen("data.dat", "w");  // Use "w" for plain text writing
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Writing data in plain text format
    for (int i = 0; i < a; i++) {
        fprintf(fp, "%d\t %.10f\n", n[i], X[i]);
    }

    fclose(fp);
    return 0;
}

