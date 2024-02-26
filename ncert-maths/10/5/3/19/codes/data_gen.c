#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "n     y(n)\n");

    // Given values
    double y_n;        // Value of y(n)

    // Generate values for n to cover the range from 0 to 15 (inclusive) with a step of 1
    for (int n = 0; n <= 15; n++) {
        // Calculate y(n)
        y_n = (n + 1) * (40 - n) / 2.0;

        // Write to file
        fprintf(file, "%d %lf\n", n, y_n);
    }

    fclose(file);

    return 0;
}
