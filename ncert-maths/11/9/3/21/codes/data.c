#include <stdio.h>

int main() {
    FILE *file = fopen("data1.txt", "w");
    if (file == NULL) {
        perror("Error creating file");
        return 1;
    }
    
    // Generate data for x(n) = 3(-2)^n u(n) till n=5
    int xn = 3; // Initialize x(0)
    fprintf(file, "%d\n", xn);
    for (int n = 1; n <= 5; n++) {
        xn *= -2; // Multiply by -2 for each iteration
        fprintf(file, "%d\n", xn);
    }

    fclose(file);
    return 0;
}

