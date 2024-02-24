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
	double x, y;
    
    for (x = -10; x <= 26; x += 0.1) {
        y = x*x - 16*x + 25;
        fprintf(fp, "%lf %lf\n", x, y); 
    }

    fclose(fp); // Close the file

    
    FILE *fp1, *fp2;
    fp1 = fopen("values1.dat", "w"); // Open for writing in text mode
    fp2 = fopen("values2.dat", "w"); // Open for writing in text mode

    if (fp1 == NULL || fp2 == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    double x0 = 8 + sqrt(39);
    double d =  -2*sqrt(39);
    double r = (8 - sqrt(39)) / (8 + sqrt(39));
    
    for (int n = -5; n <= 10; n++) {
        double xn1 = (x0 + n * d) * (n >= 0);
        double xn2 = x0 * pow(r, n) * (n >= 0);
        fprintf(fp1, "%d %lf\n", n, xn1); // Write n and xn1 to file1, separated by a space
        fprintf(fp2, "%d %lf\n", n, xn2); // Write n and xn2 to file2, separated by a space
    }

    fclose(fp1); // Close file1
    fclose(fp2); // Close file2

    return 0;
}

