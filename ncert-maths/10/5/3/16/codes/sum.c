#include <stdio.h>

// Function to perform convolution of two arrays
void convolution(const int *array1, int len1, const int *array2, int len2, int *result) {
    int lenResult = len1 + len2 - 1;
    for (int i = 0; i < lenResult; i++) {
        result[i] = 0;
    }
    for (int i = 0; i < len1; i++) {
        for (int j = 0; j < len2; j++) {
            result[i + j] += array1[i] * array2[j];
        }
    }
}

// Function to compute the sum of the first N terms of an arithmetic progression
void sum_of_ap(int a, int d, int N) {
    int x[N]; // Array to store terms of the AP
    for (int i = 0; i < N; i++) {
        x[i] = a + i * d; // Compute each term of the AP
    }

    int u[N]; // Array representing the unit step function
    for (int i = 0; i < N; i++) {
        u[i] = 1; // All elements are 1, indicating the unit step
    }
 
    int result[N + N - 1]; // Array to store the result of convolution
    convolution(x, N, u, N, result); // Compute the convolution of x and u
    
    FILE *file = fopen("result_terms.txt", "w"); // Open file for writing
    if (file == NULL) {
        printf("Error opening file.\n"); // Print error message if file opening fails
    }
    for (int i = 0; i < N ; i++) {
        fprintf(file, "%d\n",result[i]); // Write each term to the file
    }
    fclose(file); // Close the file
}

int main() {
    int a = 160;  // First term of the arithmetic progression
    int d = -20;  // Common difference of the arithmetic progression
    int N = 15; // Number of terms to sum

    // Computing the sum of the first N terms of the AP
    sum_of_ap(a, d, N);
    return 0;
}

