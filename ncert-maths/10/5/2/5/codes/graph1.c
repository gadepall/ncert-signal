#include <stdio.h>
int main() {
    FILE *file = fopen("values.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    float first_term_1 = 7;
    float first_term_2 = 18;

    float common_difference_1 = 6;     //13 - 7
    float common_difference_2 = -2.5;   //15.5 - 18

    int n ; // nth term of the series 
    float x1;  //term of the first series
    float x2;  //term of the second series

    for(n=0;n<21;n++)
    {
        x1 = first_term_1 + (float)(n)*(common_difference_1);
        x2 = first_term_2 + (float)(n)*(common_difference_2);
        fprintf(file ,"%d \t %e \t %e\n",n , x1 , x2);
    }
    fclose(file);
    return 0;
}
