// This code generates data by convolving two discrete inputs
// y(n) = x(n) * u(n)
#include <stdio.h>
#define SIZE 50 // Adjust the size according to your requirement

void convolution(int input1[], int input2[], int output[], int size) {
    for (int i = 0; i < size; i++) {
        output[i] = 0;
        for (int j = 0; j <= i; j++) {
            output[i] += input1[j] * input2[i - j];
        }
    }
}

int main() {
    FILE *file;
    file = fopen("convolution_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int size = SIZE;
    int u_n[SIZE], conv_output[SIZE];

    // Initialize u(n)
    for (int i = 0; i < size; i++) {
        u_n[i] = (i >= 0) ? 1 : 0;
    }

    // Generate (10+6n)u(n)
    int input1[SIZE];
    for (int i = 0; i < size; i++) {
        input1[i] = (10 + 6 * i) * u_n[i];
    }

    // Convolve (10+6n)u(n) with u(n)
    convolution(input1, u_n, conv_output, size);

    // Headers 
    fprintf(file, "n   y(n)\n");


    // Store the result in a text file
    for (int i = 0; i < size; i++) {
        fprintf(file, "%d   %d\n",i, conv_output[i]);
    }

    fclose(file);

    return 0;
}
