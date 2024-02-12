#include <stdio.h>
#include <math.h>

// Function to calculate the product of n terms in a geometric progression
double calculateProduct(int n, double a, double r) {
    double product = 1.0;
    for (int i = 0; i < n; i++) {
        product *= a * pow(r, i);
    }
    return product;
}

int main() {
    // Given values
    double x0, xn, r;
    int n;

    // Input the values of a, b, r, and n
    printf("Enter the first term (a): ");
    scanf("%lf", &x0);

    printf("Enter the nth term (b): ");
    scanf("%lf", &xn);


    printf("Enter the number of terms (n): ");
    scanf("%d", &n);

    r= pow((xn/x0),(1.0/(n-1)));
    // Calculate P and (ab)^n
   double P = calculateProduct(n, x0, r);
    double ab_pow_n = pow(x0*xn,(double)n);
          printf("%lf\n",ab_pow_n);
          printf("%lf\n",P);    // Check if P^2 equals (ab)^n
    if (pow(P, 2) == ab_pow_n) {
        printf("The statement P^2 = (ab)^n is verified.\n");
    } else {
        printf("The statement P^2 = (ab)^n is not verified.\n");
    }

    return 0;
}
