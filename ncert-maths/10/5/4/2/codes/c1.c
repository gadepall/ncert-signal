#include <stdio.h>

// Function to save values to file recursively
void save_values(int n, int limit, FILE *file3, FILE *file4, FILE *file5, FILE *file6) {
    if (n > limit)
        return;

    double value3 = (n + 2) / 2.0;
    double value4 = n * (n + 3) / 4.0;
    double value5 = (10 - n) / 2.0;
    double value6 = n * (21 - n) / 4.0;

    // Save the calculated values to the files
    fprintf(file3, "%.2f\n", value3);
    fprintf(file4, "%.2f\n", value4);
    fprintf(file5, "%.2f\n", value5);
    fprintf(file6, "%.2f\n", value6);

    // Recursive call for the next value
    save_values(n + 1, limit, file3, file4, file5, file6);
}

int main() {
    // Open files for writing
    FILE *file3 = fopen("py_3.txt", "w");
    FILE *file4 = fopen("py_4.txt", "w");
    FILE *file5 = fopen("py_5.txt", "w");
    FILE *file6 = fopen("py_6.txt", "w");

    if (file3 == NULL || file4 == NULL || file5 == NULL || file6 == NULL) {
        printf("Error opening files.\n");
        return 1;
    }

    // Save values recursively for all expressions
    save_values(0, 15, file3, file4, file5, file6);

    // Close files
    fclose(file3);
    fclose(file4);
    fclose(file5);
    fclose(file6);

    printf("Values saved successfully.\n");

    return 0;
}
