import numpy as np
import matplotlib.pyplot as plt

# Load data from the values.dat file
file_path_y = 'values.dat'

# Define the y_n function to load values from the file
def y_n(n):
    return np.loadtxt(file_path_y)[max(0, n):min(n + 1, len(np.loadtxt(file_path_y)))]

# Generate n values from 0 to 48
n_values = np.arange(0, 49)
y_values = np.array([y_n(n) for n in n_values])

# Plot the graph for y(n)
stem = plt.stem(n_values, y_values, markerfmt='o', linefmt='b-', basefmt='r-')

highlighted_points = [34]
highlighted_colors = ['r']  
for point, color in zip(highlighted_points, highlighted_colors):
    plt.plot(point, y_values[n_values == point], marker='o', markersize=8, color=color, linestyle='None', label=f'y({point})')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()
plt.savefig('fig1.png')
plt.show()