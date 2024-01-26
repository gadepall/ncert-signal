#include <stdio.h>
#include <math.h>

// Function to generate linearly spaced values
void linspace(double start, double end, int num, double *result) {
    double step = (end - start) / (num - 1);
    for (int i = 0; i < num; i++) {
        result[i] = start + i * step;
    }
}

int main() {
    // Open a file for writing
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    double a = -2.0 / 7.0;
    int num_points = 10;

    // Create an array to store n_values
    double n_values[num_points];
    linspace(0, 9, num_points, n_values);

    // Generate data and write to the file
    for (int i = 0; i < num_points; i++) {
        double y1 = a * pow(-7.0 / 2.0, n_values[i]);
        double y2 = a * pow(7.0 / 2.0, n_values[i]);
        fprintf(file, "%f %f %f\n", n_values[i], y1, y2);
    }

    fclose(file);
    return 0;
}

