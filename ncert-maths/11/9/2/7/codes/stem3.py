import matplotlib.pyplot as plt
import numpy as np

# Specify file paths
file_path1 = 'theory.dat'
file_path2 = 'simulation.dat'

# Read data from file1
data1 = np.loadtxt(file_path1)
x_values1, y_values1 = data1[:, 0], data1[:, 1]

# Read data from file2
data2 = np.loadtxt(file_path2)
x_values2, y_values2 = data2[:, 0], data2[:, 1]

# Plot theory data using plt.stem
plt.stem(x_values1, y_values1, linefmt='r-', markerfmt='r^', basefmt='b-', label='Theory')

# Plot simulation data using plt.scatter
plt.scatter(x_values2, y_values2, color='black', marker='o', label='Simulation')

# Set labels and legend
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.legend()

# Save and display the plot
plt.savefig('fig2.png')
plt.show()

