#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("data_v.txt", "w");  // Open file for writing

    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    double frequency = 20.0;  // Frequency in Hz
    double amplitude = -0.4;  // Amplitude of the sine wave
    double duration = 1.0;    // Duration of the signal in seconds
    double sampling_rate = 1000.0;  // Sampling rate in Hz

    int num_samples = (int)(duration * sampling_rate);

    for (int i = 0; i < num_samples; i++) {
        double t = i / sampling_rate;
        double v_t = amplitude * sin(2 * M_PI * frequency * t);
        fprintf(file, "%lf\n", v_t);
    }

    fclose(file);

    return 0;
}
