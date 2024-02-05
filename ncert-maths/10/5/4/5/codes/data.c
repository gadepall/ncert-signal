#include <stdio.h>

double calculateY(int n) {
    if (n >= 0) {
        return (n + 1) * (6.25 + n * 3.125);
    } else {
        return 0.0;
    }
}

int main() {
    FILE *file = fopen("output.txt", "w");
    
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(file, "n\t\ty(n)\n");

    for (int n = -5; n <= 14; ++n) {
        double result = calculateY(n);
        fprintf(file, "%d\t\t%.6f\n", n, result);
    }

    fclose(file);

    printf("Data written to output.txt successfully.\n");

    return 0;
}
