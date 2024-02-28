import matplotlib.pyplot as plt
import numpy as np

# Generate values for n
n_values = np.arange(0, 10)

# Calculate the corresponding values for 1/2^n
ratio_values = 1 / (2 ** n_values)

# Plot the graph
plt.plot(n_values, ratio_values, marker='o')
plt.title('Graph of Ratio vs n for r = 2')
plt.xlabel('n')
plt.ylabel('Ratio (1/r^n)')
plt.grid(True)
plt.show()