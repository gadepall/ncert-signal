import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
with open('data_a.txt', 'r') as file:
    data_a = [float(line.strip()) for line in file]

# Plotting the graph
time = np.arange(0, len(data_a), 1) / 1000.0  # Assuming a sampling rate of 1000 Hz
plt.plot(time, data_a)
plt.title('x\'\'(t)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig("analog3.png")
