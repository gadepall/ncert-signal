import numpy as np
import matplotlib.pyplot as plt

# Generate time values
t = np.linspace(0, 4e-6, 1000)  # Time values from 0 to 1e-6 seconds with 1000 points

# Calculate the corresponding y values
f = 10**9
y = np.cos(2 * np.pi * f * t)

# Plot the graph
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()
