#include<stdio.h>
int main()
{
     double power(double b, int e)
     {
     double r=1;
     int i;
     for(i=0;i<e;i++)
     {
     r*=b;
     }
     return r;
     }

    FILE *file = fopen("values.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    fprintf(file, "Values for stem plot of x_1(n):\n");
    
    for (int i = 0; i < 8; i++) {
        int term=8;
        double sum=0;
        for(int j=0;j<i+1;j++)
        {
         sum+=term;
         term=term*10+8;
        }
        fprintf(file, "%d %f\n", i, sum);
    }

    fprintf(file, "\nValues for stem plot of x_2(n):\n");  // Add a newline and heading

    for (int i = 0; i < 8; i++) {
        int n = i;
        float x_2 = (float)((8)*(power(10,n+2) - 9 * (n) - 19))/81;
        fprintf(file, "%d %.2f\n", n, x_2);
    }

    fclose(file);  // Close the file

    return 0;

}
