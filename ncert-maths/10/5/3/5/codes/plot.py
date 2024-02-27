import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x(n)
n_values_1 = data[:16, 0]
x_1_values = data[:16, 1]



# Create the first stem plot for x(n)
plt.subplot(2, 1, 1)
plt.stem(n_values_1, x_1_values, linefmt='b-', markerfmt='bo', basefmt='r-')


# Add labels and title for the first plot
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid(True)
# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig('plot.png')
# Show the combined plot
plt.show()
