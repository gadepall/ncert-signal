import numpy as np
import matplotlib.pyplot as plt

# Load data from the generated .txt file
n_values_discrete = np.arange(-3,20)
y_values_discrete = np.loadtxt("data.txt", delimiter=' ')

# Plot the data
plt.stem(n_values_discrete, y_values_discrete, label="x(n) = 2 - 6n")
plt.stem([19],[-112], 'mo',basefmt='k', label='$x_1(k_1)$' )
plt.xlabel("n")
plt.ylabel("x(n)")
plt.title("Plot of x(n)")
plt.grid(1)
plt.savefig('Figure_1.png')
