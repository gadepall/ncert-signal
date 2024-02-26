#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("digital2_points.txt", "w");

    if (fp == NULL) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    int n, points;

    // Specify the range for n (e.g., n > 0)
    for (n = 0; n <= 20; ++n) {  // Adjust the range as needed
        // Calculate the value of the sequence
        points = 4 * (n + 1) * (n + 2);

        // Write the points to the file
        fprintf(fp, "%d %d\n", n, points);
    }

    fclose(fp);

    printf("Stem plot points have been written to 'digital2_points.txt'.\n");

    return 0;
}
