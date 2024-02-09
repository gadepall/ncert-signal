import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('data3.dat')

x_values, y_values = data[:, 0], data[:, 1]

# Plot the graph
plt.stem(x_values, y_values)
plt.xlabel('n',fontsize=14)
plt.ylabel('y(n)',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True)
plt.savefig('sumplot.png',dpi=600)
plt.show()

