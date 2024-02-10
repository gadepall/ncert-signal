#include<stdio.h>
#include<math.h>

int main(){
    FILE *ptr;
    ptr= fopen("series.dat", "w");
    float x_0=1.0;
    float r= 1.2;
    for(int i=0; i<17; i++){
        fprintf(ptr, "%f ", x_0*pow(r,i));
    }
    fprintf(ptr, "\b ");
    return 0;
}