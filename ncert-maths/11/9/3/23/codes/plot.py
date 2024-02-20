import matplotlib.pyplot as plt
import numpy as np

# Read data from the "output.dat" file
data = np.loadtxt("output.dat")

# Separate columns into n and 5.2^(n-1)
n_values = data[:, 0]
y_values = data[:, 1]

# Plotting as discrete points
plt.stem(n_values, y_values, markerfmt='bo', linefmt='b-', basefmt='r-')
#plt.title('Discrete Plot of x(n) vs n')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

