#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

int main() {
    FILE *fp;
    fp = fopen("values.txt", "w");
    
    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    double amplitude = 2.2 * sqrt(2.0);
    double frequency = 100.0 * PI;
    double period = 0.1; // Increased period to accommodate two full cycles
    
   
    
    for (double t = 0.0; t <= period; t += 0.0001) { // Adjusting the time axis
        double value = amplitude * sin(frequency * t);
        
        fprintf(fp, "%lf\n", value);
    }
    
    fclose(fp);
    return 0;
}

