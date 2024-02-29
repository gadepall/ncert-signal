import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = np.sqrt(2)
omega = np.pi
phi = -np.pi/4

# Time values
t = np.linspace(0, 2*np.pi, 100)

# SHM equation
y = A * np.cos(omega * t + phi)

# Plotting
plt.plot(t, y, label=f'$A \cos( \omega t + \phi)$', color='blue')
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.legend()
plt.grid(True)
plt.show()

