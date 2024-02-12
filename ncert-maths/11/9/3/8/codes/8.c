#include <stdio.h>
#include <math.h>

#define NUM_TERMS 10

void generate_gp(double first_term, double common_ratio, double *gp_sequence) {
    FILE *fp;
    fp = fopen("gp_values.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }
	float sum=0;
    for (int n = 0; n < NUM_TERMS; n++) {
    	sum += first_term * pow(common_ratio, n);
        gp_sequence[n] =sum;
        fprintf(fp, "%.6f\n", gp_sequence[n]);
    }

    fclose(fp);
}
void generate_gp_sum(double first_term, double common_ratio, double *gp_sequence) {
    FILE *fp;
    fp = fopen("gp_sum_values.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    for (int n = 0; n < NUM_TERMS; n++) {
    	float	a=pow(common_ratio,n+1);
    	float	b= a-1;
    	float	c= common_ratio - 1;
    	float	d=b / c;
        gp_sequence[n] = first_term * d;
        fprintf(fp, "%.6f\n", gp_sequence[n]);
    }

    fclose(fp);
}

int main() {
    double first_term = sqrt(7);
    double common_ratio = sqrt(3);
    double gp_sequence[NUM_TERMS];

   generate_gp(first_term, common_ratio, gp_sequence);
   generate_gp_sum(first_term, common_ratio, gp_sequence);
    return 0;
}

