import numpy as np
import matplotlib.pyplot as plt

# Define parameters
V0 = 1.0  # amplitude of voltage
C = 30e-6   # capacitance
L = 27e-3  # inductance
omega_0 = 1.11e3  # angular frequency

# Time values
t = np.linspace(0, 0.05, 1000)  # adjust the time range as needed

# Current equation
current = V0 * np.sqrt(C / L) * np.sin(omega_0 * t)

# Plotting
plt.plot(t, current)
plt.xlabel('t in seconds')
plt.ylabel('I(t) in Amperes')
plt.grid(True)
plt.savefig('p.png', dpi=300, bbox_inches='tight')

