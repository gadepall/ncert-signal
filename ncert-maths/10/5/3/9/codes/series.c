#include<stdio.h>
int terms(int a, int d, int n); 

int main(){
    FILE *ptr;  // declaring a file pointer
    ptr=fopen("series.txt", "w"); // creating a new file to write into
    for(int i=-3; i<9; i++){
        fprintf(ptr, "%d ", terms(1,2,i)); // printing the terms of the AP
    }
    fprintf(ptr, "%d\n", terms(1,2,9));
    int s_7=0, s_17=0;  // finding the sum of the first 7 terms and 17 terms of the AP
    for(int i=0; i<7; i++){
        fprintf(ptr, "%d ", terms(1,2,i));
        s_7 +=terms(1,2,i);
    }
    fprintf(ptr, "\n%d\n", s_7);
    for(int i=0; i<17; i++){
        fprintf(ptr, "%d ", terms(1,2,i));
        s_17 +=terms(1,2,i);
    }
    fprintf(ptr, "\n%d", s_17);
}

int terms(int a, int d, int n){
    if(n<0) return 0;
    else return a+n*d;  // function which generates terms of the AP
}