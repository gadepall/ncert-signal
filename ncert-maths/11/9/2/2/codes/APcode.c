#include <stdio.h>

int main() {
    int sum = 0;
    int num;

    // Loop through numbers from 100 to 1000
    for(num = 105; num < 1000; num++) {
        // Check if the number is a multiple of 5
        if(num % 5 == 0) {
            sum += num;
        }
    }

    printf("The sum of numbers between 100 and 1000 which are multiples of 5 is: %d\n", sum);

    return 0;
}
