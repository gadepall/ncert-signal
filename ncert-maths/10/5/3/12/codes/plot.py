import matplotlib.pyplot as plt
import numpy as np

# Generate data points using NumPy arrays
n_values = np.arange(0, 50)
y_values = 3 * n_values**2 + 6 * n_values + 3 * n_values + 6

# Highlight the 39th term
highlighted_x = n_values[38]
highlighted_y = y_values[38]

# Save data to output.dat file
np.savetxt('output.dat', np.column_stack((n_values, y_values)), fmt='%d %.2f')

# Read the data from the file for plotting
data = np.loadtxt("output.dat")
x_values = data[:, 0]
y_values = data[:, 1]

# Create a discrete stem plot for the entire function
plt.stem(x_values, y_values, linefmt='-', markerfmt='o', basefmt='', label='3n^2 + 6n + 3n + 6')

# Highlight the 39th term with a red dot and annotation
plt.scatter([highlighted_x], [highlighted_y], color='red', label='39th term', marker='o', s=100, zorder=3)
plt.annotate('4920', xy=(highlighted_x, highlighted_y), xytext=(highlighted_x - 5, highlighted_y + 50))

# Add labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
#plt.title('Discrete Stem Plot of 3n^2 + 6n + 3n + 6 vs n with 39th term highlighted')

# Show legend
plt.legend()

# Display the plot
plt.show()

