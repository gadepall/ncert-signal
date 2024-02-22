#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Iterate over values of n from 0 to 4
    for (int n = 0; n <= 4; ++n) {
        double term = pow(-1, n ) * pow(5, n + 2);
        fprintf(file, "%d %.2f\n", n, term);
    }

    fclose(file);
    printf("Values saved to 'values.dat' successfully.\n");
    return 0;
}

