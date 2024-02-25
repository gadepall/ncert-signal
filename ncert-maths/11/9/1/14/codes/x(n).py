import numpy as np
import matplotlib.pyplot as plt

#Defining function x(n)
def x(n):
    return ((1 + np.sqrt(5))**(n + 1) - (1 - np.sqrt(5))**(n + 1)) / (2**(n + 1) * np.sqrt(5))

#Setting values of n
n = np.arange(0,7,1)

#Calculating the value of the function
y = x(n)

#Plotting a stem graph
plt.stem(n, y, markerfmt='bo', linefmt='b-')
plt.xlabel('n')
plt.xticks(np.arange(0,7,1))
plt.yticks((np.arange(0,15,1)))
plt.ylabel('x(n)')
plt.title('Plot of x(n)')
plt.grid(True)
plt.show()
