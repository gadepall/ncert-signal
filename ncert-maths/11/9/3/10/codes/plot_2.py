import matplotlib.pyplot as plt
import numpy as np
#import os
n_values = np.arange(0,10)
x=1.2
y_values = x ** (2*n_values+3)
fig,ax = plt.subplots()
ax.stem(n_values,y_values,label=f'x={x}')
ax.set(xlim=(-1,10), xticks=np.arange(0,10),ylim=(0,50),yticks=np.arange(0,50,5))
plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()
plt.grid(True)
plt.savefig('../figs/plot_2.png')
#os.system('open ../figs/plot_2.png')
