import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.loadtxt("coordinate.txt")
t, current = data[:, 0], data[:, 1]

# Scale the current values to match the desired Irms
scaling_factor = 15.92 / np.sqrt(np.mean(current**2))
current *= scaling_factor

# Calculate the RMS value
rms_current = np.sqrt(np.mean(current**2))

# Plot the current vs. time
plt.plot(t, current, label='Current')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.axhline(y=rms_current, color='r', linestyle='--', label=f'RMS Current: {rms_current:.4f} A')
plt.legend()
plt.grid(True)
plt.show()

