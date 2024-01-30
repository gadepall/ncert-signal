#include <stdio.h>

// Function to calculate the general term of an arithmetic progression
int general_term(int x0, int d, int n) {
    return x0 + n * d;
}

int main() {
    int m, n, x0, xm, xm_n, xm_n_sum_xm, d;

    m = 6;
    n = 2;

    // Given values for the AP
    x0 = 3; // Changed x0 to 3
    d = 2;

    // Calculating the terms
    xm = general_term(x0, d, m);
    xm_n = general_term(x0, d, m - n);
    xm_n_sum_xm = general_term(x0, d, m + n) + xm_n;

    // Checking if the sum of (m+n)th and (m-n)th terms is equal to twice the mth term
    if (xm_n_sum_xm == 2 * xm) {
        printf("Therefore x(m+n) + x(m-n) = 2 * x(m)\n");
    } else {
        printf("The sum of (m+n)th and (m-n)th terms is NOT equal to twice the mth term.\n");
    }

    return 0;
}

