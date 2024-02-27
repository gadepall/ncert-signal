#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    int a = 2;
    int d = 7;
    int start_n = 0;
    int end_n = 15;

    

    // Calculate values for the entire range of n and write to file
    for (int n = start_n; n <= end_n; ++n) {
        int x_n = (a + d * n) > 0 ? (a+n*d) : 0;
        fprintf(file, "%d %d\n", n, x_n);
    }

    fclose(file);

    return 0;
}
