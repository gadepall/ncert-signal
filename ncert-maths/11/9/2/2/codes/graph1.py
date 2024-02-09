import matplotlib.pyplot as plt
import numpy as np

# Generate data points using NumPy arrays for the new function
n_values = np.arange(0, 200)
y_values = (5 * n_values**2 + 215 * n_values + 210) / 2

# Highlight the 178th term
highlighted_x = n_values[177]
highlighted_y = y_values[177]

# Save data to output.dat file
np.savetxt('output.dat', np.column_stack((n_values, y_values)), fmt='%d %.2f')

# Read the data from the file for plotting
data = np.loadtxt("output.dat")
x_values = data[:, 0]
y_values = data[:, 1]

# Create a discrete stem plot for the entire function
plt.stem(x_values, y_values, linefmt='-', markerfmt='o', basefmt='', label='(5n^2 + 215n + 210)/2')

# Highlight the 178th term with a red dot and annotation
plt.scatter([highlighted_x], [highlighted_y], color='red', label='178th term', marker='o', s=100, zorder=3)
plt.annotate('y(n)=98450', xy=(highlighted_x, highlighted_y), xytext=(highlighted_x - 20, highlighted_y + 200))

# Add labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Discrete Stem Plot of Sum(n) vs n ')

# Show legend
plt.legend()

# Display the plot
plt.show()
