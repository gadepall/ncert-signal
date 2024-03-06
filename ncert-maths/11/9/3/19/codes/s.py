import numpy as np
import matplotlib.pyplot as plt

# Read data from .dat file
data = np.loadtxt('yn.dat')

# clear all the previous figures
plt.close("all")

# plot the graph
plt.stem(range(len(data)), data, markerfmt='bo', linefmt='b-', basefmt='r-', label=r'Simulation') 
plt.scatter(range(len(data)), data, color='orange', marker='x', s=100, label=r'Analysis')

# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')

# Set x-axis ticks to correspond to 0, 1, 2, 3, 4
plt.xticks(range(len(data)))

# Add legend
plt.legend()
plt.grid(True)
plt.savefig("fig1.png")

