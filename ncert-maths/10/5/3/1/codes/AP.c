#include <stdio.h>

void generateAP(float initial, float commonDiff, int terms, int n_values[], float y_values[]) {
    for (int i = 0; i < terms; i++) {
        n_values[i] = i;
        y_values[i] = initial + i * commonDiff;
    }
}

void saveToDatFile(int n_values[], float y_values[], int terms) {
    FILE *fp;
    fp = fopen("ap3_data.dat", "w");
    if (fp == NULL) {
        return;
    }

    fprintf(fp, "n_value y_value\n");
    for (int i = 0; i < terms; i++) {
        fprintf(fp, "%d %f\n", n_values[i], y_values[i]);
    }

    fclose(fp);
}

float calculateSum(float initial, float commonDiff, int n) {
    return (n + 1) * (2 * initial + n * commonDiff) / 2;
}

void saveSumToDatFile(int n_values[], float sums[], int terms) {
    FILE *fp;
    fp = fopen("ap3_sum.dat", "w");
    if (fp == NULL) {
        return;
    }
    fprintf(fp, "n_value sum\n");
    for (int i = 0; i < terms; i++) {
        fprintf(fp, "%d %f\n", n_values[i], sums[i]);
    }

    fclose(fp);
}

int main() {
    float initial, commonDiff;
    int terms;
    
    printf("Enter initial term: ");
    scanf("%f", &initial);
    
    printf("Enter common difference: ");
    scanf("%f", &commonDiff);
    
    printf("Enter number of terms: ");
    scanf("%d", &terms);

    int n_values[terms];
    float y_values[terms];

    generateAP(initial, commonDiff, terms, n_values, y_values);
    saveToDatFile(n_values, y_values, terms);
    
    float sums[terms];
    for (int i = 0; i < terms; i++) {
        sums[i] = calculateSum(initial, commonDiff, i);
    }

    saveSumToDatFile(n_values, sums, terms);

    return 0;
}

