#include<stdio.h>
int terms(int a, int d, int n); 
int sum(int a, int d, int n);

int main(){
    FILE *ptr;  // declaring a file pointer
    ptr=fopen("series.txt", "w"); // creating a new file to write into
    for(int i=-3; i<17; i++){
        fprintf(ptr, "%d ", sum(1,2,i));
    }
    fprintf(ptr,"%d\n", sum(1,2,17));
    for(int i=-3; i<9; i++){
        fprintf(ptr, "%d ", terms(1,2,i)); // printing the terms of the AP
    }
    fprintf(ptr, "%d\n", terms(1,2,9));
    int s_6=0, s_16=0;  // finding the sum of the first 7 terms and 17 terms of the AP
    for(int i=0; i<7; i++){
        fprintf(ptr, "%d ", terms(1,2,i));
        s_6 +=terms(1,2,i);
    }
    fprintf(ptr, "\n%d\n", s_6);
    for(int i=0; i<17; i++){
        fprintf(ptr, "%d ", terms(1,2,i));
        s_16 +=terms(1,2,i);
    }
    fprintf(ptr, "\n%d", s_16);
}

int terms(int a, int d, int n){
    if(n<0) return 0;
    else return a+n*d;  // function which generates terms of the AP
}

int sum(int a, int d, int n){
    if(n<0) return 0;
    else return 0.5*(n+1)*(2*a+n*d);
}