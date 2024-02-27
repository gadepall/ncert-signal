#include <stdio.h>
#include <math.h>

int u(int n) {
    if (n >= 0) return 1;
    else return 0;
}

double power(double b, int e)
     {
     double r=1;
     int i;
     for(i=0;i<e;i++)
     {
     r*=b;
     }
     return r;
     }

float series_values(int n) {
    return ((2*n+3)*power((n+1),2)) * u(n);
}

void convolve(float sig1[], int sig2[], float res[], int size1, int size2) {
    int len_result = size1 + size2 - 1;

    for (int i = 0; i < len_result; i++) {
        res[i] = 0;
        for (int j = 0; j < size1; j++) {
            if (i - j >= 0 && i - j < size2) {
                res[i] += sig1[j] * sig2[i - j];
            }
        }
    }
} // function to convolve the arrays

int main() {
    FILE *fp;
    fp = fopen("values2.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    float sig1[11];
    int sig2[11]; // Adjusted the size to match sig1
    for (int i = 0; i < 11; i++) {
        sig1[i] = series_values(i);
        sig2[i] = u(i);
    }

    float res[21]; // Changed the size to match the result of convolution
    float sum=0;
    convolve(sig1, sig2, res, 11, 11);
    for (int i = 0; i < 11; i++) { // Adjusted the loop to match res size
        sum += sig1[i];
        fprintf(fp, "%d\t%.2f\t%.2f\n", i, sum, res[i]);
    }

    fclose(fp);
}

