#include <stdio.h>

int main() {
    // Define variables
    int firstTerm = 9;
    int commonDifference = 8;
    int targetSum = 636;
    
    // Initialize variables for the loop
    int currentTerm = firstTerm;
    int sum = 0;
    int termsCount = 0;

    // Iterate until the sum reaches or exceeds the target
    while (sum < targetSum) {
        // Add the current term to the sum
        sum += currentTerm;

        // Move to the next term
        currentTerm += commonDifference;

        // Increment the count of terms
        termsCount++;
    }

    // Print the result
    printf("Number of terms needed: %d\n", termsCount);

    return 0;
}

