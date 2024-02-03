#include<stdio.h>
int func(int n){
	return 17+9*n;
}
void main(){
int sum = 0;
FILE *ptr;
ptr = fopen("series.txt","w");
for (int i = 0; func(i)<=350; i++){
	fprintf(ptr,"%d ",func(i));
	sum += func(i);
}
fprintf(ptr,"\n%d",sum);
}
