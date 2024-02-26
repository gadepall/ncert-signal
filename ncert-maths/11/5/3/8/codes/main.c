#include <stdio.h>
#define SIZE 51
int x(int n) {
    return (4*n+10);
}

void convolution(int input1[], int input2[], int output[], int size) {
    for (int i = 0; i < size; i++) {
        output[i] = 0;
        for (int j = 0; j <= i; j++) {
            output[i] += input1[j] * input2[i - j];
        }
    }
}

int main() {
    FILE *fp;
    fp = fopen("output.dat", "w"); // Open file for writing

    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    int n = 15; // Number of terms
    int a=10;
    int d=4;
    int sum=0;


    // 2nd part of code DOING CONVOLUTION TO OBTAIN SUM OF N TERMS AND STORING VALUES IN TEXT FILE

    int size = SIZE;
    int u_n[SIZE], conv_output[SIZE];

    // Initialize u(n)
    for (int i = 0; i < size; i++) {
        u_n[i] = (i >= 0) ? 1 : 0;
    }

    // Generate (10+6n)u(n)
    int input1[SIZE];
    for (int i = 0; i < size; i++) {
        input1[i] = (10 + 4 * i) * u_n[i];
    }

    // Convolve (10+6n)u(n) with u(n)
    convolution(input1, u_n, conv_output, size);

    // Headers 
    fprintf(fp, "n y(n)\n");


    // Store the result in a text file
    for (int i = 0; i < size; i++) {
        fprintf(fp, "%d %d\n",i, conv_output[i]);
    }

    fclose(fp);

    return 0;
}
