import matplotlib.pyplot as plt
import numpy as np
# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x_1(n) and x_2(n)
n_values_1 = data[:30, 0]
x_1_values = data[:30, 1]


# Highlight points
highlight_n_1 = 28
highlight_value_1 = 8 + 2 * highlight_n_1
plt.figure(figsize=(4,4))

# Create the first stem plot for x_1(n)
plt.subplot(2, 1, 1)
plt.stem(n_values_1, x_1_values, linefmt='b-', markerfmt='bo', basefmt='r-')

if highlight_value_1 != 0:
    plt.stem(highlight_n_1, highlight_value_1, linefmt='r-', markerfmt='ro', basefmt=' ')
plt.grid(True)    
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('')
plt.tight_layout()
plt.savefig('plot.png')
plt.show()

