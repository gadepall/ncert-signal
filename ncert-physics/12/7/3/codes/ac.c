#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("coordinate.txt", "w");

    // Given values
    double inductance = 44e-3;  // inductance in henries
    double voltage = 220.0;     // voltage in volts
    double frequency = 50.0;    // frequency in hertz
    double omega = 2 * M_PI * frequency;

    // Time array for one cycle (100 points per cycle for a smooth plot)
    for (int i = 0; i < 100; ++i) {
        double t = (double)i / 100.0 / frequency;
        double current = voltage / (omega * inductance) * sin(omega * t);
        fprintf(file, "%.6f %.6f\n", t, current);
    }

    fclose(file);

    return 0;
}

