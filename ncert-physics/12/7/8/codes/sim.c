#include <stdio.h>
#include <math.h>

#define CAPACITOR_VALUE 30e-6  // Capacitance in Farads
#define INDUCTOR_VALUE 30e-3    // Inductance in Henrys
#define INITIAL_CHARGE 6e-3     // Initial charge in Coulombs
#define TIME_STEP 1e-6          // Time step for simulation in seconds
#define SIMULATION_TIME 0.000005   // Total simulation time in seconds

void simulateLCircuit() {
    double voltage = 0.0;      // Voltage across the capacitor
    double current = 0.0;      // Current through the inductor
    double charge = INITIAL_CHARGE;  // Charge on the capacitor
    double totalEnergy = 0.0;  // Total energy in the circuit

    printf("Time(s)   Voltage(V)   Current(A)   Charge(C)   Energy_C(J)   Energy_L(J)   Total Energy(J)\n");

    for (double time = 0; time <= SIMULATION_TIME; time += TIME_STEP) {
        // Update voltage, current, and charge using numerical integration (Euler's method)
        voltage = charge / CAPACITOR_VALUE;
        current = voltage / INDUCTOR_VALUE;
        charge += current * TIME_STEP;

        // Calculate energy in the capacitor and inductor
        double energyC = 0.5 * CAPACITOR_VALUE * voltage * voltage;
        double energyL = 0.5 * INDUCTOR_VALUE * current * current;

        // Calculate total energy
        totalEnergy = energyC + energyL;

        // Print simulation results
        printf("%.6f   %.6f   %.6f   %.6f   %.6f   %.6f   %.6f\n", time, voltage, current, charge, energyC, energyL, totalEnergy);
    }
}

int main() {
    simulateLCircuit();

    return 0;
}

