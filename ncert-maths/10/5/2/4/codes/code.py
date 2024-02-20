import numpy as np
import matplotlib.pyplot as plt

# Read data from the .dat file
data = np.loadtxt("AP.dat")

# Extract n_values and x_n_values from the data
n_values = data[:, 0]
x_n_values = data[:, 1]

# Create a stem plot
plt.stem(n_values, x_n_values, basefmt='b-', linefmt='b-', markerfmt='bo', use_line_collection=True)

# Highlight the stem at n=15
highlight_index = 15
highlight_n = n_values[highlight_index]
highlight_x_n = x_n_values[highlight_index]
plt.stem(highlight_n, highlight_x_n, linefmt='r-', markerfmt='ro', label='n=15', use_line_collection=True)

# Set labels and title
plt.xlabel('n')
plt.ylabel('$x(n)$')

# Set x-axis ticks to integers
plt.xticks(np.arange(min(n_values), max(n_values)+1, 1))

# Add legend
plt.legend()

# Save the plot
plt.savefig('plot_with_highlight.png')

# Show the plot
plt.show()

