#include <stdio.h>
#include <math.h>

double pow(double base, double exponent) 
{
    double result = 1.0;
    while (exponent != 0) {
        result *= base;
        --exponent;
    }
    return result;
}
int main() {
    FILE *file;
    file = fopen("coordinates.txt", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
     double n=8; // Number of terms

    // Geometric progression parameters
   
    double firstTerm = -3.0;
    double commonRatio = -3.0;

    // Generating and saving coordinates
    for (double i = 0; i < n; ++i) {
        double x = i ;
        double y = firstTerm * pow(commonRatio, i);

        fprintf(file, "%.2f %.2f\n", x, y);
    }

    fclose(file);
    printf("Coordinates saved in coordinates.txt.\n");

    return 0;
}

