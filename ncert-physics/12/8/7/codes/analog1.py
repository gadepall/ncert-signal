import numpy as np
import matplotlib.pyplot as plt

# Time values scaled from 0 to 10^-7
t = np.linspace(0, 1e-7, 1000)  # Time from 0 to 10^-7

# Speed of light
c = 3.0e8  # Speed of light in m/s

# Wave number
k = 1.0     # Wave number

# Calculate angular frequency
omega = c * k

# Amplitude of the magnetic field
B_amplitude = 510e-9  # 510 nano

# Positions to plot
x_values = [1, 2, 3, 4]

plt.figure(figsize=(10, 6))

# Plotting magnetic field for each value of x
for x in x_values:
    # Magnetic field component (90 degrees out of phase with electric field)
    B_field = B_amplitude * np.sin(omega * t - k * x + np.pi/2)
    plt.plot(t, B_field, linestyle='--', label=f'Magnetic Field (B) at x={x}')

plt.title('Magnetic Field Component versus Time at Different Positions')
plt.xlabel('Time (s)')
plt.ylabel('Field Amplitude')
plt.legend()
plt.grid(True)
plt.show()

