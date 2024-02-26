#include <stdio.h>

int main() {
    int n;
    double x[5];  // To store the first five terms of the sequence

    // Calculate the values for n >= 0
    for (n = 0; n < 5; n++) {       
            x[n] = (double)(n+1) / (n + 2);     
    }

    // Open a file for writing
    FILE *file = fopen("sequence.txt", "w");

    // Check if the file opened successfully
    if (file != NULL) {
        // Write the sequence to the file
        for (n = 0; n < 5; n++) {
            fprintf(file, "%.2f\n", x[n]);
        }

        // Close the file
        fclose(file);

        printf("Sequence has been written to sequence.txt\n");
    } else {
        printf("Error opening the file.\n");
    }

    return 0;
}
