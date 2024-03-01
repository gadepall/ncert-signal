#include <stdio.h>
#include <math.h>

// Value of x(0)
#define X_0 (16.0 / 7.0)

// Function to calculate x(n)
double x_n(int n) {
    return X_0 * pow(2, n);
}

int main() {
    FILE *file = fopen("datax.dat", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and write x(n) values to the file
    for (int n = 0; n < 10; n++) {  // Adjust the range as needed
        double x = x_n(n);
        fprintf(file, "%d %f\n", n, x);
    }

    fclose(file);
    printf("Data has been saved to datax.dat.\n");
    return 0;
}

