import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('Values.txt')
x_values = data[:,0]

y_values = data[:,1]
y_calcu_values = data[:,2]

plt.stem(x_values, y_values, label=r'Theory')
plt.scatter(x_values, y_calcu_values, marker = 'X',s=100, color = 'red', label = r'Simulation')
plt.xlabel('n')
plt.ylabel('y(n)')

#plt.axhline(0, color='black',linewidth=0.5)
#plt.axvline(0, color='black',linewidth=0.5)

plt.grid(True)
plt.savefig('y(n)_vs_n.png')

