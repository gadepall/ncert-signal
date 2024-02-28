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
    int a = 2, d = 7;

    for (int n = 1; n <= 40; n++) {
        int *A = (int *)malloc(n * sizeof(int));
        int *B = (int *)malloc(n * sizeof(int));
        int *result = (int *)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) {
            A[i] = a + (i * d);
            B[i] = 1;
        }
        convolution(A, B, n, result);
        printf("%d\n",result[n - 1]);
        free(A);
        free(B);
        free(result);
    }

    return 0;
}
