#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "n     x(n)      y(n)\n");

    // Generate values for n to cover the range from -10 to 10 (inclusive) with a step of 1
    for (int n = 0; n <= 20; n++) {
        // Calculate values for-->theory
        int Theory = 150 - 4 * n;

        // Calculate values for-->simulation
        int Simulation = 150 - 4 * n;

        // Write to file
        fprintf(file, "%d     %d       %d\n", n, Theory, Simulation);
    }

    fclose(file);

    return 0;
}

