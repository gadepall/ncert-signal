import numpy as np
import matplotlib.pyplot as plt


n_values=np.arange(-3,11)
y1=np.loadtxt("series.dat", delimiter=" ", max_rows=1)
y2=np.loadtxt("series.dat", delimiter=" ", skiprows=1)
plt.stem(n_values,y1, markerfmt="bo", basefmt='r', label=r'Theory')
plt.scatter(n_values,y2, marker='x',s=100,color="red", label=r'Simulation')
plt.xlabel('n')
plt.ylabel("y(n)")
plt.legend()
plt.grid(True)
plt.savefig('../figs/Figure_1.png')