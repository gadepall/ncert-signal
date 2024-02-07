#include <stdio.h>
#include<math.h>

// Define the function
double expression(int n) {
    return ((n * n * (n + 1) * (n + 1) / 4.0) + (5.0 * n * (n + 1) * (2 * n + 1) / 6.0) + (4.0 * n * (n + 1) / 2.0)) * (n >= 0);
}

int main() {
    // Define the range of n values (e.g., from 1 to 10)
    int start_n = -5;
    int end_n = 10;

    // Open the .dat file for writing
    FILE *file = fopen("data3.dat", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Generate and store x_values and y_values in the .dat file
    for (int n = start_n; n <= end_n; ++n) {
        double y_value = expression(n);
        fprintf(file, "%d\t%lf\n", n, fabs(y_value));
    }

    // Close the file
    fclose(file);

    return 0;
}

