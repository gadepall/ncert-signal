import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Set the backend to Agg for Termux
matplotlib.use('Agg')

# Read data from result.dat
data = np.genfromtxt('result.dat', skip_header=1)

# Extract columns
n_values = data[:, 0]
amount_values = data[:, 1]

# Stem plot
plt.stem(n_values, amount_values, basefmt='b-', linefmt='r-', markerfmt='ro', use_line_collection=True)
plt.stem(10, amount_values[-1], linefmt='g-', markerfmt='go', label='n=10', use_line_collection=True)
plt.xlabel('Years (n)')
plt.ylabel('Amount')
plt.grid(True)

# Save the plot to a file (optional)
plt.savefig('stem_plot.png')

# Display the legend
plt.legend()

# Display the plot in Termux
plt.show()
