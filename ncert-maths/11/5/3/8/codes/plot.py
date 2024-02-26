import numpy as np
import matplotlib.pyplot as plt

# Specify the line number to start reading from
start_line = 16  # Adjust this line number as per your requirement

# Read data from the text file, skipping the specified number of lines
data = np.loadtxt("output.dat",skiprows=1)

# Separate y and x values
x_values = data[:, 0]
y_values = data[:, 1]




highlight_index = 50
plt.scatter(x_values[highlight_index], y_values[highlight_index], color='red', marker='x', s=100, label='y(50)(Analysis)')
plt.stem(x_values, y_values, markerfmt='bo', linefmt='b-', basefmt='r-',label='y(n)(Simulation)') 
plt.axhline(y=5610, color='green', linestyle='--',label='(y=5610)')
# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')


# Add legend
plt.legend()

plt.savefig('../figs/plot.png')

