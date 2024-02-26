#include <stdio.h>
double calculateY(int n) {
    if (n >= 0) {
        return ((n + 1)) * (200 + n * 25);
    }
    else {
        return 0.0;
    }
}
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
void sum_of_ap(int a, int d, int N) {
    int x[N];
    for (int i = 0; i < N; i++) {
        x[i] = a + i * d;
    }
    int u[N];
    for (int i = 0; i < N; i++) {
        u[i] = 1;                                          
    }                                               
    int result[N + N - 1];
    convolution(x, N, u, N, result);
    FILE *file = fopen("result_terms.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");                   
    }
    for (int i = 0; i < N ; i++) {
        fprintf(file, "%d\n", result[i]);
    }
    fclose(file);
}
 int main() {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    fprintf(file, "n\t\ty(n)\n");
    for (int n = 0; n <= 29; ++n) {
        double result = calculateY(n);
        fprintf(file, "%d\t\t%.6f\n", n, result);
    }
       fclose(file);
       printf("Data written to output.txt successfully.\n");
    int a = 200;  // First term of the arithmetic progression
    int d = 50;  // Common difference of the arithmetic progression
    int N = 30; // Number of terms to sum
    // Computing the sum of the first N terms of the AP
    sum_of_ap(a, d, N);
    return 0;
}
