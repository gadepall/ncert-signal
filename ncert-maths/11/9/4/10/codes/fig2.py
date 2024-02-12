import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Read data from the "output.dat" file
data = np.loadtxt("output.dat")

# Extract n, y, and Simulation from the data
n = data[:, 0]
y = data[:, 2]
Simulation = data[:, 3]

# Set the figure size
plt.figure(figsize=(6, 4))  # Adjust width and height as needed

# Plot for y(n) and Simulation
plt.stem(n, y, linefmt='r-', markerfmt='rx', basefmt='r-', label=r'$y(n)$')
plt.stem(n, Simulation, linefmt='g-', markerfmt='go', basefmt='g-', label='Simulation')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.setp(plt.gca().lines[0], markersize=8)  
plt.setp(plt.gca().lines[1], markersize=12) 
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('../figs/fig2.png')
plt.show()

