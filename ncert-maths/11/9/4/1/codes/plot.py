import numpy as np
import matplotlib.pyplot as plt
data1 = np.loadtxt("simulation_values.dat", skiprows=1)
data2=np.loadtxt("analysis_values.dat",skiprows=1)
plt.close("all")
n1 = data1[:10, 0]
y_n1= data1[:10, 2]
n2=data2[:10, 0]
y_n2=data2[:10, 2]
# plot the graph
plt.stem(n1, y_n1,markerfmt='D', label='Simulation')
plt.stem(n2, y_n2, label='Analysis', linefmt='r--', markerfmt='x', basefmt=' ')
# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.legend()
plt.grid(True)
plt.savefig("Graph.png")
plt.show()
