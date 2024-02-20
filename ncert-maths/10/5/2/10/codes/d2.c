#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w"); // Open for writing in text mode

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
	int x0 = 2;
	int d = 1;
    for (int n = -5; n <= 10; n++) {
        double xn = (x0 + n*d)*(n >= 0);
        fprintf(fp, "%d %lf\n", n, xn); // Write n and xn to file, separated by a space
    }

    fclose(fp); // Close the file

    return 0;
}
