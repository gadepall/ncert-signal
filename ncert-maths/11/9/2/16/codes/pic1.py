import matplotlib.pyplot as plt
import numpy as np

loaded = np.transpose(np.loadtxt("pqrs.dat", delimiter=' '))

x = loaded[0]
y = loaded[1]
 
plt.stem(x, y, basefmt='b-', linefmt='d-', markerfmt='ro')
plt.title('General Term of Arithematic Progression')
plt.xlabel('n')
plt.ylabel('Term Value')
plt.grid(1)
plt.show()

