#include <stdio.h>
#include <math.h>

// Generates a sequence of values and corresponding y values based on an arithmetic progression formula.
void linespace(int start, int stop, int step, int* n_values, int* y_values, int num_values) {
  // Loop through each index to generate values and calculate y values.
    for (int i = 0; i < num_values; ++i) {
        n_values[i] = start + i * step;
        int sum = (n_values[i]+1) * (240+ (n_values[i]) *5) / 2;
        y_values[i] = sum;
    } 
}

void solveQuadratic(double a, double b, double c) {
    double discriminant, root1, root2;

    // Calculate discriminant
    discriminant = b * b - 4 * a * c;

    // Check if roots are real or complex
    if (discriminant > 0) {
        // Real roots
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);

        printf("Roots are real and different.\n");
        printf("Root 1 = %.2f\n", root1);
        printf("Root 2 = %.2f\n", root2);
    } else if (discriminant == 0) {
        // Real and equal roots
        root1 = -b / (2 * a);

        printf("Roots are real and equal.\n");
        printf("Root 1 = Root 2 = %.2f\n", root1);
    } else {
        // Complex roots
        double realPart = -b / (2 * a);
        double imaginaryPart = sqrt(-discriminant) / (2 * a);

        printf("Roots are complex and different.\n");
        printf("Root 1 = %.2f + %.2fi\n", realPart, imaginaryPart);
        printf("Root 2 = %.2f - %.2fi\n", realPart, imaginaryPart);
    }
}

int main() {
    // Define the range and step size
    int start = 0;
    int stop = 9;
    int step = 1;

    // Calculate the number of values in the range
    int num_values = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    int n_values[num_values];
    int y_values[num_values];

    // Call the linespace function
    linespace(start, stop, step, n_values, y_values, num_values);

    // Save data to a file
    FILE* file = fopen("output.dat", "w");

    if (file != NULL) {
        for (int i = 0; i < num_values; ++i) {
            fprintf(file, "%d %d\n", n_values[i], y_values[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }

	double a=5, b=-125, c=720;

    // Call the function to solve the quadratic equation
    solveQuadratic(a, b, c);

    return 0;
  
}

