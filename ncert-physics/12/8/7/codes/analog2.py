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

# Amplitude of the electric field
E_amplitude = 153

# Positions to plot
x_values = [1, 2, 3, 4]

plt.figure(figsize=(10, 6))

# Plotting for each value of x
for x in x_values:
    # Electric field component (general form)
    E_field = E_amplitude * np.sin(omega * t - k * x)

    # Plotting
    plt.plot(t, E_field, label=f'Electric Field (E) at x={x}')

plt.title('Electric Field Component versus Time at Different Positions')
plt.xlabel('Time (s)')
plt.ylabel('Field Amplitude')
plt.legend()
plt.grid(True)
plt.show()

