#include<stdio.h>
#include<stdlib.h>
float y(int n){
	float sum = 0;
	for(int i=0; i<=n; i++){
		sum += 1.0/((i+1)*(i+2));
	}
	return sum;
}
/*void append(*ptr, len, add){
	ptr = (int *)realloc(ptr, sizeof(int)*(len+1));
	*(ptr+len) = add;*/

float y_calcu(int n){
	return 1-(1.0/(n+2));
}
void main(){
	FILE *fptr;
	fptr = fopen("Values.txt","w");
	//int *ptr = (int*)malloc(int(s))
	for(int i = 0; i<=10 ; i++){
		//printf("%f ,", t);
		fprintf(fptr, "%d %.3f %.3f\n", i, y(i), y_calcu(i));
	}
}
