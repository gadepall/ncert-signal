#include <stdio.h>

int main() {
    int n;
    int x[5];  // To store the first five terms of the sequence

    // Initialize the first term
    x[0] = 3;

    // Calculate the next four terms using the recurrence relation
    for (n = 1; n < 6; n++) {
        x[n] = 3 * x[n - 1] + 2;
    }

    // Open a file for writing
    FILE *file = fopen("sequence.txt", "w");

    // Check if the file opened successfully
    if (file != NULL) {
        // Write the sequence to the file
        for (n = 0; n < 6; n++) {
            fprintf(file, "%d\n", x[n]);
        }

        // Close the file
        fclose(file);

        printf("Sequence has been written to sequence.txt\n");
    } else {
        printf("Error opening the file.\n");
    }

    return 0;
}

