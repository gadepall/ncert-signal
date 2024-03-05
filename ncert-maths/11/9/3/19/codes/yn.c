#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("yn.dat", "w"); // Open file for writing

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int n;
    double yn;

    for (n = 0; n <= 4; n++) {
        yn = (-256.0 / pow(2, n)) + (512.0 / 1);
        fprintf(fp, "%d %f\n", n, yn); // Write n and y(n) to file
    }

    fclose(fp); // Close the file

    printf("Data has been saved to yn.dat\n");
    return 0;
}

