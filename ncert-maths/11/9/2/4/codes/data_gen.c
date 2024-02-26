#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("output.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "n     y(n)\n");

    // Given values
    double y_n;        // Value of y(n)

    // Generate values for n to cover the range from 0 to 20(inclusive) with a step of 1
    for (int n = 0; n <= 20; n++) {
        // Calculate y(n)
        y_n =  0.25*pow( n , 2)-5.75*n-6 ;

        // Write to file
        fprintf(file, "%d %lf\n", n, y_n);
    }

    fclose(file);

    return 0;
}
