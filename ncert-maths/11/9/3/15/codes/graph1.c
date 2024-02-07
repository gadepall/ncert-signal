#include <stdio.h>
#include<math.h>
float y(int n); //recursive function to calculate the sum of GP : y(n) = sum of first (n+1) terms of the GP 

float a = 729;    //first term of the GP

float r = 2.0 / 3.0 ;  //common ratio of thr GP

int main() {
    FILE *file = fopen("values.dat", "w"); //open values.dat to print the data in it
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int n ; // term number 
    float x ; // stores the term x(n) of the GP in the loop 
    
    for(n=0;n<=21;n++)
    {
        x = a*(pow(r,n));
        fprintf(file ,"%d \t %e \t %e\n",n , x , y(n)); //print n,x(n), y(n)
    }
    fclose(file);     //close the file after printing the output
    return 0;
}
float y(int n)
{
    if(n==0)
        return a; //return first term for y(0)
    else
        return y(n-1) + (float)pow(r,n)*(a);  //sum of n terms  = sum of n-1 terms + nth term
}
