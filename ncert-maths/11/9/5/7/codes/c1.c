#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("data.txt", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate x(n) = 3^(n+1) without using pow
    int power_of_three = 3;
    for (int n = 0; n <= 3; ++n) {
        int x_n = 1; // Initialize with 3

        // Multiply by 3 for (n+1) times
        for (int i = 0; i <= n; ++i) {
            x_n *= power_of_three;
        }

        fprintf(fp, "%d %d\n", n, x_n);
    }

    fclose(fp);
    return 0;
}
