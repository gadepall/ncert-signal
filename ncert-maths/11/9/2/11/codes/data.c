#include <stdio.h>
#include <stdlib.h>

int main() 
{

    // Generate random values for x (first term) and y (common difference)
    int x_0 = 5; // Random value between 0 and 9
    int d = 2; // Random value between 1 and 5

    int n = 10; // Number of terms

    FILE *file = fopen("arithmetic_progression_data.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file!\n");
        return 1;
    }

    for (int i = 0; i <= n; ++i) {
        int term = x_0 + (i) * d;
        fprintf(file, "%d %d\n", i, term);
    }

    fclose(file);

    // Assume specific values for p, q, r, a, and d
    int p = rand()%10+1;
    int q = rand()%10+1;
    int r = rand()%10+1;

    // Calculate the sum of the first p, q, and r terms of the arithmetic progression
    int a = p * (2 * x_0 + (p - 1) * d) / 2;
    int b = q * (2 * x_0 + (q - 1) * d) / 2;
    int c = r * (2 * x_0 + (r - 1) * d) / 2;

    // Verify the expression
    double expression_result = (1.0 * a / p) * (q - r) + (1.0 * b / q) * (r - p) + (1.0 * c / r) * (p - q);

    printf("Assumed values:\n");
    printf("p: %d\nq: %d\nr: %d\n", p, q, r);
    printf("\na=%d\nb=%d\nc=%d\n",a, b, c);
    printf("Expression result: %f\n", expression_result);

    return 0;
}
