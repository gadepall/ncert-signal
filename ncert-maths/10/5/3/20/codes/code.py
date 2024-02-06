import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.loadtxt('data.dat', skiprows=1)
n_values = data[:, 0]
x_values = data[:, 1]
y_values = data[:, 2]

# Highlighted index
highlight_index = 5

# Plot x(n) with highlighted stem at n=5 in red
plt.figure(figsize=(8, 4))
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='b-', label='x(n)')

# Highlight the stem at n=5 in red
plt.stem(n_values[highlight_index], x_values[highlight_index], linefmt='r-', markerfmt='ro', basefmt='r-')

plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()
plt.grid(True)
plt.savefig('plot1.png')
plt.show()

# Plot y(n) with highlighted stem at n=5 in red
plt.figure(figsize=(8, 4))
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='b-', label='y(n)')

# Highlight the stem at n=5 in red
plt.stem(n_values[highlight_index], y_values[highlight_index], linefmt='r-', markerfmt='ro', basefmt='r-')

plt.xlabel('n')
plt.ylabel('y(n)')
plt.legend()
plt.grid(True)
plt.savefig('plot2.png')
plt.show()

