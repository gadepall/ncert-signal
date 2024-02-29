#include <stdio.h>
#include <math.h> 

int main() {
    FILE *file;
    file = fopen("codes/points.txt", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    int n,end;
    printf("Enter the end value for n: ");
    scanf("%d", &end);

    // Generate and store points in the text file
    
    for (n = 1; n <= end; n++) {
        double result = pow(-1, n) * pow(n+1, 3);
        fprintf(file, "%d\t%.2f\n", n, result);
    }

    fclose(file);

    printf("Points generated and stored in 'points.txt' file.\n");

    return 0;
}
