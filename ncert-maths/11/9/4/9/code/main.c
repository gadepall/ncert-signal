#include <stdio.h>
#include<math.h>
int main(){
	int n=10,x[10],y[10],u[10],i;
	for (i=0;i<n;i++){
		int a=(i+1)*(i+2)*(2*i+3);
		x[i]= a/6 +pow(2,i+2)-2;
		}
	for (i=1;i<=n;i++){
		u[i-1] = i*i +pow(2,i);
		}
	for(i=0;i<n;i++){
		y[i]=0;
	for(int j=0;j<=i;j++){
		y[i] =y[i] + u[j];}
	}
    FILE *fp = fopen("output.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    for (int i = 0; i < n; i++) {
        fprintf(fp, "%d\t  %d\n", x[i], y[i]);
    }
    fclose(fp);

    return 0;
}

