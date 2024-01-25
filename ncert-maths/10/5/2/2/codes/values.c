#include <stdio.h>

int main() {
    FILE *file = fopen("values.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    fprintf(file, "Values for stem plot of x_1(n):\n");

    for (int i = 0; i < 33; i++) {
        int n = i;
        float x_1 = (float)(10 - 3 * n);
        fprintf(file, "%d %.2f\n", n, x_1);
    }

    fprintf(file, "\nValues for stem plot of x_2(n):\n");  // Add a newline and heading

    for (int i = 0; i < 21; i++) {
        int n = i;
        float x_2 = (float)(-3 + 2.5 * n);
        fprintf(file, "%d %.2f\n", n, x_2);
    }

    fclose(file);  // Close the file

    return 0;
}

