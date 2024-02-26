#include <stdio.h>

// Function to generate AP terms
void generate_ap(int start, int end, int common_difference, FILE *file) {
    int current_term = start;
    while (current_term <= end) {
        fprintf(file, "%d\n", current_term);
        current_term += common_difference;
    }
}

int main() {
    // Open a file for writing
    FILE *file = fopen("values.dat", "w");

    // Check if the file was opened successfully
    if (file == NULL) {
        perror("Error opening file");
        return 1; // Exit with an error code
    }

    // Generate AP terms and write to the file
    int start_term = 105;
    int end_term = 994;
    int common_difference = 7;
    generate_ap(start_term, end_term, common_difference, file);

    // Close the file
    fclose(file);

    printf("Values written to values.dat.\n");

    return 0; // Exit successfully
}

