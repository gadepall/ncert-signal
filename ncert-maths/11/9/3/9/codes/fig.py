import numpy as np
import matplotlib.pyplot as plt

# Define the function
def y_n(n, a):
    return (1 - (-a)**(n + 1)) / (1 + a)

# Generate values for n (starting from n=0)
n_values = np.arange(0, 10, 1)  # Adjust the range and step size as needed

# Choose a value for 'a'
a = 0.7  # You can change this value as needed

# Calculate corresponding y values
y_values = y_n(n_values, a)

# Plot the function as a discrete plot
plt.stem(n_values, y_values)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.show()
