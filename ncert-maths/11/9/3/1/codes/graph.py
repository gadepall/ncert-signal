import matplotlib.pyplot as plt
import numpy as np

# Read x(n) values from the file
n_values, x_values = np.loadtxt('output.txt', unpack=True)

# Plotting
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r-', label='x(n)')
#plt.title('Plot of x(n) vs n', fontsize=16)
plt.xlabel('n', fontsize=16)
plt.ylabel('x(n)', fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid(True)
plt.legend(fontsize=16)
plt.savefig('stem_plot.png', dpi=600)
plt.show()
