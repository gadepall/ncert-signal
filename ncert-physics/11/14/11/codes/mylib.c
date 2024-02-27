#include "mylib.h"
#include <stdio.h>
#include <math.h>
void linspace(float start, float stop, float step, float* x_values, float* y_values, int num_values, float(*func)(float)){
for(int i = 0; i<num_values; ++i){
 x_values[i] = start + i * step;
 y_values[i] = func(x_values[i]);
}}
void save(int x, float* x_values, float* y_values){
//Save data to a file
     FILE* file = fopen("output.dat", "w");

    if (file != NULL) {
        for (int i = 0; i < x; ++i) {
            fprintf(file, "%f %f\n", x_values[i], y_values[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }
}
void app(int x, float* x_values, float* y_values){
//Save data to a file
     FILE* file = fopen("output.dat", "a");

    if (file != NULL) {
        for (int i = 0; i < x; ++i) {
            fprintf(file, "%f %f\n", x_values[i], y_values[i]);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }
}
