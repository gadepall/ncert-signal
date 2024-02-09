#include <stdio.h>
#include <math.h>

int main() {
    // Define the parameters
    int x_0 = 5;  // Initial value of the signal
    int r = 2;    // Common ratio

    // Number of terms to generate
    int num_terms = 6;

    // Open the .dat file for writing
    FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    // Write the input values to the file for y(n) and x(n)
    fprintf(file, "n\tx(n)\ty(n)\n");

    // Generate and write the sequence values for y(n) and x(n)
    double sum_x = 0;

    for (int n = 0; n < num_terms; n++) {
        int y_n = x_0 * ((pow(r, n + 1) - 1) / (r - 1)) * (n >= 0);

        int x_n = x_0 * pow(r, n);  // Modified to directly calculate x(n)

        fprintf(file, "%d\t%d\t%d\n", n, x_n, y_n);

        sum_x += x_n;
    }

    // Close the file
    fclose(file);

    // Print the sum of the first 6 terms for x(n)
    printf("Sum of the first 6 terms of x(n): %lf\n", sum_x);

    return 0;
}

