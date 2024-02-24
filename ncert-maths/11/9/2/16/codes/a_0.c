#include <stdio.h>

int main() {
    FILE *file = fopen("pqrs.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the output to the file
    int a = 1;
    int d = 2;
    int start_n = 0;
    int end_n = 8;
    int n;
    for (n = start_n; n <= end_n; ++n) {
        int term_value;
        if (n >= 1)
            term_value = (a + (n + 1) * d)-2;
        else
            term_value = 1;
        fprintf(file, "%d %d\n",n, term_value);
    }

    fclose(file);
    return 0;
}
