#include <stdio.h>

int main() {
    int y = 0;
    int n;
    int y1=0;
    int y2=0;
    FILE *outputFile;

    // Open the file for writing
    outputFile = fopen("values.dat", "w");

    if (outputFile == NULL) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    // Print the sequence values to the console and save them to the file
    for (n = 1; n <= 49; ++n) {
        y=y+n;
        printf("%d \n",y);
        fprintf(outputFile, "%d \n", y);
    }

    // Close the file
    fclose(outputFile);

    for(n=1;n<=34;n++){
        y1=y1+n;
    }
    for(n=36;n<=49;n++){
        y2=y2+n;
    }

    printf("y1 = %d\n",y1);
    printf("y2 = %d\n",y2);

    if(y1==y2){
        printf("%d=%d\n",y1,y2);
        printf("x=35, Hence Proved");

    }


    return 0;
}