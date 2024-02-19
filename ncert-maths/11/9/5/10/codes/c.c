#include <stdio.h>
#include <math.h>

// Function to calculate power of 2 recursively
double power_of_2(int exponent) {
    if (exponent == 0)
        return 1;
    else if (exponent > 0)
        return 2 * power_of_2(exponent - 1);
    else
        return 0.5 * power_of_2(exponent + 1);
}

// Function to save values of 2^(n+3) and 2^(5-n) to files recursively
void save_values(int n, int limit, FILE *file1, FILE *file2) {
    if (n > limit)
        return;

    double value1 = power_of_2(n + 3);
    double value2 = power_of_2(5 - n);

    fprintf(file1, "%.2f\n", value1);
    fprintf(file2, "%.2f\n", value2);

    save_values(n + 1, limit, file1, file2);
}

int main() {
    // Open files for writing
    FILE *file1 = fopen("py_1.txt", "w");
    FILE *file2 = fopen("py_2.txt", "w");

    if (file1 == NULL || file2 == NULL) {
        printf("Error opening files.\n");
        return 1;
    }

    // Save values recursively
    save_values(0, 15, file1, file2);

    // Close files
    fclose(file1);
    fclose(file2);

    printf("Values saved successfully.\n");

    return 0;
}
