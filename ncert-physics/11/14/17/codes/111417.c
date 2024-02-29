#include <stdio.h>
#include <math.h>
#include "ee1205.h"

// Length of pendulum
const double l = 1;
// Radius of track
const double R = 1;
// Velocity of car
const double v = 1;
// Acceleration due to gravity
const double g = 9.81;

double theta(double t) {
    double k = sqrt(1/l * sqrt(pow(pow(v, 2) / R, 2) + pow(g, 2)));
    return sin(k * t) / k;
}

int main () {
    // Generate x-axis.
    double* t = linspace(0, 10, 10000);

    // Open output file.
    FILE* out;
    fopen_s(&out, "111417cout.txt", "w");

    // Write output to file.
    for (size_t i = 0; i < 10000; i++) fprintf(out, "%lf ", theta(t[i]));

    // Close file and free memory allocated for x-axis.
    fclose(out);
    free(t);

    return 0;
}