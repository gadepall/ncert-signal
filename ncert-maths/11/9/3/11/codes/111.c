#include <stdio.h>
#include <math.h>  // Include math.h for pow function

int main() {
    FILE *file = fopen("values_y.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    fprintf(file, "Values for stem plot of y(n) = 2(n+1) + {3(3^(n+1)-1)}/2:\n");

    for (int i = 0; i < 11; i++) {
        int n = i;
        float y = 2 * (n + 1) + (3 * (pow(3, n + 1) - 1)) / 2.0;

        fprintf(file, "%d %.2f\n", n, y);
    }

    fclose(file);  // Close the file

    return 0;
}

