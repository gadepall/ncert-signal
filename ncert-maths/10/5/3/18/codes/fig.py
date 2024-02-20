import numpy as np
import matplotlib.pyplot as plt
c = np.loadtxt("data.dat", delimiter='\t')


plt.stem(c[:, 0], c[:, 1])
plt.stem([12], [45.5], 'ro', basefmt='k', label=r'theory')
plt.scatter(c[:, 0], c[:, 2],s=100, marker='x', color="black", label = r'simulation')
plt.title("Plot of y(n) function")
plt.grid(1)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.legend()
plt.savefig('fig_1.jpg')





