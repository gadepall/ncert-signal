import os
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("output.dat")

n_values = data[:, 0].astype(int)
y_values = data[:, 1].astype(int)

plt.plot(n_values, y_values, marker='o', linestyle='-', color='b', label='Line Plot')

plt.stem(n_values, y_values, linefmt=':', markerfmt='r^', basefmt='b', label='Stem Plot')

plt.xlabel('n')
plt.ylabel('S(n)')

plt.grid(True)
plt.legend()

save_path = 'figs/python.1(1).png'
plt.savefig(save_path)
plt.show()

