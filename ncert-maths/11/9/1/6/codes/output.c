#include <stdio.h>

int main() {
    FILE *file = fopen("output.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    for (int i = 0; i < 11; i++) {
        int x = i;
        float y = (float)((x + 1) * (x + 1) * (x + 1) + 5 * (x + 1)) / 4;
        fprintf(file, "%d %.2f\n", x, y);
    }

    fclose(file);  // Close the file

    return 0;
}

