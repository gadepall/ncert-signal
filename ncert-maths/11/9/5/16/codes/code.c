#include <stdio.h>
#include <math.h>

void linespace(int start, int stop, int step, int* n_values, double* x_values, int num_values) {
    for (int i = 0; i < num_values; ++i) {
        n_values[i] = start + i * step;
        //corresponding values of x(0) = 36.0/35 and d_x = 82.0/105
        x_values[i] = 36.0/35 + n_values[i]*82.0/105;
    }
}

int main() {
    // Define the range and step size
    int start = 0;
    int stop = 5;
    int step = 1;

    // Calculate the number of values in the range
    int num_values = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    int n_values[num_values];
    double x_values[num_values];

    // Call the linespace function
    linespace(start, stop, step, n_values, x_values, num_values);

    // Save data to a file
    FILE* file = fopen("output.dat", "w");

    if (file != NULL) {
        for (int i = 0; i < num_values; ++i) {
            fprintf(file, "%d %.2lf\n", n_values[i], x_values[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }

    return 0;
}

