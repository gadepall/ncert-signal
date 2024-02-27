#include <stdio.h>

int main() {
    FILE *file = fopen("values.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    fprintf(file, "Values for stem plot of x_1(n), x_2(n), x_3(n), x_4(n), x_5(n):\n");

    for (int i = 0; i < 33; i++) {
        int n = i;
        float x_1 = (float)(7 + 3 * n);
        float x_2 = (float)(-18 + 2 * n);
        float x_3 = (float)(15 - 3 * n);
        float x_4 = (float)(18.9 + 2.5 * n);
        float x_5 = 3.5;
        
        fprintf(file, "%d %.2f %.2f %.2f %.2f %.2f\n", n, x_1, x_2, x_3, x_4, x_5);
    }

    fclose(file);  // Close the file

    return 0;
}

