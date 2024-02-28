import numpy as np
import matplotlib.pyplot as plt

def y(n):
    return (1220 + 1190*n - 30*n**2)

x = np.arange(0,15)

plt.stem(x,y(x),markerfmt='bo', linefmt='b-',label='y(n)')
plt.scatter(11,y(11),color='g',marker='x',s=100,label='y(11)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.xticks(np.arange(0,15,1))
plt.title('Plot of y(n)')
plt.axvline(11, color='r', linestyle='--')
plt.axhline(y(11), color='b', linestyle='--')

plt.legend(loc='upper left')
plt.show()
