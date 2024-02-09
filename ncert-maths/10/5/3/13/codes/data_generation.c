#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int a = 8;
    int d = 8;
    int start_n = -2;
    int end_n = 15;

    // Write a and d values to the file
    fprintf(file, "%d %d\n", a, d);

    // Calculate values for the entire range of n and write to file
    for (int n = start_n; n <= end_n; ++n) {
        int x_n = (a + d * n) > 0 ? (a + d * n) : 0;
        fprintf(file, "%d %d\n", n, x_n);
    }

    fclose(file);

    return 0;
}

