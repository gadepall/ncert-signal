#include <stdio.h>
#include <math.h>

int main() {
     FILE *file;
        file = fopen("result.dat", "w");

 if (file == NULL) {
           printf("Error opening file!\n");
        return 1;
         }

    fprintf(file, "n\tAmount\n");

    for (int n = 0; n <= 10; ++n) {
   double amount = 15625 * pow(0.8, n);
                                                    fprintf(file, "%d\t%.2f\n", n, amount);
     }

  fclose(file);

    return 0;
}
