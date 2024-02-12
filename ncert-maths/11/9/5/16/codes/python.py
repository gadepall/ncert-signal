import matplotlib.pyplot as plt
import numpy as np

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract n_values and y_values from the data
n_values = data[:, 0].astype(int)
x_values = data[:, 1]

# Create a stem plot
plt.stem(n_values, x_values, linefmt='|', markerfmt='o', basefmt='b', label='Stem Plot')

plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.legend()
plt.savefig('../figs/fig1.png')
plt.show()


