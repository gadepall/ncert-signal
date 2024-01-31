#include <stdio.h>

int main() {
    FILE *file = fopen("output.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    for (int i = 0; i < 10; i++) {
        int x = i;
        float y =25-3*x;
        fprintf(file, "%d %.2f\n", x, y);
    }

    fclose(file);  // Close the file

    return 0;
}
