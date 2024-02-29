#include <stdio.h>

int main() {
    FILE *file = fopen("values.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening the file for writing.\n");
        return 1;
    }

    for (int n = 0; n <= 63; ++n) {
        int xn = 12 + 4 * n;
        fprintf(file, "%d\n", xn);
    }

    fclose(file);
    return 0;
}
