import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('values.dat')
n = data[:, 0].astype(int)
xn = data[:, 1]

plt.stem(n, xn)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

