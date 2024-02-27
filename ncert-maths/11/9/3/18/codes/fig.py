import matplotlib.pyplot as plt
import numpy as np
# Read data from the .dat file with space as the delimiter, skip lines starting with 'Values'
data = np.loadtxt('values.dat', delimiter=' ', comments='Values')

# Extracting values for x_1(n) and x_2(n)
n_values_1 = data[:7, 0]
x_1_values = data[:7, 1]


plt.figure(figsize=(4,4))
# Create the first stem plot for x_1(n)
plt.subplot(2, 1, 1)
plt.stem(n_values_1, x_1_values, linefmt='b-', markerfmt='bo', basefmt='r-')


plt.grid(True)    
plt.xlabel('n')
plt.ylabel('s(n)')
plt.title('')
plt.tight_layout()
plt.savefig('plot.png')
plt.show()

