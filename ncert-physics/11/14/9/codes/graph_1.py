import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
with open('data.txt', 'r') as file:
    data_x_custom = [float(line.strip()) for line in file]

# Plotting the graph
time = np.arange(0, len(data_x_custom), 1) / 1000.0  # Assuming a sampling rate of 1000 Hz
plt.plot(time, data_x_custom)
plt.title(' x(t)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig("analog1.png")
