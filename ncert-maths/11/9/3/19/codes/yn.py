import numpy as np
import matplotlib.pyplot as plt

# Read data from .dat file
data = np.loadtxt('yn.dat')

# Separate data into x and y values
x = data[:, 0]
y = data[:, 1]

# Plot the graph
plt.plot(x, y, marker='o', linestyle='-')
plt.title('Plot of y(n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()

