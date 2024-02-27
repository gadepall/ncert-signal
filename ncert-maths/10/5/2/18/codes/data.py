import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.dat")

n_values = data[:, 0].astype(int)
x_values = data[:, 1].astype(int)

# Creating a stem plot
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='b-', label='Stem Plot')

# Highlighting the first three elements as per the question
plt.stem(n_values[:3], x_values[:3], linefmt='r-', markerfmt='ro', basefmt='r-')

plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.legend()

plt.savefig('../figs/fig1.png')

