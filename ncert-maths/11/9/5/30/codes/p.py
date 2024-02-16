import numpy as np
import matplotlib.pyplot as plt

n_values_discrete = np.arange(-3,21)
y_values_discrete = np.loadtxt("data2.txt", delimiter=' ')

plt.stem(n_values_discrete, y_values_discrete, linefmt='b-', markerfmt='bo')
plt.stem([14],[17000], 'ro', markerfmt='ro', basefmt='r')
plt.stem([20],[20000], 'ro', markerfmt='ro', basefmt='r')
plt.xlabel("n")
plt.ylabel("x(n)")
plt.title("x(n)=10000+500n")
plt.grid(True)
plt.savefig('p.jpeg')

