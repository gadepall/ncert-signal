import numpy as np
import matplotlib.pyplot as plt

#Defining function y(n)
def y(n):
    return ((1 + np.sqrt(5))**(n + 2) - (1 - np.sqrt(5))**(n + 2)) / (2 * ((1 + np.sqrt(5))**(n + 1) - (1 - np.sqrt(5))**(n + 1)))

#Setting values of n
n = np.arange(0,7,1)

#Calculating the value of the function
h = y(n)

#Plotting a stem graph
plt.stem(n, h, markerfmt='bo', linefmt='b-')
plt.xlabel('n')
plt.xticks(np.arange(0,7,1))
plt.yticks((np.arange(0,5,1)))
plt.ylabel('y(n)')
plt.title('Plot of y(n)')
plt.grid(True)
plt.show()
