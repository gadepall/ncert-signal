import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters
R = 40
L = 5
C = 80e-6  # 80uF = 80 * 10^-6 F

omega = np.linspace(0, 100, 100)  # You can adjust the range and number of points as needed

# Calculate the modulus of Z for each frequency
modulus_Z = np.sqrt(R**2 + (1 - (omega)**2 * L * C)**2)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(omega, modulus_Z, label='|Z|')
plt.scatter(50, 40)
plt.text(50, 40, '(50, 40)', verticalalignment='bottom', horizontalalignment='right')  # Add text at (50, 40)
plt.title('Impedance vs Frequency')
plt.xlabel('Frequency ($\omega$)')
plt.ylabel('|Z|')
plt.grid(True)
plt.yscale('log')
plt.legend()
plt.savefig("../figs/impedance.png")
plt.close()

# Define the voltage function epsilon
def epsilon(omega, t):
    return 230 * np.sqrt(2) * np.exp(1j * omega * t)

# Define V_C and V_L functions
def V_C(omega, t):
    return np.real(-1j / (omega * C) * epsilon(omega, t) / R)

def V_L(omega, t):
    return np.real(1j * omega * L * epsilon(omega, t) / R)

# Generate values for omega and t
omega_values = np.linspace(45, 50, 1000)
t_values = np.linspace(0, 0.2, 1000)

# Create meshgrid for omega and t
omega_mesh, t_mesh = np.meshgrid(omega_values, t_values)

# Calculate V_C + V_L for each omega and t combination
V_combined = V_C(omega_mesh, t_mesh) + V_L(omega_mesh, t_mesh)

# Create a new figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(omega_mesh, t_mesh, V_combined, cmap='viridis', alpha=0.8)
fig.colorbar(surf, shrink=0.5, aspect=5)

# Mark omega = 50 with a vertical line
t_min, t_max = min(t_values), max(t_values)
ax.plot([50, 50], [t_min, t_max], [0,0], color='red', linestyle='--', linewidth=2)
ax.text(50, t_min, 0, "$\omega=50$", color='red', fontsize=12, ha='right', va='bottom')
# Set labels and title
ax.set_xlabel('$\omega$')
ax.set_ylabel('$t$')
ax.set_zlabel('$V_C + V_L$ (Volts)')
ax.set_title('$V_C + V_L$ vs $\omega$ vs $t$')
plt.savefig("../figs/LCvoltage.png")
plt.close()

V = 230 * np.sqrt(2) * np.exp(1j * 50 * t_values)

# Plot the real and imaginary parts
plt.figure(figsize=(10, 6))
plt.plot(t_values, V.real, label='Input voltage')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Input Voltage vs Time (50 Hz)')
plt.legend()
plt.grid(True)
plt.savefig("../figs/Vin.png")

