#include <stdio.h>

void calculate_and_save_coordinates(FILE *file, int a, int d, int n) {
    for (int i = 0; i <= n; ++i) {
        fprintf(file, "%d %d\n", i, a + d * i);
    }
}

long long calculate_sum(int a, int d, int n) {
    // Sum of an AP: S(n) = n/2 * [2a + (n-1)d]
    return (long long)n * (2 * (long long)a + (n - 1) * (long long)d) / 2;
}

void verify_sum(int a, int d, int n) {
    long long expected_sum = 3 * (long long)n * n + 5 * (long long)n;
    long long actual_sum = calculate_sum(a, d, n);

    if (actual_sum == expected_sum) {
        printf("Sum verified.\n");
    } else {
        printf("Sum verification failed.\n");
    }
}

int main() {
    FILE *file;
    file = fopen("coordinates.txt", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and save coordinates for x(n) = a + dn for n = 0 to 30
    calculate_and_save_coordinates(file, 8, 6, 30);

    // Verify the sum for the given AP
    verify_sum(8, 6, 30);

    fclose(file);

    return 0;
}

