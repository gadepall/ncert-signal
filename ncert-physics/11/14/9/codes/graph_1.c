#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("data.txt", "w");  // Open file for writing

    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    double angular_frequency = 2 * M_PI * 1.0;  // Adjust the angular frequency as needed
    double amplitude = 0.02;  // Amplitude of the cosine wave
    double duration = 5.0;    // Duration of the signal in seconds
    double sampling_rate = 1000.0;  // Sampling rate in Hz

    int num_samples = (int)(duration * sampling_rate);

    for (int i = 0; i < num_samples; i++) {
        double t = i / sampling_rate;
        double x_t = amplitude * cos(angular_frequency * t);
        fprintf(file, "%lf\n", x_t);
    }

    fclose(file);

    return 0;
}
