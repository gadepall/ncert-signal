import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('data1.txt')

x_values = data1[:5]

highlight_indices = np.arange(4)
plt.stem(range(5), x_values, basefmt=" ", label='x(n)')
plt.stem(highlight_indices, x_values[highlight_indices], linefmt='r', markerfmt='ro', label='First 4 terms of GP')

x_0 = 3
r = -2
n_range = np.arange(0, 6) 

x_values = x_0 * (r ** n_range) * (n_range >= 0)

plt.stem(n_range, x_values, linefmt='C0-', markerfmt='C0o', basefmt=" ")

highlight_indices = [0, 1, 2, 3]
highlight_values = x_0 * (r ** np.array(highlight_indices))
plt.stem(highlight_indices, highlight_values, linefmt='r-', markerfmt='ro')

plt.xlabel('n')  
plt.ylabel('x(n)')  
plt.xlim(-1, 6)  
plt.ylim(min(x_values) - 0.5, max(x_values) + 0.5)  

plt.grid(True)  
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5)  

plt.legend()
plt.show()

