import matplotlib.pyplot as plt
import numpy as np

# Constants
I0 = 14.14  # Amplitude for current
V0 = 300.0   # Amplitude for voltage
phi = 0.0    # Phase shift
frequency = 50.0  # Frequency in Hz

# Time values
t = np.linspace(0, 0.02, 1000)  # Time from 0 to 1 second with 1000 points

# Current and Voltage functions
I = I0 * np.sin(2 * np.pi * frequency * t + np.radians(phi))
V = V0 * np.sin(2 * np.pi * frequency * t + np.radians(phi))

# Plotting Current
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, I, label=r'$I(t) = I_0 \cdot \sin(100\pi t + \phi)$')
plt.axhline(y=10, color='blue', linestyle='--', label='Horizontal Line at I')
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Current (I)')
plt.title('Sine Wave Current with Marked Point and Lines')
plt.legend()

# Plotting Voltage
plt.subplot(1, 2, 2)
plt.plot(t, V, label=r'$V(t) = V_0 \cdot \sin(100\pi t + \phi)$')
plt.axhline(y=212.13, color='blue', linestyle='--', label='Horizontal Line at V')
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Sine Wave Voltage with Marked Point and Lines')
plt.legend()

# Adjust layout and save the plot as an image (e.g., PNG)
plt.tight_layout()
plt.savefig('../figs/merged_sine_wave_plots.png')

# Show the plots (optional)
plt.show()

