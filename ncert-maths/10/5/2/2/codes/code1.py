import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x_1(n) and x_2(n)
n_values_1 = data[:33, 0]
x_1_values = data[:33, 1]

n_values_2 = data[34:, 0]
x_2_values = data[34:, 1]

# Highlight points
highlight_n_1 = 29
highlight_value_1 = 10 - 3 * highlight_n_1

highlight_n_2 = 10
highlight_value_2 = -3 + 2.5 * highlight_n_2

# Create the first stem plot for x_1(n)
plt.subplot(2, 1, 1)
plt.stem(n_values_1, x_1_values, linefmt='b-', markerfmt='bo', basefmt='r-')

if highlight_value_1 != 0:
    plt.stem(highlight_n_1, highlight_value_1, linefmt='r-', markerfmt='ro', basefmt=' ')

# Add labels and title for the first plot
plt.xlabel('$n$')
plt.ylabel('$x_1(n)$')
plt.grid(True)

# Create the second stem plot for x_2(n)
plt.subplot(2, 1, 2)
plt.stem(n_values_2, x_2_values, linefmt='b-', markerfmt='bo', basefmt=' ')

plt.stem(highlight_n_2, highlight_value_2, linefmt='r-', markerfmt='ro', basefmt=' ')

# Add labels and title for the second plot
plt.xlabel('$n$')
plt.ylabel('$x_2(n)$')
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig('plot.png')
# Show the combined plot
plt.show()

