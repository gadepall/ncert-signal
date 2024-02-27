#include <stdio.h>

#define N 10 // Number of points

int main() {
    FILE *file;
    file = fopen("coordinates.txt", "w");

    if (file == NULL) {
        fprintf(stderr, "Error opening file coordinates.txt\n");
        return 1;
    }

    int n;
    long result;

    for (n = 0; n < N; n++) {
        result = (n + 1) * (n + 3);
        fprintf(file, "%d %ld\n", n, result);
    }

    fclose(file);

    printf("Coordinates saved to coordinates.txt\n");

    return 0;
}

