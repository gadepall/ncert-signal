#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("values.dat", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int x;
    for (x = -5; x < 30; x++) {
        double y = (x >= 0) ? (5 + x * 1.75) : 0;
        fprintf(file, "%d %f\n", x, y);
    }

    fclose(file);
    

    return 0;
}
