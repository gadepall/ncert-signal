import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.loadtxt("data12.dat")

# Separate n and x(n) values
n_values, x_values = data[:, 0], data[:, 1]

# Plot the graph
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r-', label=r'$x(n) = (253 - 5n)u(n)$')
plt.xlabel('n')
plt.ylabel('x(n)')

highlight_n = 20
highlight_index = np.where(n_values == highlight_n)[0]
plt.stem(n_values[highlight_index], x_values[highlight_index], linefmt='r-', markerfmt='ro', label=f'n = {highlight_n}')

plt.grid(True)
plt.legend()
plt.savefig('x(n)_vs_n.png')
