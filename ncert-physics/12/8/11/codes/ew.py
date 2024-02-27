import numpy as np
import matplotlib.pyplot as plt

# Constants
N_C = 3.1  # N/C
WAVE_NUMBER = 1.8  # rad/m
ANGULAR_FREQUENCY = 5.4e6  # rad/s

# Function for Electric Field
def electric_field(y, t):
    return N_C * np.cos(WAVE_NUMBER * y + ANGULAR_FREQUENCY * t)
# Create a meshgrid for y and t
y_values = np.linspace(0, 10, 500)  # adjust the range as needed
t_values = np.linspace(0, 1e-5, 500)  # adjust the range as needed
y_mesh, t_mesh = np.meshgrid(y_values, t_values)

# Calculate the electric field values
E_values = electric_field(y_mesh, t_mesh)
# Plot the 2D sinusoidal wave
plt.plot(y_values, E_values[0, :], label='Electric Field')
plt.title('Electric Field as a Sinusoidal Wave')
plt.xlabel('y (m)')
plt.ylabel('EM Wave')
plt.legend()
plt.grid(True)
plt.show()

