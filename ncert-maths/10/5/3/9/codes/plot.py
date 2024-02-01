import matplotlib.pyplot as plt
import numpy as np

def x(n):
        return (1+2*n)
n_values= np.arange(-3, 18, 1)
n_1=np.array([6,16])
#y= np.loadtxt("series.txt", delimiter=" ", max_rows=1)
y=np.heaviside(n_values, 1)*(n_values+1)**2
y_1=np.heaviside(n_1, 1)*(n_1+1)**2

plt.stem(n_values, y, linefmt='-', markerfmt='o', basefmt='r', label=r'$(n+1)^2$')
plt.stem(n_1, y_1, 'pink')
plt.xlabel('n')
plt.ylabel("x(n)")
plt.title("Stem Plot of $y(n)$")
plt.legend()
plt.grid(True)
plt.savefig("Figure_1.png")