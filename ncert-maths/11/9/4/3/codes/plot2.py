import numpy as np
import matplotlib.pyplot as plt
c = np.loadtxt("values2.dat", delimiter='\t')


plt.stem(c[:, 0], c[:, 1])
plt.scatter(c[:, 0], c[:, 2],s=100, marker='x', color="black", label = r'simulation')
plt.scatter(c[:, 0], c[:, 2],s=100, marker='.', color="blue", label = r'analysis')
plt.grid(1)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.legend()
plt.savefig('fig_1.jpg')
