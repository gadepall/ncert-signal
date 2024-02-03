import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt", skiprows=0)
x_values, y_values= data[:, 0], data[:, 1]


# Plot the stem plots
plt.stem(x_values, y_values, linefmt='-', markerfmt='ro', basefmt='-', label='x_(n)')

plt.stem(1, 9, linefmt='-', markerfmt='go', basefmt='-', label='n=1')
plt.stem(2, 27, linefmt='-', markerfmt='go', basefmt='-', label='n=2')

# Set labels and legend
plt.xlabel('n')
plt.legend()
plt.grid(True)
plt.show()

