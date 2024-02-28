import numpy as np
import matplotlib.pyplot as plt

# Given parameters
L = 0.12  # inductance in Henry
C = 480 * 10**(-9)  # capacitance in Farad
R = 23  # resistance in Ohms

# Define the frequency range (including both positive and negative values)
omega = np.linspace(-10000, 10000, 2000)  # adjust the range as needed

# Calculate |H(jω)|
H = np.abs(R + 1j * omega * L + 1 / (1j * omega * C))

# Calculate the point for given values
omega_given = 1 / np.sqrt(L * C)
H_given = np.abs(R + 1j * omega_given * L + 1 / (1j * omega_given * C))

# Create subplots with adjusted spacing
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the graph
ax.plot(omega, H, label='|H(jω)|')
ax.scatter(omega_given, H_given, color='red', label='Given values')

# Mark the given point
ax.annotate(
    f'({omega_given:.2f}, {H_given:.2f})',
    xy=(omega_given, H_given),
    xytext=(omega_given, H_given + 0.1),
    arrowprops=dict(facecolor='black', shrink=0.05),
)

ax.set_title('|H(jω)| vs. ω')
ax.set_xlabel('Frequency (rad/s)')
ax.set_ylabel('|H(jω)|')
ax.legend()
ax.grid(True)

plt.tight_layout()  # Adjust spacing
plt.show()

