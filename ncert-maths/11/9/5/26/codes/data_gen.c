#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("output_data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Print headers
    fprintf(file, "n     x1(n)     x2(n)      y1(n)     y2(n)\n");

    // Generate values for n to cover the range from -10 to 10 (inclusive) with a step of 1
    for (int n = -10; n <= 10; n++) {
        // Calculate and write to file
        fprintf(file, "%d %lf %lf %lf %lf\n", n,
            n >= 0 ? ((n + 1) * pow((n + 2), 2)) : 0,
            n >= 0 ? pow((n + 1), 2) * (n + 2) : 0,
            n >= 0 ? (3 * pow(n, 4) + 26 * pow(n, 3) + 81 * pow(n, 2) + 106 * n + 48) / 12 : 0,
            n >= 0 ? (3 * pow(n, 4) + 22 * pow(n, 3) + 57 * pow(n, 2) + 62 * n + 24) / 12 : 0);
    }

    fclose(file);

    return 0;
}
