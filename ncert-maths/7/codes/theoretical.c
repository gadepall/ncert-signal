#include <stdio.h>

int sum(int x) {
    int s = (x+1)*(4+x*7)/2;
    return s;
}

int main() {
    int n = 39, a = 2, d = 7;
    for(int n=0;n<40;n++){
    printf("%d\n", sum(n));
    }
    return 0;
}
