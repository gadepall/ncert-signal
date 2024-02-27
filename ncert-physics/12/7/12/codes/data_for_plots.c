#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

// Function to calculate capacitor charge
double capacitor_charge(double q0, double frequency, double time) {
    return q0 * cos(2 * PI * frequency * time);
}

// Function to calculate capacitor current
double capacitor_current(double w, double time ,double capacitance) {
    return -200*sin(w*time);
}
// Function to calculate capacitor voltage
double capacitor_voltage(double w, double time ,double capacitance) {
    return 200*cos(w*time);
}

// Function to calculate capacitor energy
double capacitor_energy(double vol, double capacitance) {
    return 0.5 * capacitance * vol*vol;
}

// Function to calculate inductor energy
double inductor_energy(double vol, double capacitance) {
    return (1- 0.5 * capacitance * vol*vol);
}

int main() {
    // Given values
    double initial_capacitor_charge = 10e-3; // Initial energy across capacitor in joules (10 mC)
    double capacitance = 50e-6; // Capacitance in farads
    double inductance = 100e-3; // Inductance in henrys 

    // Calculate frequency
    double frequency = 1 / (2 * PI * sqrt(inductance * capacitance));
    double ang_freq = 1 / ( sqrt(inductance * capacitance));
    // Time parameters
    double time_start = 0;
    double time_end = 0.03;
    double time_step = 0.0001; // Adjust the time step as needed

    // Open file for writing
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    // Write headers to file
    fprintf(file, "Time(sec)     \tCapacitor Charge(C)   \tCapacitor Voltage(V)   \tCurrent(A)     \tCapacitor Energy(J)       \tInductor Energy(J)\n");

    // Calculate and write values to the file
    for (double time = time_start; time <= time_end; time += time_step) {
        double capacitor_charge_val = capacitor_charge(initial_capacitor_charge, frequency, time);
        double capacitor_current_val = capacitor_current(ang_freq, time,capacitance);
        double capacitor_voltage_val = capacitor_voltage(ang_freq,time, capacitance);
        double capacitor_energy_val = capacitor_energy(capacitor_voltage_val, capacitance);
        double inductor_energy_val = inductor_energy(capacitor_voltage_val, capacitance);

        // Write values to the file
        fprintf(file, "%.4f   \t%12.6f   \t%20.6f   \t%20.6f   \t%21.6f   \t%18.6f\n", time, capacitor_charge_val, capacitor_voltage_val, capacitor_current_val, capacitor_energy_val, inductor_energy_val);
    }

    // Close the file
    fclose(file);

    return 0;
}