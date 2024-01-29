import numpy as np
import matplotlib.pyplot as plt

# Read values from the file
data = np.loadtxt('values.dat')
x = data[:, 0]
y = data[:, 1]

# Plot the graph
plt.stem(x, y)
plt.xlim(-5, 30)
plt.ylim(0, 55)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
