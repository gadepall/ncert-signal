import numpy as np
import matplotlib.pyplot as plt

# Load data from .dat file
file_path = 'simulated.dat'
y = np.loadtxt(file_path)

# Generate x values based on the length of y
x = np.arange(1, len(y) + 1)

# Highlight a specific value
highlight_index =  # Replace with the index you want to highlight
highlight_x = x[highlight_index]
highlight_y = y[highlight_index]

# Plot the graph
plt.stem(x, y, label='Data',basefmt='k-',linefmt='b-',markerfmt='bo',use_line_collection=True)
plt.scatter(highlight_x, highlight_y, color='red', label='Highlighted Point')

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Your Data with Highlighted Point')

# Add legend
plt.legend()

# Save the figure
plt.savefig('../figs/main.png',dpi=300)

# Show the plot
plt.show()
