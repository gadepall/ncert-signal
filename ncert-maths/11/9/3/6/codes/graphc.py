import matplotlib.pyplot as plt
import numpy as np

# Read data from file
data = np.loadtxt("data.txt")
n_values, y1, y2 = data[:, 0], data[:, 1], data[:, 2]

# Plot the data for the first sequence
plt.stem(n_values, y1, linefmt='-', markerfmt='o', basefmt='r', label=r'$(-7/2)^{n-1}$')
plt.xlabel('n')
plt.ylabel("x(n)")
plt.legend()
plt.grid(True)
plt.savefig("graph1.png")
plt.clf()  # Clear the figure for the next plot

# Plot the data for the second sequence
plt.stem(n_values, y2, linefmt='-', markerfmt='o', basefmt='r', label=r'$-(7/2)^{n-1}$')
plt.xlabel('n')
plt.ylabel("x(n)")
plt.legend()
plt.grid(True)
plt.savefig("graph2.png")

