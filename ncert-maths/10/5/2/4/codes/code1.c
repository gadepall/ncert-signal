#include <stdio.h>

int main() {
    // Define parameters for the arithmetic progression
    int initial_term = 3;           // Initial term of the arithmetic progression
    int common_difference = 5;      // Common difference between consecutive terms

    // Generate values for n and corresponding x(n)
    int n_values[20];               // Array to store values of n
    int x_n_values[20];             // Array to store corresponding values of x(n)

    // Generate values starting from n = 0
    for (int i = 0; i < 20; i++) {
        n_values[i] = i;            // Assigning current value of i as n
        x_n_values[i] = initial_term + i * common_difference;  // Calculate x(n) using the formula
    }

    // Save the values in a .dat file
    FILE *file = fopen("AP.dat", "w");   // Open a file named "AP.dat" in write mode
    if (file == NULL) {                   // Check if file opening was successful
        fprintf(stderr, "Error opening file for writing.\n");  // Print error message to stderr
        return 1;                          // Return 1 to indicate failure
    }

    // Write the values to the file
    for (int i = 0; i < 20; i++) {
        fprintf(file, "%d %d\n", n_values[i], x_n_values[i]);  // Write n and x(n) values to file
    }

    // Close the file
    fclose(file);   // Close the file stream

    return 0;   // Return 0 to indicate successful execution
}

