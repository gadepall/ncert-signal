#include <stdio.h>
#include <float.h>

int main() {
    FILE *file = fopen("1.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Parameters for the first GP
    double x0_1 =-4.0/3.0 ;
    double r_1 = 2;

    // Parameters for the second GP
    double x0_2 = 4.0;
    double r_2 = -2;

    // Number of terms
    int n = 10;

    // Write the values for both GPs to the file in two columns with integers on the x-axis
    for (int i = 1; i <= n; ++i) {
        fprintf(file, "%d\t%e\t%e\n", i, x0_1, x0_2);
        x0_1 *= r_1;
        x0_2 *= r_2;
    }
    
    // Close the file
    fclose(file);

    //Read the values from the file and callculate the sum of first two terms
    file = fopen("1.dat", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double sum_1 = 0, sum_2 = 0, ratio_1, ratio_2;

    for (int i = 0; i < 2; ++i) {
        int index;
        double term_1, term_2;
        fscanf(file, "%d %lf %lf", &index, &term_1, &term_2);

        sum_1 += term_1;
        sum_2 += term_2;

    }
    
    for (int i = 0; i < 5; i++) {
    	int index;
        double term_1, term_2;
        fscanf(file, "%d %lf %lf", &index, &term_1, &term_2);
    	if ( i==2 )
        {
        	ratio_1 = term_1;
        	ratio_2 = term_2;
        }
        if( i==4 )
        {
        	ratio_1 = term_1/ratio_1;
        	ratio_2 = term_2/ratio_2;
        }
    }
    
    // Print the results
    printf("Sum of the first two terms for sequence 1: %e\n", sum_1);
    printf("Ratio of 5th and 3rd term for sequence 1: %e\n", ratio_1);
    printf("Sum of the first two terms for sequence 2: %e\n", sum_2);
    printf("Ratio of 5th and 3rd term for sequence 2: %e\n", ratio_2);
    

    return 0;
}
