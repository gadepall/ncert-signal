#include <stdio.h>

void generate_ap(int start, int common_diff, int n, const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file for writing.\n");
        return;
    }

    for (int i = 0; i < n; i++) {
        fprintf(file, "%d\n", start + i * common_diff);
    }

    fclose(file);
}

int main() {
    int start_value = 100;
    int common_difference = 1;
    int num_terms = 10;
    const char *filename = "ap_data.txt";

    generate_ap(start_value, common_difference, num_terms, filename);

    return 0;
}

