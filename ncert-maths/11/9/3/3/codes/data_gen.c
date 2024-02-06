#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "n     x(n)\n");

    // Given values
    double x_0 = 2.0; // Replace with your desired value
    double r = 3.0;   // Replace with your desired value

    // Generate values for n to cover the range from 0 to 10 (inclusive) with a step of 1
    for (int n = 0; n <= 11; n++) {
        // Calculate and write to file
        fprintf(file, "%d %lf\n", n, (n >= 0) ? x_0 * pow(r, n) : 0.0);
    }

    fclose(file);

    return 0;
} 
