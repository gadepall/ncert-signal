#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Calculate and write values to file
    for (int n = 0; n <= 25; n++) {
        int xn = 4 * n + 1;
        fprintf(file, "%d %d\n", n, xn);
    }

    fclose(file);

    return 0;
}

