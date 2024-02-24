#include<stdio.h>

int linspace(int a, int n, int d){

      return a+n*d ;
}


int main(){
int d,a,n,b;
a=8;
b=26;
n=7;
d=(b-a)/(n-1);

FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Discrete values for n
    for (int i = 0; i < 7; i++) {
        int k;
        k = linspace(8, i, d);
        if(n != 6){
            fprintf(file, "%d ", k);
        }
        else{
            fprintf(file, "%d", k);

        }
    }
    






fclose(file);
return 0;
}
