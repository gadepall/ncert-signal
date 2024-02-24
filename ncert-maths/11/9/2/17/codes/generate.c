#include<stdio.h>
int u(int n){
	if(n>=0){
	  return 1; 
	}
	else{
	 return 0;
	}

}

int x(int n){
	return (100 + 5*n)*(u(n));
}
void main(){
   FILE *ptr;
   ptr = fopen("gen_values.txt","w");
   for (int  n=-10; n <=30; n++){
   	fprintf(ptr, "%d %d\n", n,x(n));
  }
   fclose(ptr);

}
