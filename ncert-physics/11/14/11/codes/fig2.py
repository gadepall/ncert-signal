import numpy as np
import matplotlib.pyplot as plt

# Load data from the "output.dat" file using numpy's loadtxt
data = np.loadtxt("output.dat")

# Extract n_values and y_values from the data
x_values = data[402:, 0].astype(float)
y_values = data[402:, 1].astype(float)

# Plot
plt.plot(x_values, y_values)
plt.xlabel(r'$t$')
plt.ylabel(r'$-2\cos{\frac{\pi}{2}t}$')
plt.grid(True)
plt.savefig('../figs/fig2.png')
