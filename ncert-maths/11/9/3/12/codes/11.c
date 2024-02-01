#include <stdio.h>
#include <float.h>

int main() {
    FILE *file = fopen("11.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Parameters for the first GP
    double first_term_1 = 5.0 / 2.0;
    double common_ratio_1 = 2.0 / 5.0;

    // Parameters for the second GP
    double first_term_2 = 2.0 / 5.0;
    double common_ratio_2 = 5.0 / 2.0;

    // Number of terms
    int n_terms = 20;

    // Write the values for both GPs to the file in two columns with integers on the x-axis
    for (int i = 1; i <= n_terms; ++i) {
        fprintf(file, "%d\t%e\t%e\n", i, first_term_1, first_term_2);
        first_term_1 *= common_ratio_1;
        first_term_2 *= common_ratio_2;
    }
    
    // Close the file
    fclose(file);

    // Read the values from the file and calculate the sum and product of the first three terms
    file = fopen("11.dat", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double sum_1 = 0, sum_2 = 0;
    double product_1 = 1, product_2 = 1;

    for (int i = 0; i < 3; ++i) {
        int index;
        double term_1, term_2;
        fscanf(file, "%d %lf %lf", &index, &term_1, &term_2);

        sum_1 += term_1;
        sum_2 += term_2;
        product_1 *= term_1;
        product_2 *= term_2;
    }

    // Close the file
    fclose(file);

    // Print the results
    printf("Sum of the first three terms for sequence 1: %e\n", sum_1);
    printf("Product of the first three terms for sequence 1: %e\n", product_1);
    printf("Sum of the first three terms for sequence 2: %e\n", sum_2);
    printf("Product of the first three terms for sequence 2: %e\n", product_2);

    return 0;
}

