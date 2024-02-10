// This code generates data by convolving two discrete inputs
// y(n) = x(n) * u(n)
#include <stdio.h>
#include <math.h>
#define SIZE 200 // Adjust the size according to your requirement

void convolution(float input1[], float input2[], float output[], float size) {
    for (int i = 0; i < size; i++) {
        output[i] = 0;
        for (int j = 0; j <= i; j++) {
            output[i] += input1[j] * input2[i - j];
        }
    }
}

int main() {
    FILE *file;
    file = fopen("allterms.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int size = SIZE;
    float u_n[SIZE], s_n[SIZE], conv_output[SIZE];

    // Initialize u(n)
    for (int i = 0; i < size; i++) {
        u_n[i] = (i >= 0) ? 1 : 0;
    }
    
    for (int i = 0; i < size; i++) {
        s_n[i] = (1.0 + 37*i/24.0 + 5.0*pow(i,2)/8 + pow(i,3)/12) * u_n[i];
    }

    // Generate (10+6n)u(n)
    float input1[SIZE];
    for (int i = 0; i < size; i++) {
        input1[i] = (i+2)*(i+2)/4 * u_n[i];
    }

    // Convolve (10+6n)u(n) with u(n)
    convolution(input1, u_n, conv_output, size);

    // Headers 
    fprintf(file, "n   x(n)*u(n)  s(n)\n");


    // Store the result in a text file
    for (int i = 0; i < size; i++) {
        fprintf(file, "%d   %f   %f\n",i, conv_output[i], s_n[i]);
    }

    fclose(file);

    return 0;
}
