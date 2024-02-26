import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt("data.dat")

n_values = data[:, 0]
x_values = data[:, 1]

# Plot the stem graph
plt.stem(n_values, x_values, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x(n)')
#plt.title('Stem Plot of x(n)')
plt.grid(True)
plt.savefig('x_n_stem_plot.png')  # Save the plot as a PNG file
plt.show()

