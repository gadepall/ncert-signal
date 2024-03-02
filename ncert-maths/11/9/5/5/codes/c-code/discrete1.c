#include <stdio.h>

// Function to generate the second sequence
void generateSecondSequence() {
    int original_sequence[] = {2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 35, 36, 38, 40, 42, 44, 45, 46, 48, 50, 52, 54, 
    55, 56, 58, 60, 62, 64, 65, 66, 68, 70, 72, 74, 75, 76, 78, 80, 82, 84, 85, 86, 88, 90, 92, 94, 95, 96, 98, 100};
    int n = sizeof(original_sequence) / sizeof(original_sequence[0]);

    int second_sequence[n];
    int current_sum = 0;

    FILE *file = fopen("values1.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return;
    }

    for (int i = 0; i < n; i++) {
        current_sum += original_sequence[i];
        second_sequence[i] = current_sum;
        fprintf(file, "%d ", second_sequence[i]);
    }

    fclose(file);
}

int main() {
    generateSecondSequence();

    return 0;
}