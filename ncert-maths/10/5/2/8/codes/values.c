#include <stdio.h>

int main() {
    FILE *file = fopen("values.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    fprintf(file, "Values for stem plot of x_1(n):\n");

    for (int i = 0; i < 31; i++)
     {
        int n = i;
        float x_1 = (float)(8 + 2 * n);
        fprintf(file, "%d %.2f\n", n, x_1);
    }
    }
