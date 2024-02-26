#include<stdio.h>

int x_n(int n) {
    return ((n+1)*(n+2)) * (n >= 0);
}

int u(int n) {
    return (n >= 0) ? 1 : 0;
}

int convolution(int n) {
    int result = 0;
    for (int k = 0; k <= n; k++) {
        result += x_n(k) * u(n - k);
    }
    return result;
}

int y_n(int n) {
    return ((n+1)*(n+2)*(n+3)/3) * (n >=0);
}

int main() {
    int sum1=0;

    FILE *file1 = fopen("simulation_values.dat", "w");
    if (file1 == NULL) {
        printf("Error opening file!");
        return 1;
    }

    for (int n = 0; n <= 10; ++n) {
        int x_value = x_n(n);
        int y_value = y_n(n);

        sum1+= x_value;
        fprintf(file1, "%d %d %d\n", n, x_value,y_value);
    }

    fclose(file1);
    int sum2=0;

    FILE *file2 = fopen("analysis_values.dat", "w");
    if (file2 == NULL) {
        printf("Error opening file!");
        return 1;
    }

    for (int n = 0; n <= 10; ++n) {
        int x_value1 = x_n(n);
        int y_value1 = convolution(n);

        sum2+= x_value1;
        fprintf(file2, "%d %d %d\n", n, x_value1,y_value1);
    }

    fclose(file2);
    return 0;
}
