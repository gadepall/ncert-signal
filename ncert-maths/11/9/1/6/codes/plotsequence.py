import numpy as np
import matplotlib.pyplot as plt


# Read data from the .dat file with space as the delimiter
data = np.loadtxt('output.dat', delimiter=' ')

x = data[:, 0]
y = data[:, 1]

# Plot the data
plt.stem(x, y, basefmt='b-', linefmt='r-', markerfmt='ro', bottom=0)

highlight_indices = [0, 1, 2, 3, 4]
for i in highlight_indices:
    plt.stem(i, y[i], linefmt='b-', markerfmt='bo', basefmt='y-', bottom=0)

plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid(True)

# Save the plot to a file (e.g., PNG)
plt.savefig('plot_from_c.png')
plt.show()

