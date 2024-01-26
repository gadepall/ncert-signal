import matplotlib.pyplot as plt
import numpy as np

a = 1.5  
r = 2.0
start = 0
end = 12
x_1 = 7
y_1 = 192
x_2 = 11
y_2 = 3072

n_values = np.arange(start, end + 1).astype(np.float32)
gp_values = np.loadtxt('data.txt', delimiter=' ')
plt.stem(n_values, gp_values, basefmt='b-', linefmt='d-', markerfmt='ro')
plt.stem([7], [192], 'mo', basefmt='k', label='$x_1(k_1)$')
plt.stem([11], [3072], 'mo', basefmt='k', label='$x_1(k_1)$')
plt.title('General Term of Geometric Progression')
plt.xlabel('n')
plt.ylabel('Term Value')
plt.grid(True)
plt.show()

