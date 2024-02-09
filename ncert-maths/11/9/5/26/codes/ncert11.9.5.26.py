import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.loadtxt("output_data.txt")

n_values = data[:, 0]


plt.close('all')
# Plot 1
plt.stem(n_values, data[:, 1], label=r'$(n+1)(n +2)^2$')
plt.legend()
plt.xlabel("n")
plt.ylabel("x_1(n)")
plt.title("Stem plot of x_1(n)")
plt.savefig("x1_plot.png")
plt.clf()  # Clear the figure

# Plot 2
plt.stem(n_values, data[:, 2], label=r'$(n+1)^2(n +2)$')
plt.legend()
plt.xlabel("n")
plt.ylabel("x_2(n)")
plt.title("Stem plot of x_2(n)")
plt.savefig("x2_plot.png")
plt.clf()

# Plot 3
plt.stem(n_values, data[:, 3], label=r'$\frac{3n^4+26n^3+81n^2+106n+48}{12}$')
plt.legend()
plt.xlabel("n")
plt.ylabel("y_1(n)")
plt.title("Stem plot of y_1(n)")
plt.savefig("y1_plot.png")
plt.clf()

# Plot 4
plt.stem(n_values, data[:, 4], label=r'$\frac{3n^4+22n^3+57n^2+62n+24}{12}$')
plt.legend()
plt.xlabel("n")
plt.ylabel("y_2(n)")
plt.title("Stem plot of y_2(n)")
plt.savefig("y2_plot.png")
plt.clf()
