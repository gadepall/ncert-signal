#include <stdio.h>
#include <math.h>

int u(int n) {
    if (n >= 0) return 1;
    else return 0;
}

float ap_values(float x0, float d, int n) {
    return (x0 + n * d) * u(n);
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
    fp = fopen("values1.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    float sig1[16];
    int sig2[16]; // Adjusted the size to match sig1
    for (int i = 0; i < 16; i++) {
        sig1[i] = ap_values(5, 2.67 , i);
        sig2[i] = u(i);
    }

    float res[31]; // Changed the size to match the result of convolution
    float sum=0;
    convolve(sig1, sig2, res, 16, 16);
    for (int i = 0; i < 16; i++) { // Adjusted the loop to match res size
        sum += sig1[i];
        fprintf(fp, "%d\t%.2f\t%.2f\n", i, sum, res[i]);
    }

    fclose(fp);
}

