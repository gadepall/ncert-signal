#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("gp_sum_data.txt", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate data for the sum of the first n terms of the GP with first term 3 and common ratio 3
    int first_term = 3;
    int common_ratio = 3;
    int sum = 0;
    int common_ratio_power = 1;

    for (int n = 0; n <= 3; ++n) {
        sum += first_term * common_ratio_power;

        // Update common_ratio_power for the next iteration
        common_ratio_power *= common_ratio;

        fprintf(fp, "%d %d\n", n, sum);
    }

    fclose(fp);
    return 0;
}

