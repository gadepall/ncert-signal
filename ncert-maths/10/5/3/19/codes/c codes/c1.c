#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("data.txt", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Generate y(n) = (n+1) * (40-n) * 0.5 and write to file
    for (int n = 0; n <= 16; ++n) {
        fprintf(fp, "%d %f\n", n, (n + 1) * (40 - n) * 0.5);
    }

    fclose(fp);
    return 0;
}
