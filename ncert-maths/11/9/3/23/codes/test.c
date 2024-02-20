#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("output.dat", "w");  // Open file for writing

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;  // Return an error code
    }

    // Calculate and write values to the file
    for (int n = 1; n <= 10; ++n) {  // Adjust the range as needed
        double result = 5*pow(2, n - 1);
        fprintf(file, "%d %lf\n", n, result);
    }

    fclose(file);  // Close the file

    printf("Values written to output.dat.\n");

    return 0;  // Return success code
}