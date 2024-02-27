#ifndef MYLIB_H
#define MYLIB_H
void linspace(float start, float stop, float step, float* x_values, float* y_values, int num_values, float(*func)(float)) ;
void save(int x, float* x_values, float* y_values) ;
void app(int x, float* x_values, float* y_values) ;
#endif
