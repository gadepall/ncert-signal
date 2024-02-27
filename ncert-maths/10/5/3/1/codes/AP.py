import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Define the parameters of the AP

# Load data from the .dat files
data_ap = np.loadtxt('dat_files/AP/ap4_data.dat', skiprows=1)  # Skip the header row
data_sum = np.loadtxt('dat_files/SUM/ap4_sum.dat', skiprows=1)

# Separate the columns into n_values and y_values for AP data
n_values_ap = data_ap[:, 0]
y_values_ap = data_ap[:, 1]

# Separate the columns into n_values and y_values for sum data
n_values_sum = data_sum[:, 0]
y_values_sum = data_sum[:, 1]

xo = data_ap[0,1]  # Example initial term
d = data_ap[1,1] - data_ap[0,1]  # Example common difference
T = data_ap[-1,0] + 1  # Generate AP up to 100 terms
print(xo, d, T)

# Define the unit step function
def u(n):
    return np.where(n >= 0, 1, 0)
    
# Define the sequence {xo+nd}u(n)
def sequence_x(n):
    return (xo + d*n) * u(n)

# Generate the arithmetic progression sequence up to 10 terms
n = np.arange(0, 1000)
x = sequence_x(n)
h = u(n)

# Simulate the sum of the AP by convolving u(n) with only the terms up to n=10
simulated_sum = convolve(u(n), x)

# Calculate the actual sum of the AP for the first 10 terms
# actual_sum = (n + 1) * (2 * xo + n * d) / 2

# Plot the simulated result and the actual sum
fig, axs = plt.subplots(2, 1, figsize=(8, 8))

# Plot AP data
axs[0].stem(n_values_ap, y_values_ap, linefmt='c-', markerfmt='co', basefmt='r-')
axs[0].set_xlabel('n')
axs[0].set_ylabel('x(n)')

# Plot sum data
axs[1].scatter(np.arange(0, int(T)), simulated_sum[0:int(T)], marker='x', color='red', label='Simulation')
axs[1].stem(n_values_sum[0:int(T)], y_values_sum[0:int(T)], linefmt='b', markerfmt='', label='Analysis')
axs[1].scatter(n_values_sum[-1], y_values_sum[-1], color='orange', zorder=3)
axs[1].set_xlabel('n')
axs[1].set_ylabel('y(n)')

plt.tight_layout()
plt.legend()
plt.grid(True)
plt.show()

