#include <stdio.h>
#include <stdlib.h>

// Function to perform convolution of two arrays
void convolution(int *A, int *B, int n, int *result) {
    for (int i = 0; i < n; i++) {
        result[i] = 0;
        for (int j = 0; j <= i; j++) {
            result[i] += A[j] * B[i - j];
        }
    }
}

int main() {
    int N = 30; // Maximum value of n
    int *A = (int *)malloc(N * sizeof(int));
    int *B = (int *)malloc(N * sizeof(int));
    int *result = (int *)malloc(N * sizeof(int));

    // Initialize arrays A and B
    for (int i = 0; i < N; i++) {
        A[i] = (i + 5) * (i + 5); // n^2 for n starting from 5
        B[i] = 1; // Constant term for convolution
    }

    // Perform convolution for each value of n
    convolution(A, B, N, result);

    // Print the result for each value of n
    for (int i = 0; i < N; i++) {
        printf("%d\n",result[i]);
    }

    free(A);
    free(B);
    free(result);

    return 0;
}
