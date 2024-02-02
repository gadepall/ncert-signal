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
    for (int n = -10; n <= 10; n++) {
        // Calculate values for-->theory
        int u_n = n >= 0 ? 1 : 0;
        int u_n_minus_1 = (n - 1) >= 0 ? 1 : 0;
        int u_n_minus_2 = (n - 2) >= 0 ? 1 : 0;
        int Theory = 2 * u_n + (1 - n) * u_n_minus_1;

        // Calculate values for-->simulation
        int Simulation = 2 * u_n_minus_1 + (2 - n) * u_n_minus_2 + 2 * u_n - 2 * u_n_minus_1 - u_n_minus_2;

        // Write to file
        fprintf(file, "%d     %d       %d\n", n, Theory, Simulation);
    }

    fclose(file);

    return 0;
}
