#include<stdio.h>

int x_n(int n) {
    return (3+6*n) * (n >= 0);
}

int main() {
    int sum1=0;

    FILE *file1 = fopen("values.dat", "w");
    if (file1 == NULL) {
        printf("Error opening file!");
        return 1;
    }

    for (int n = 0; n <= 10; ++n) {
        int x_value = x_n(n);
        sum1+= x_value;
        fprintf(file1, "%d %d\n", n, x_value);
    }

    fclose(file1);
    return 0;
}
