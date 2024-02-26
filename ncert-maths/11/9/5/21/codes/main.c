#include <stdio.h>
#include <stdlib.h>

// Function for convolution
void convolution(const double *array1, int len1, const double *array2, int len2, double *result) {
    int lenResult = len1 + len2 - 1;
    for (int i = 0; i < lenResult; i++) {
        result[i] = 0;
    }
    for (int i = 0; i < len1; i++) {
        for (int j = 0; j < len2; j++) {
            result[i + j] += array1[i] * array2[j];
        }
    }
}

// Function for generating the sequence 0.6+0.66+0.666+...
void generate_sequence(double *sequence, int length) {
    double num = 0.6;
    for (int i = 0; i < length; i++) {
        sequence[i] = num;
        num = num * 0.1 + 0.6;
    }
}

// Function for simulating the sequence and writing partial sums to file
void simulate_and_write_to_file(const char *filename, int length) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file %s.\n", filename);
        return;
    }

    double value = 0.6; // First term
    double sum = 0;    // Initialize sum
    for (int i = 0; i < length; i++) {
        sum += value;
        fprintf(file, "%lf\n", sum); // Writing partial sum to file
        value = value * 0.1 + 0.6;    // Generate the next term
    }

    fclose(file);
}

// Function for reading a sequence from a file
void read_sequence_from_file(const char *filename, double *sequence, int length) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file %s.\n", filename);
        return;
    }

    for (int i = 0; i < length; i++) {
        fscanf(file, "%lf", &sequence[i]);
    }

    fclose(file);
}

// Function for displaying a stem plot
void display_stem_plot(const double *data, int length) {
    printf("Stem plot:\n");
    for (int i = 0; i < length; i++) {
        printf("%2d |", (int)data[i]);
        for (int j = 0; j < (int)data[i]; j++) {
            printf("*");
        }
        printf("\n");
    }
}

// Function for convolution (integer version)
void convolution_int(const int *array1, int len1, const int *array2, int len2, int *result) {
    int lenResult = len1 + len2 - 1;
    for (int i = 0; i < lenResult; i++) {
        result[i] = 0;
    }
    for (int i = 0; i < len1; i++) {
        for (int j = 0; j < len2; j++) {
            result[i + j] += array1[i] * array2[j];
        }
    }
}

// Function for generating the sequence 5+55+555+...
void generate_sequence_int(int *sequence, int length) {
    int num = 5;
    for (int i = 0; i < length; i++) {
        sequence[i] = num;
        num = num * 10 + 5;
    }
}

// Function for simulating the sequence and writing partial sums to file (integer version)
void simulate_and_write_to_file_int(const char *filename, int length) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file %s.\n", filename);
        return;
    }

    int value = 5; // First term
    int sum = 0;   // Initialize sum
    for (int i = 0; i < length; i++) {
        sum += value;
        fprintf(file, "%d\n", sum); // Writing partial sum to file
        value = value * 10 + 5;      // Generate the next term
    }

    fclose(file);
}

// Function for reading a sequence from a file (integer version)
void read_sequence_from_file_int(const char *filename, int *sequence, int length) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file %s.\n", filename);
        return;
    }

    for (int i = 0; i < length; i++) {
        fscanf(file, "%d", &sequence[i]);
    }

    fclose(file);
}

// Function for displaying a stem plot (integer version)
void display_stem_plot_int(const int *data, int length) {
    printf("Stem plot:\n");
    for (int i = 0; i < length; i++) {
        printf("%2d |", data[i]);
        for (int j = 0; j < data[i]; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main() {
    int N = 6; // Number of terms in the sequence
    double sequence[N];

    // Generating the sequence 0.6+0.66+0.666+...
    generate_sequence(sequence, N);

    // Creating a sequence of 1s
    double u[N];
    for (int i = 0; i < N; i++) {
        u[i] = 1;
    }

    // Performing convolution
    double result[N + N - 1];
    convolution(sequence, N, u, N, result);

    // Writing the convolution result to a file
    FILE *convolutionFile = fopen("simuate2.dat", "w");
    if (convolutionFile == NULL) {
        printf("Error opening file for convolution result.\n");
        return 1;
    }
    for (int i = 0; i < N; i++) {
        fprintf(convolutionFile, "%lf\n", result[i]);
    }
    fclose(convolutionFile);

    // Simulating the sequence and writing partial sums to a file
    simulate_and_write_to_file("theory2.dat", N);

    // Analysis phase
    // Reading the convolution result from the file
    double convolution_result[N];
    read_sequence_from_file("simuate2.dat", convolution_result, N);

    // Reading the simulated sequence from the file
    double simulated_sequence[N];
    read_sequence_from_file("theory2.dat", simulated_sequence, N);

    // Displaying stem plot for convolution result
    printf("Stem plot for convolution result:\n");
    display_stem_plot(convolution_result, N);

    // Displaying stem plot for simulated sequence
    printf("\nStem plot for simulated sequence:\n");
    display_stem_plot(simulated_sequence, N);

    // For the integer version
    int sequence_int[N];
    generate_sequence_int(sequence_int, N);

    int u_int[N];
    for (int i = 0; i < N; i++) {
        u_int[i] = 1;
    }

    // Performing convolution (integer version)
    int result_int[N + N - 1];
    convolution_int(sequence_int, N, u_int, N, result_int);

    // Writing the integer convolution result to a file
    FILE *convolutionFile_int = fopen("simuate1.dat", "w");
    if (convolutionFile_int == NULL) {
        printf("Error opening file for integer convolution result.\n");
        return 1;
    }
    for (int i = 0; i < N; i++) {
        fprintf(convolutionFile_int, "%d\n", result_int[i]);
    }
    fclose(convolutionFile_int);

    // Simulating the integer sequence and writing partial sums to a file
    simulate_and_write_to_file_int("theory1.dat", N);

    // Analysis phase for the integer version
    // Reading the integer convolution result from the file
    int convolution_result_int[N];
    read_sequence_from_file_int("simuate1.dat", convolution_result_int, N);

    // Reading the integer simulated sequence from the file
    int simulated_sequence_int[N];
    read_sequence_from_file_int("theory1.dat", simulated_sequence_int, N);

    printf("\nInteger version:\n");
    // Displaying stem plot for integer convolution result
    printf("Stem plot for integer convolution result:\n");
    display_stem_plot_int(convolution_result_int, N);

    // Displaying stem plot for integer simulated sequence
    printf("\nStem plot for integer simulated sequence:\n");
    display_stem_plot_int(simulated_sequence_int, N);

    return 0;
}

