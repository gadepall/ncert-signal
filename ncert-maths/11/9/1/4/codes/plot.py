import matplotlib.pyplot as plt
import numpy as np

# Load data using loadtxt
data = np.loadtxt("data.txt")

# Extract x and y values
x, y = data[:, 0], data[:, 1]

# Plot the terms
plt.stem(x, y, markerfmt='o', linefmt='b-', basefmt='r-')
plt.title('Terms of the Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()
plt.savefig('plot.png')

