#include<stdio.h>
#include<math.h>
#include<stdlib.h>

float gp(float a,int r,int n){
return a * pow(r,n);
}

int main()
{
    FILE *fp;
    fp  = fopen("data.txt", "w");
    float a = 1.5;
    int r = 2;
    float b;
    int n = 12;
    for(int i = 0; i<=n; i++){
        if(i != n){
            b = gp(a,r,i);
        fprintf(fp,"%.1f ", b);
        }
        else{
            b = gp(a,r,i);
        fprintf(fp,"%.1f", b);
        } 
    
    }
}
