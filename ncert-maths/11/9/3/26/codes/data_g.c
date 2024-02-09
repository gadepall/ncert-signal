#include <stdio.h>
void print(FILE *file,int a, int r, int start_n, int end_n)
{
    int term=1;
    for (int n = start_n; n < end_n; ++n) 
    {
        int x_n = (term*r) > 0 ? (term*r) : 0;
        term = x_n;
        fprintf(file, "%d %d\n", n, x_n);
    }
    
}

int main() {
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    print(file, 3,3,0,4);
    fclose(file);

    return 0;
}
