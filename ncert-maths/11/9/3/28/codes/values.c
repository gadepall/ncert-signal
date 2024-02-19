#include <stdio.h>
#include <math.h>


int main() {
    FILE *fp;
    fp = fopen("data.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    double x0 = 1.0; // initial value of x(0)
    double r = 3 + 2 * sqrt(2); // root value

    for (int n = -4; n < 5; n++) {
        double x = 0.0;
        if (n >= 0) {
            x = x0 * pow(r, n);
        }
        fprintf(fp, "%d %.2lf\n", n, x);
    }

    fclose(fp);
    return 0;
}

