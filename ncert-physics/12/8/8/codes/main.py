import numpy as np
import matplotlib.pyplot as plt

# Function to calculate electric field vector E
def electric_field(x, t):
    return 120 * np.sin(1.05 * x - 3.1 * 10**8 * t)

# Function to calculate magnetic field vector B
def magnetic_field(x, t):
    return (4e-7) * np.sin(1.05 * x - 3.14 * 10**8 * t)

# Values for x
x_values = [1, 2, 3]

# Time values with smaller increments for better visualization
time_values = np.linspace(0, 1e-7, 1000)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plotting the graphs for electric field (E) in the first subplot
for x in x_values:
    E_values = electric_field(x, time_values)
    ax1.plot(time_values, E_values, label=f'E, x = {x}')

# Set axis labels and title for Electric Field (E)
ax1.set_ylabel('Electric Field (E)')
ax1.set_title('Electric Field vs Time')
ax1.legend()  # Display legend with x values
ax1.grid(True)

# Plotting the graphs for magnetic field (B) in the second subplot
for x in x_values:
    B_values = magnetic_field(x, time_values)
    ax2.plot(time_values, B_values, label=f'B, x = {x}')

# Set axis labels and title for Magnetic Field (B)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Magnetic Field (B)')
ax2.set_title('Magnetic Field vs Time')
ax2.legend()  # Display legend with x values
ax2.grid(True)

# Adjust layout for better spacing
plt.tight_layout()

# Show the combined plot with two subplots
plt.show()
