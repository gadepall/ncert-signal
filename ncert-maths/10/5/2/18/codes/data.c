#include <stdio.h>

int main() {
    FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int n;
        for (n = 0; n < 8; n++) {
            int x = (-13 + 5 * n) * (n >= 0); 
            // x(n) = (-13 + 5n)u(n)
            fprintf(file, "%d %d\n", n, x);
        }
    
    fclose(file);
    printf("Data written to data.dat\n");
    return 0;
}

