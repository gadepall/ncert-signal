#include <stdio.h>

int main() {
    // Simulate the same data
    int n[] = { 1, 2, 3, 4, 5};
    int y_n[] = {3, 9, 27, 81, 243};

    // Write the simulated data to a file
    FILE *fp;
    fp = fopen("terms_c.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    fprintf(fp, "n y_n\n");
    for (int i =0; i < 5; i++) {
        fprintf(fp, "%d %d\n", n[i], y_n[i]);
    }
    fclose(fp);

    return 0;
}
