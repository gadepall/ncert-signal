import numpy as np
import matplotlib.pyplot as plt

# Load data from the output.dat file
file_path_y = 'output.dat'

def y(n):
    return np.where(n < 0, 0, np.loadtxt(file_path_y))

# Generate n values from -2 to 10
n = np.arange(-2, 11)

# Plot the graph for y(n)
plt.stem(n, y(n), markerfmt='o', linefmt='b-', basefmt='r-')

# Highlight specific points with different colors in y(n)
highlighted_points = [3, 6, 10]
highlighted_colors = ['r', 'g', 'b']  # Different colors for y(3), y(6), y(10)

for point, color in zip(highlighted_points, highlighted_colors):
    plt.plot(point, y(n)[n == point], marker='o', markersize=8, color=color, linestyle='None', label=f'y({point})')

plt.title('Terms of y(n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()
plt.savefig('fig1.png')
plt.close()

