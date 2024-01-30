#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Maximum length of allocated strings
#define MAX_STRING_LENGTH 128

// Number of terms to compute
#define NUMBER_OF_TERMS 8

const int FIRST_TERM = 30;

const int COMMON_RATIO = 2;

// Function that calculates x(n) = (30 * 2^n)u(n)
unsigned long long x(int n) {
    if (n < 0) {
        // 0 for all negative values
        return 0;
    }
    // 2^n can be represented as a left bitshift by n bits.
    return FIRST_TERM * pow(COMMON_RATIO, n);
}

int main() {
    // File pointer
    FILE* out;
    // Open the file.
    fopen_s(&out, "11_9_3_30cout.txt", "w");
    // Character pointer to store the formatted string.
    char* formatted_str = (char*) malloc(sizeof(char) * MAX_STRING_LENGTH);
    for (int i = 0; i < NUMBER_OF_TERMS; i++) {
        // Format the string.
        sprintf(formatted_str, "%llu ", x(i));
        // Write the formatted string to the file.
        fputs(formatted_str, out);
    }
    // Close the file.
    fclose(out);
    // Free the memory allocated for the formatted string.
    free(formatted_str);
}