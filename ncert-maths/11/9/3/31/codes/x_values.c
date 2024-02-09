include <stdio.h>
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
				            double amount = 500 * pow(1.1, n);
					            fprintf(file, "%d\t%.2f\n", n, amount);
						        }

			        fclose(file);

				    return 0;
}
