#include <stdio.h>

// Function to generate arithmetic progression and save to file
void generate_arithmetic_progression(int a, int d, int n, const char *filename) {
    FILE *fp;
    fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening the file.\n");
        return;
    }

    // Generate and write the arithmetic progression values to file
    for (int i = 0; i < n; i++) {
        fprintf(fp, "%d\n", a + i*d);
    }
    fclose(fp);
}

int main() {
    // Parameters for the arithmetic progressions
    int a[] = {2, 18, 5, -4, 53};  // initial terms
    int d[] = {12, -5, 3/2, 2, -15};  // common differences
    int n = 30; // number of terms

    // Generate the arithmetic progressions and save to files
    for (int i = 0; i < 5; i++) {
        char filename[10];
        sprintf(filename, "data%d.txt", i + 1);
        generate_arithmetic_progression(a[i], d[i], n, filename);
    }

    return 0;
}

