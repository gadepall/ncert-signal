#include <stdio.h>

// Function to calculate the sum of a geometric progression
double sum_of_GP(double x0, double d, int n) {
    double sum = 0;
    int i;
    for (i = 0; i < n; i++) {
        sum += x0;
        x0 *= d; // Multiply by the common ratio for the next term
    }
    return sum;
}

int main() {
    double x0 = 4; // First term
    double d = 4;  // Common ratio
    int n = 8;     // Number of terms

    // Calculate the sum of the geometric progression
    double sum = sum_of_GP(x0, d, n);

    // Print the result
    printf("Sum of the geometric progression: %lf\n", sum);

    return 0;
}
