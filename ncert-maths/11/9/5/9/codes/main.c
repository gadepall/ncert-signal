#include <stdio.h>

// Function to generate terms of the geometric progression and store in a file
void generate_GP_and_store(int initial_term, int common_ratio, int num_terms, const char* filename, int table_number) {
    FILE *fp;
    fp = fopen(filename, "a"); // Open file in append mode
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    // Generate terms of the geometric progression
    int term = initial_term;
    fprintf(fp, "n\tTerm\n");
    for (int i = 0; i < num_terms; i++) {
        fprintf(fp, "%d\t%d\n", i, term); // Modify here to start with zero-indexing
        term *= common_ratio;
    }

    fclose(fp);
}

int main() {
    int initial_term = 1; // Modify initial term here
    int num_terms = 6;  // Number of terms to generate
    const char* filename1 = "gp_data1.txt";
    const char* filename2 = "gp_data2.txt";

    // Generate table for r = 3 and store in file1
    generate_GP_and_store(initial_term, 3, num_terms, filename1, 1);

    // Generate table for r = -3 and store in file2
    generate_GP_and_store(initial_term, -3, num_terms, filename2, 2);

    printf("Data generated and stored in %s and %s\n", filename1, filename2);

    return 0;
}

