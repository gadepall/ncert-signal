import numpy as np
import matplotlib.pyplot as plt
data1 = np.loadtxt("values.dat", skiprows=1)
n1 = data1[:10, 0]
x_n1= data1[:10, 1]
plt.stem(n1, x_n1)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig("Graphimage.png")
plt.show()
