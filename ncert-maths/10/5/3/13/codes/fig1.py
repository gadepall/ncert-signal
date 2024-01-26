import matplotlib.pyplot as plt
import numpy as np

# Read a and d values from the file
a, d = np.loadtxt("data.txt", max_rows=1, dtype=int)

# Read data (excluding the first line with a and d values)
data = np.loadtxt("data.txt", skiprows=1)
n_values, ap_values = data[:, 0], data[:, 1]

# Calculate the sum using NumPy vectorized approach
sum_x_n = np.sum(np.maximum(0, a + d * n_values))

# Plot the data
plt.stem(n_values, ap_values, basefmt='b-', linefmt='d-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('a.png')

