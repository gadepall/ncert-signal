#include <stdio.h>

int main() {
    int sum = 0;
    for (int n = 5; n <= 30; n++) {
        sum += n * n;
        printf("%d\n", sum);
    } 
    return 0;
}
