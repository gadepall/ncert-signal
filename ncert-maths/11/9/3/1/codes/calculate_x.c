// calculate_x.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    // Generate values for n from -3 to 6
    int n_values[] = {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6};
    int num_values = sizeof(n_values) / sizeof(n_values[0]);

    // Open a file for writing
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Calculate x(n) for each n and write the values to the file
    for (int i = 0; i < num_values; i++) {
        double x_n = (5.0 / 2) * pow(0.5, n_values[i]) * (n_values[i] >= 0);  // Multiply by the unit step function
        fprintf(file, "%d\t %lf\n", n_values[i], x_n);
    }

    // Close the file
    fclose(file);

    return 0;
}
