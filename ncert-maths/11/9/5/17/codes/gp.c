#include <stdio.h>

double calculate_identity_term(double base, int exponent) {
    double result = 1.0;

    for (int i = 0; i < exponent; i++) {
        result *= base;
    }

    return result;
}

void calculate_and_save_sequence(FILE *file, double a, double b, double c, double d, int n) {
    double x_n = a;

    for (int i = 0; i <= n; i++) {
        fprintf(file, "%d %lf\n", i, x_n);
        x_n *= 2.0; // Equivalent to pow(2, i)
    }
}

int verify_identity(double a, double b, double c, double d, int n) {
    for (int i = 0; i <= n; i++) {
        double numerator1 = calculate_identity_term(b, i) + calculate_identity_term(c, i);
        double denominator1 = calculate_identity_term(a, i) + calculate_identity_term(b, i);

        double numerator2 = calculate_identity_term(c, i) + calculate_identity_term(d, i);
        double denominator2 = calculate_identity_term(b, i) + calculate_identity_term(c, i);

        double left_side = numerator1 / denominator1;
        double right_side = numerator2 / denominator2;

        if ((left_side - right_side > 1e-9) || (right_side - left_side > 1e-9)) {
            printf("Identity verification failed for n = %d\n", i);
            return 1;  // Identity verification failed
        }
    }

    printf("Identity verified for all values up to n = %d\n", n);
    return 0;
}

int main() {
    FILE *file1 = fopen("coordinate1.txt", "w");
    FILE *file2 = fopen("coordinate2.txt", "w");

    if (file1 == NULL || file2 == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    double a = 0.25, b = 0.5, c = 1, d = 2;

    // Calculate and save sequence for x(n) = a * 2^n
    calculate_and_save_sequence(file1, a, b, c, d, 10);

    // Verify the identity for the given sequence
    int verification_result = verify_identity(a, b, c, d, 10);

    // Generate data for x(n) = 0.25^n + 0.5^n
    for (int n = 0; n < 5; ++n) {
        double x_n = calculate_identity_term(0.25, n) + calculate_identity_term(0.5, n);
        fprintf(file2, "%.4f\n", x_n);
    }

    fclose(file1);
    fclose(file2);

    return verification_result;
}
