#include <stdio.h>

// Function to generate an array of equally spaced values
void linspace(double start, double end, int num, double *result) {
    double step = (end - start) / (num - 1);

    for (int i = 0; i < num; i++) {
        result[i] = start + i * step;
    }
}

int main() {
    // Define the range
    double start_x = -2.0;
    double end_x = 12.0;
    int num_points = 100;  // Adjust this based on the desired number of points

    // Allocate an array to store the values of x
    double x_values[num_points];

    // Generate equally spaced values using linspace
    linspace(start_x, end_x, num_points, x_values);

    // Calculate the values of y and write to the file
    FILE *file = fopen("data.txt", "w");

    if (file != NULL) {
        for (int i = 0; i < num_points; i++) {
            double x = x_values[i];
            double y = (2 * x - 3) / 6;

            // Write x and y to the file
            fprintf(file, "%lf %lf\n", x, y);
        }

        // Close the file
        fclose(file);
    } else {
        printf("Error opening the file.\n");
    }

    return 0;
}

