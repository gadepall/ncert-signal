import matplotlib.pyplot as plt
import numpy as np

data=np.loadtxt("data.txt", skiprows=1)

plt.close("all")

n=data[:5,0]
s_n=data[:5,2]


plt.stem(n, s_n, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.axhline(y=363, color='green', linestyle='--',label='y=363')
plt.xlabel('$n$')
plt.ylabel('$s(n)$')
plt.xticks(n)


plt.legend()
plt.grid(True)
plt.savefig("figure_plot.png")
plt.show()