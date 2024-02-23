import matplotlib.pyplot as plt
import numpy as np

# Parameters for the geometric progression
first_term = 4
common_ratio = 4
total_terms = 8

# Generate data points using NumPy arrays for the geometric progression
n_values = np.arange(1, total_terms + 1)
y_values = first_term * (1 - common_ratio**n_values) / (1 - common_ratio)

# Highlight the 8th term (index 7)
highlighted_x = n_values[7]
highlighted_y = y_values[7]

# Save data to output.dat file
np.savetxt('output.dat', np.column_stack((n_values, y_values)), fmt='%d %.2f')

# Read the data from the file for plotting
data = np.loadtxt("output.dat")
x_values = data[:, 0]
y_values = data[:, 1]

# Create a discrete stem plot for the entire function
plt.stem(x_values, y_values, linefmt='-', markerfmt='o', basefmt='', label='Simulation')

# Highlight the 8th term with a red dot and annotation
plt.scatter([highlighted_x], [highlighted_y], color='blue', label='8th term', marker='o', s=100, zorder=3)
plt.annotate(f'Sum={highlighted_y}', xy=(highlighted_x, highlighted_y), xytext=(highlighted_x - 0.5 , highlighted_y - 50))
plt.scatter(x_values, y_values, color='red', marker='x', zorder=3 , label='Theory')
# Add labels and title
plt.xlabel('Term Number (n)')
plt.ylabel('Sum')
plt.title('Discrete Stem Plot of Sum of GP vs Term Number')

# Show legend
plt.legend()

# Display the plot
plt.show()
