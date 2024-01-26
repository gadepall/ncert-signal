import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt", skiprows=0)
x_values, y_values, z_values = data[:, 0], data[:, 1], data[:,2]


# Plot the stem plots
plt.stem(x_values, y_values, linefmt='-', markerfmt='ro', basefmt='-', label='x_1(n)')
plt.stem(x_values, z_values, linefmt='-', markerfmt='bo', basefmt='-', label='x_2(n)')
plt.stem(12, 87, linefmt='-', markerfmt='go', basefmt='-', label='n=12')
print(x_values, y_values, z_values)

# Set labels and legend
plt.xlabel('n')
plt.legend()
plt.grid(True)
plt.show()

