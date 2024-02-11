#include <stdio.h>

int main() {
    FILE *file1 = fopen("data1.txt", "w");
    if (file1 == NULL) {
        perror("Error creating file1");
        return 1;
    }
    float x_1 = 7;
    float d_1 = 3.5;
    for (int i = 0; i < 23; i++) {
        float term1 = x_1 + i * d_1;
        fprintf(file1, "%f ", term1);
    }
    fclose(file1);

    FILE *file2 = fopen("data2.txt", "w");
    if (file2 == NULL) {
        perror("Error creating file2");
        return 1;
    }
    float x_2 = 34;
    float d_2 = -2;
    for (int i = 0; i < 13; i++) {
        float term2 = x_2 + i * d_2;
        fprintf(file2, "%f ", term2);
    }
    fclose(file2);

    FILE *file3 = fopen("data3.txt", "w");
    if (file3 == NULL) {
        perror("Error creating file3");
        return 1;
    }
    float x_3 = -5;
    float d_3 = -3;
    for (int i = 0; i < 76; i++) {
        float term3 = x_3 + i * d_3;
        fprintf(file3, "%f ", term3);
    }
    fclose(file3);

    // Code to read and calculate sums from the files
    FILE *file1_read = fopen("data1.txt", "r");
    if (file1_read == NULL) {
        perror("Error opening data1.txt");
        return 1;
    }
    float term1, sum1 = 0.0;
    while (fscanf(file1_read, "%f", &term1) == 1) {
        sum1 += term1;
    }
    fclose(file1_read);
    printf("Sum for x_1(n): %.1f\n", sum1);

    FILE *file2_read = fopen("data2.txt", "r");
    if (file2_read == NULL) {
        perror("Error opening data2.txt");
        return 1;
    }
    float term2, sum2 = 0.0;
    while (fscanf(file2_read, "%f", &term2) == 1) {
        sum2 += term2;
    }
    fclose(file2_read);
    printf("Sum for x_2(n): %.1f\n", sum2);

    FILE *file3_read = fopen("data3.txt", "r");
    if (file3_read == NULL) {
        perror("Error opening data3.txt");
        return 1;
    }
    float term3, sum3 = 0.0;
    while (fscanf(file3_read, "%f", &term3) == 1) {
        sum3 += term3;
    }
    fclose(file3_read);
    printf("Sum for x_3(n): %.1f\n", sum3);

    return 0;
}

