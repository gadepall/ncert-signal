#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double trapezoidal_integration(double x[], double y[], int n) {
    double area = 0.0;
    for (int i = 1; i < n; ++i) {
        area += 0.5 * (x[i] - x[i - 1]) * (y[i] + y[i - 1]);
    }
    return area;
}

int main() {
    // Constants
    double R = 1.0;       // Resistance in ohms

    // Time parameters
    double t_start = 0;
    double t_end = 3e-3;
    int num_points = 1000;

    // Allocate memory for time, current, and power arrays
    double *time = malloc(num_points * sizeof(double));
    double *current = malloc(num_points * sizeof(double));
    double *power = malloc(num_points * sizeof(double));

    // Calculate time, current, and power
    for (int i = 0; i < num_points; ++i) {
        time[i] = t_start + i * (t_end - t_start) / (num_points - 1);

        // Calculate current I(t)
        current[i] = -(400 / sqrt(3)) * exp(-10000 * time[i]) * sin(10000 * sqrt(3) * time[i]);

        // Calculate power P(t) = i(t)^2 * R
        power[i] = pow(current[i], 2) * R;
    }

    // Calculate area using trapezoidal rule for power
    double area_under_power_curve = trapezoidal_integration(time, power, num_points);

    // Print the area to the terminal for verification
    printf("Area under the power curve: %.6lf Joules\n", area_under_power_curve);

    FILE *output_file = fopen("data_for_damping.txt", "w");
    if (output_file == NULL) {
        fprintf(stderr, "Error opening output file.\n");
        return 1;
    }

    // Append the calculated data to the file
    fprintf(output_file, "Time(s)\tCurrent(A)\tPower(W)\n");
    for (int i = 0; i < num_points; ++i) {
        fprintf(output_file, "%.6lf   %.6lf   %.6lf\n", time[i], current[i], power[i]);
    }

    fclose(output_file);

    // Free allocated memory
    free(time);
    free(current);
    free(power);

    return 0;
}
