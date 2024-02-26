import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x_1(n), x_2(n), x_3(n), x_4(n), and x_5(n)
n_values = data[:, 0]
x_1_values = data[:, 1]
x_2_values = data[:, 2]
x_3_values = data[:, 3]
x_4_values = data[:, 4]
x_5_values = data[:, 5]

# Create the stem plots for x_1(n), x_2(n), x_3(n), x_4(n), and x_5(n)
plt.subplot(3, 2, 1)
plt.stem(n_values, x_1_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_1(n)$')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.stem(n_values, x_2_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_2(n)$')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.stem(n_values, x_3_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_3(n)$')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.stem(n_values, x_4_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_4(n)$')
plt.grid(True)

plt.subplot(3, 2, 5)
plt.stem(n_values, x_5_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('$x_5(n)$')
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig('plot_modified.png')
# Show the combined plot
plt.show()

