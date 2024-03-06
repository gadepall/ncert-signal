#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("data_a.txt", "w");  // Open file for writing

    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    double frequency = 20.0;  // Frequency in Hz
    double amplitude = -8.0;  // Amplitude of the cosine wave
    double duration = 1.0;    // Duration of the signal in seconds
    double sampling_rate = 1000.0;  // Sampling rate in Hz

    int num_samples = (int)(duration * sampling_rate);

    for (int i = 0; i < num_samples; i++) {
        double t = i / sampling_rate;
        double a_t = amplitude * cos(2 * M_PI * frequency * t);
        fprintf(file, "%lf\n", a_t);
    }

    fclose(file);
    return 0;
}
