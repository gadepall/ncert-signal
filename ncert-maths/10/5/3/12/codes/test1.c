#include <stdio.h>

int main() {
    // Define the function
    int n_values[50];
    float y_values[50];

    // Generate data points
    for (int i = 0; i < 50; ++i) {
        n_values[i] = i;
        y_values[i] = 3 * i * i + 6 * i + 3 * i + 6;
    }

    // Open the file for writing
    FILE *file = fopen("output.dat", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1; // Return with an error code
    }

    // Print n and y values to the file
    for (int i = 0; i < 50; ++i) {
        fprintf(file, "%d %.2f\n", n_values[i], y_values[i]);
    }

    // Close the file
    fclose(file);

    return 0; // Return with success code
}