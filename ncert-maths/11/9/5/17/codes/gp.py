import numpy as np
import matplotlib.pyplot as plt

# Load data for the first plot
data1 = np.loadtxt("coordinate1.txt")

# Extract x and y values for the first plot
x1 = data1[:, 0]
y1 = data1[:, 1]

# Load data for the second plot
data2 = np.loadtxt("coordinate2.txt")

# Extract x and y values for the second plot
x2 = np.arange(0, 5)
y2 = data2

# Plot the first subplot
plt.figure(1)
plt.stem(x1, y1, basefmt='k-', linefmt='r-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)

# Plot the second subplot
plt.figure(2)
plt.stem(x2, y2, linefmt='r-', markerfmt='ro', basefmt='r-')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)

# Display the plots
plt.show()

