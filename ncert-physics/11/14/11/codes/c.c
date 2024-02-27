#include <stdio.h>
#include <math.h>
#include "mylib.h"
float f(float x){
return -3 * (sin(M_PI * x));
}
float q(float x){
return -2 * (cos(M_PI/2 * x));
}
int main() {
    // Define the range and step size
    float start = 0;
    float stop = 4;
    float step = 0.01;

    // Calculate the number of values in the range
    int num_values = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    float x_values[num_values];
    float y_values[num_values];
	float(*func)(float);
	func = f;
    // Call the linspace function
    linspace(start, stop, step, x_values, y_values, num_values, func);
    //Call save function
    save(num_values, x_values, y_values);
    func = q;
    // Call the linspace function
    linspace(start, stop, step, x_values, y_values, num_values, func);
    //Call save function
    app(num_values, x_values, y_values);
    }
