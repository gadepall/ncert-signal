#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("data12.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = -2; n <= 20; ++n) {
        int u_n = (n >= 0) ? 1 : 0;
        fprintf(file, "%d %d\n", n, (253 - 5 * n) * u_n);
    }

    fclose(file);

    return 0;
}
