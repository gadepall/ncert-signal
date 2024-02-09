import numpy as np
import matplotlib.pyplot as plt

# Load coordinates from the text file
coordinates = np.loadtxt('coordinates.txt')

# Extract n_values and x_values from coordinates
n_values, x_values = coordinates[:, 0], coordinates[:, 1]

# Plot the stem plot with the highlighted point at n=26 in red
highlight_index = np.where(n_values == 26)[0][0]

plt.stem(n_values, x_values, linefmt='-', markerfmt='.', basefmt=' ')
plt.stem(n_values[highlight_index], x_values[highlight_index], linefmt='r-', markerfmt='ro', basefmt=' ')

plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of x(n) = 8 + 6n')
plt.grid(True)
plt.show()

