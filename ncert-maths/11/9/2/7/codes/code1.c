#include <stdio.h>

int main() {
    // Writing to "simulation.dat" file
    FILE *simulationFile = fopen("simulation.dat", "w");
    if (simulationFile == NULL) {
        printf("Error opening the simulation.dat file.\n");
        return 1;  // Return an error code
    }

    for (int i = 0; i < 10; i++) {
        int x = i;
        float y = i + 2 + 2.5 * i * (i +1);
        fprintf(simulationFile, "%d %.2f\n", x, y);
    }

    fclose(simulationFile);  // Close the file

    // Writing to "theory.dat" file
    FILE *theoryFile = fopen("theory.dat", "w");
    if (theoryFile == NULL) {
        printf("Error opening the theory.dat file.\n");
        return 1;  // Return an error code
    }

    for (int i = 0; i < 10; i++) {
        int x = i;
        float y = i * (3.5 + 2.5 * i);
        fprintf(theoryFile, "%d %.2f\n", x, y);
    }

    fclose(theoryFile);  // Close the file

    return 0;
}

