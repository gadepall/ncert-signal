#include<stdio.h>
#include<math.h>
int u(int n){
	if(n<0) return 0;
	else return 1;
}  // unit step function

int sum(int n){
    return ((n+1)*(n+2)*(n+2)*(n+3)/12)*u(n);
} // sum to n terms of the series

void convolve(int sig1[],int sig2[], int res[], int size1, int size2)
{
	int len_result = size1 + size2 - 1;

    for (int i = 0; i < len_result; i++) {
        res[i] = 0;
        for (int j = 0; j < size1; j++) {
            if (i - j >= 0 && i - j < size2) {
                res[i] += sig1[j] * sig2[i - j];
            }
        }
    }
} // function to convolve the arrays

int x(int n){
	return pow((n+1),2)*u(n);
} // general term of the series

int main(){
    FILE *ptr;
    ptr=fopen("series.dat", "w");
    for(int i=-3; i<10; i++){
        fprintf(ptr,"%d ", sum(i));
    }
    fprintf(ptr,"%d\n", sum(10));// theoretical values of sum of n terms of the series

    int size1=16, size2=16;
	int sig1[size1];
	for(int i=-3; i<14;i++){
		sig1[i+3]=u(i);
	}
	int sig2[size2];
	for(int i=0; i<16; i++){
		sig2[i]=x(i-3);
	}
	int result1[size1+size2-1];
	convolve(sig1, sig2, result1, size1, size2);
	int result2[2*size1+size2-2];
	convolve(sig1,result1,result2,size2,size1+size2-1);
	for(int i=6; i<19; i++){
		fprintf(ptr,"%d ", result2[i]);
	}
    fprintf(ptr, "%d",result2[19]);// sum to n terms of the series using convolution

    fclose(ptr);
}