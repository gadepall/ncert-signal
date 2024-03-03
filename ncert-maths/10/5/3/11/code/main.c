#include <stdio.h>

// Function to calculate the sum of the first n terms of an arithmetic progression
int x(int n) {
    return 3 - 2 * n;
}

// Function to calculate the arithmetic progression
void arithmetic_progression(int n, int a, int d,int shravya[]) {
     for (int i=0;i<n;i++){
    shravya[i] = 4 * n - n * n;
}
}

void convolution( int y[],int a,int d, int n) {
   for (int i = 0; i<n;i++){
   	y[i] = (i+1)*(2*a + (i)*d)/2;
    }
}

int main() {
    int n=10,a=3, d=-2;
    int sh[10];  
    int x_sequence[10]; // Sequence x(n)
    int u_sequence[10]; // Sequence u(n)
    int y_sequence[10];
    for (int i = 1; i <= n; i++) {       
            sh[i-1] =4*i-i*i  ;     
    }
    for (int i = 0; i < n; i++) {
        x_sequence[i] = x(i);
    }

    // Generate sequence u(n) (unit step function)
    for (int i = 0; i < n; i++) {
        u_sequence[i] = 1;
    }
    convolution(  y_sequence, a,d,n);

    FILE *fp = fopen("output.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    for (int i = 0; i < n; i++) {
        fprintf(fp, "%d\t %d\n", sh[i], y_sequence[i]);
    }
    fclose(fp);

    return 0;
}

