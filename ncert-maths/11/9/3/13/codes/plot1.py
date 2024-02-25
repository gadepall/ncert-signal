import matplotlib.pyplot as plt
import numpy as np

data=np.loadtxt("terms.txt", skiprows=1)

plt.close("all")

n=data[:5,0]
x_n=data[:5,1]


plt.stem(n, x_n, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.axhline(y=243, color='green', linestyle='--',label='y=243')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.xticks(n)


plt.legend()
plt.grid(True)
plt.savefig("figure_plot.png")
plt.show()