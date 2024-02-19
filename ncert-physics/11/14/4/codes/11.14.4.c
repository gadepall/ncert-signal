#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

void saveData(FILE *file, double omega, double t_start, double t_end, double t_step, double (*function)(double, double)) {
    for (double t = t_start; t <= t_end; t += t_step) {
        fprintf(file, "%lf %lf\n", t, function(omega, t));
    }
}

double function1(double omega, double t) {
    return sin(omega * t) - cos(omega * t);
}

double function2(double omega, double t) {
    return pow(sin(omega * t), 3);
}

double function3(double omega, double t) {
    return 3 * cos(PI/4 - 2 * omega * t);
}

double function4(double omega, double t) {
    return cos(omega * t) + cos(3 * omega * t) + cos(5 * omega * t);
}

double function5(double omega, double t) {
    return exp(-pow(omega * t, 2));
}

double function6(double omega, double t) {
    return 1 + omega * t + pow(omega * t, 2);
}

int main() {
    double omega = 1.0; // You can adjust the value of omega
    double t_start = 0.0;
    double t_end = 10.0;
    double t_step = 0.1;

    FILE *file1 = fopen("function1_data.txt", "w");
    FILE *file2 = fopen("function2_data.txt", "w");
    FILE *file3 = fopen("function3_data.txt", "w");
    FILE *file4 = fopen("function4_data.txt", "w");
    FILE *file5 = fopen("function5_data.txt", "w");
    FILE *file6 = fopen("function6_data.txt", "w");

    if (file1 == NULL || file2 == NULL || file3 == NULL || file4 == NULL || file5 == NULL || file6 == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    saveData(file1, omega, t_start, t_end, t_step, function1);
    saveData(file2, omega, t_start, t_end, t_step, function2);
    saveData(file3, omega, t_start, t_end, t_step, function3);
    saveData(file4, omega, t_start, t_end, t_step, function4);
    saveData(file5, omega, t_start, t_end, t_step, function5);
    saveData(file6, omega, t_start, t_end, t_step, function6);

    fclose(file1);
    fclose(file2);
    fclose(file3);
    fclose(file4);
    fclose(file5);
    fclose(file6);

    return 0;
}




