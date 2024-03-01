import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data_y = np.loadtxt('values_y.dat', delimiter=' ', comments='Values')

# Extracting values for y(n)
n_values_y = data_y[:, 0]
y_values = data_y[:, 1]

# Create the stem plot for y(n)
plt.stem(n_values_y, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)

# Save the plot as an image file
plt.savefig('plot_y.png')

# Show the plot
plt.show()

