import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt("output_data.txt", skiprows=1)

# Extract columns
n = data[:, 0]
x_n = data[:, 1]
y_n = data[:, 2]

# Plotting with adjusted marker size and different colors for better visibility
plt.stem(n, y_n, linefmt='r-', markerfmt='ro', basefmt='r-', label=r'Simulation')
plt.scatter(n, x_n, color='green',marker='x',s=100, label=r'Theory')
plt.xlabel('n')
plt.ylabel('Function Values')
plt.title('Stem Plot of Theory and Simulation')
plt.legend()
plt.savefig("Theory_vs_Simulation")
