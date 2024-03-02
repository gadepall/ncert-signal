#include <stdio.h>
#include <math.h>

// Function to calculate y(n)
double y_n(int n, double x_0, double r) {
    return x_0 * ((pow(r, n) - 1) / (r - 1));
}

int main() {
    double x_0 = 16.0 / 7.0;  // Value of x(0)
    double r = 2.0;           // Value of r

    FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and write y(n) values to the file
    for (int n = 0; n < 10; n++) {  // Adjust the range as needed
        double y = y_n(n, x_0, r);
        fprintf(file, "%d %f\n", n, y);
    }

    fclose(file);
    return 0;
}

