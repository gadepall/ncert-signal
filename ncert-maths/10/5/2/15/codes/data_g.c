#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int a1 = 63;
    int d1 = 2;
    int a2=3;
    int d2=7;
    int start_n = 0;
    int end_n = 14;

    // Write a and d values to the file

    // Calculate values for the entire range of n and write to file
    for (int n = start_n; n <= end_n; ++n) {
        int x1_n = (a1 + d1 * n) > 0 ? (a1 + d1 * n) : 0;
        int x2_n = (a2 + d2 * n) > 0 ? (a2 + d2 * n) : 0;
        fprintf(file, "%d %d %d\n", n, x1_n, x2_n);
    }

    fclose(file);

    return 0;
}
