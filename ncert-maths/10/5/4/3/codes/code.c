#include <stdio.h>
int main() {    
    double bottomToTopDistanceCm = 250; 
    double rungDistanceCm = 25; 
    double bottomRungLengthCm = 45; 
    double topRungLengthCm = 25;    
    int numberOfRungs = (int)(bottomToTopDistanceCm / rungDistanceCm) + 1;
    double totalLengthCm = (numberOfRungs / 2.0) * (bottomRungLengthCm + topRungLengthCm);
    printf("Total length of wood required: %.2f centimeters\n", totalLengthCm);
    return 0;
}

