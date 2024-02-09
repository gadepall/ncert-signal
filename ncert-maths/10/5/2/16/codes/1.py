import matplotlib.pyplot as plt
import numpy as np

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract n_values and y_values from the data
n_values = data[:, 0].astype(int)
y_values = data[:, 1].astype(int)

# Create a stem plot
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='b-', label='Stem Plot')
plt.stem(4,28, linefmt='r--',markerfmt='bo',basefmt='r-')
plt.stem(6,40, linefmt='r--',markerfmt='bo',basefmt='r-')

plt.xlabel('n_values')
plt.ylabel('x(n)_values')
plt.grid(True)
plt.legend()

plt.savefig('../figs/fig1.png')
plt.show()
