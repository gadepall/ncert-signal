import numpy as np
import matplotlib.pyplot as plt

# Define the function y(n) = (n(n+1))/2
def y1(n):
    return (n * (n + 1)) / 2

# Define the function y(n) = (n(n+1)(2n+1))/6
def y2(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

# Define the function y(n) = ((n(n+1))/2)^2
def y3(n):
    return ((n * (n + 1)) / 2) ** 2

# Generate a range of n values
n_values = np.arange(0, 10)

# Calculate the theoretical values for y(n)
y1_theo = y1(n_values)
y2_theo = y2(n_values)
y3_theo = y3(n_values)

# Simulate the functions using the step function
y1_sim = np.cumsum(n_values)
y2_sim = np.cumsum(n_values * n_values)
y3_sim = np.cumsum(n_values * n_values * n_values)

# Plot the simulation versus theory for y1(n)
plt.stem(n_values, y1_theo, label='Theory for y1(n)', linefmt=':', markerfmt='o', basefmt='b')
plt.stem(n_values, y1_sim, label='Simulation for y1(n)', linefmt='-', markerfmt='s', basefmt='r')

plt.xlabel('n')
plt.ylabel('y1(n)')
plt.legend()
plt.grid(True)
plt.savefig('y_1(n).png')
plt.show()

# Plot the simulation versus theory for y2(n)
plt.stem(n_values, y2_theo, label='Theory for y2(n)', linefmt=':', markerfmt='o', basefmt='b')
plt.stem(n_values, y2_sim, label='Simulation for y2(n)', linefmt='-', markerfmt='s', basefmt='r')

plt.xlabel('n')
plt.ylabel('y2(n)')
plt.legend()
plt.grid(True)
plt.savefig('y_2(n).png')
plt.show()

# Plot the simulation versus theory for y3(n)
plt.stem(n_values, y3_theo, label='Theory for y3(n)', linefmt=':', markerfmt='o', basefmt='b')
plt.stem(n_values, y3_sim, label='Simulation for y3(n)', linefmt='-', markerfmt='s', basefmt='r')

plt.xlabel('n')
plt.ylabel('y3(n)')
plt.legend()
plt.grid(True)
plt.savefig('y_3(n).png')
plt.show()

