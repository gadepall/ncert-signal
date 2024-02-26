#include <stdio.h>
#include <math.h>

// Define the signal x(n) = (2n + 1)^2 for n = 0 to 5
int signal(int n) {
    return pow(((2 * n) + 1) ,2);
}

// Define the unit step function u(n)
int u(int n) {
    return (n >= 0) ? 1 : 0;
}

void linespace(int start, int stop, int step, int* n, int* x, int* y, int num) {
    for (int i = 0; i < num; ++i) {
       n[i]= start + i * step;
        x[i]= pow((2*n[i] +1),2); 
        y[i]= (4*pow(n[i],3)+12*pow(n[i],2)+11*n[i]+3)/3;
    }
}

int convolution() {
    // Result of convolution
    int y[6] = {0}; // Initialize with zeros
    // Perform convolution
    for (int n = 0; n <=5 ; n++) {
        for (int k = 0; k <= n; k++) {
            y[n] += signal(k) * u(n - k);
        }
    }
    // Print the result
    printf("Result of convolution:\n");
    for (int i = 0; i <= 5; i++) {
        printf("y[%d] = %.2d\n", i, y[i]);
    }
    return y[5];
}

int main() {
    // Define the range and step size
    int start = 0;
    int stop = 10;
    int step = 1;

    // Calculate the number of values in the range
    int num = (stop - start) / step + 1;

    // Allocate arrays to store the generated values
    int n[num];
    int x[num];
    int y[num];

    // Call the linespace function
    linespace(start, stop, step, n, x,y, num);

    // Save data to a file
    FILE* file = fopen("output.dat", "w");
    
    int u_n = num >= 0 ? 1 : 0;
    int u_n_minus_1 = (num - 1) >= 0 ? 1 : 0;
    int u_n_minus_2 = (num - 2) >= 0 ? 1 : 0;
    int u_n_minus_3 = (num - 3) >= 0 ? 1 : 0;
    int u_n_minus_4 = (num - 4) >= 0 ? 1 : 0;
    
    // Calculate values for-->simulation
        int Simulation = u_n + 9*u_n_minus_1 + 25*(num-1)*u_n_minus_2 + 12*(num-1)*(num-2)*u_n_minus_3 + 8*(num-1)*(num-2)*(num-3)*u_n_minus_4/6;

       

    if (file != NULL) {
        for (int i = 0; i < num; ++i) {
         
    // Calculate values for-->simulation
        int Simulation = u_n + 9*u_n_minus_1 + 25*(i-1)*u_n_minus_2 + 12*(i-1)*(i-2)*u_n_minus_3 + 8*(i-1)*(i-2)*(i-3)*u_n_minus_4/6;

            fprintf(file, "%d %d %d %d\n", n[i], x[i], y[i], Simulation);
        }

        fclose(file);
        printf("Data saved to 'output.dat'.\n");
    } else {
        printf("Error opening file for writing.\n");
    }
    
    file = fopen("output.dat", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    int n1=5;
    double  y_n = (4*pow(n1,3)+12*pow(n1,2)+11*n1+3)/3 ;
    printf("y(%d) according to the formula : %lf\n", n1, y_n);
    int sum = convolution();
    printf("The value of y(5) using convolution is: %d\n",sum); 
    if(y_n == sum)
    {
    	printf("y(5) using convolution and formula are same.\n");
    }
    else
    printf("Error!!!\n");

    return 0;
}
