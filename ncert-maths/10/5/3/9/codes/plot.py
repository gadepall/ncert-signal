import matplotlib.pyplot as plt
import numpy as np

n_values= np.arange(-3, 18, 1)
n_1=np.array([6,16])
y= np.loadtxt("series.txt", delimiter=" ", max_rows=1)
y_1= [y[i+3] for i in (n_1)]

plt.stem(n_values, y, linefmt='-', markerfmt='o', basefmt='r', label=r'$(n+1)^2$')
plt.stem(n_1, y_1, 'pink')
plt.xlabel('n')
plt.ylabel("x(n)")
plt.title("Stem Plot of $y(n)$")
plt.legend()
plt.grid(True)
plt.savefig("Figure_1.png")