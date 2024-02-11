import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('data1.txt')
data2 = np.loadtxt('data2.txt')
data3 = np.loadtxt('data3.txt')

y_values_1 = np.cumsum(data1)  
y_values_2 = np.cumsum(data2)  
y_values_3 = np.cumsum(data3)  

y_1_22 = y_values_1[22]
y_2_12 = y_values_2[12]
y_3_75 = y_values_3[75]

plt.stem(np.arange(len(data1)), y_values_1, basefmt=" ", label='y_1(n)')
plt.stem(22, y_1_22, linefmt='r', markerfmt='ro', label=f'y_1(22)={y_1_22}')
plt.xlabel('n')
plt.ylabel('y_1(n)')
plt.legend()
plt.show()

plt.stem(np.arange(len(data2)), y_values_2, basefmt=" ", label='y_2(n)')
plt.stem(12, y_2_12, linefmt='r', markerfmt='ro', label=f'y_2(12)={y_2_12}')
plt.xlabel('n')
plt.ylabel('y_2(n)')
plt.legend()
plt.show()

plt.stem(np.arange(len(data3)), y_values_3, basefmt=" ", label='y_3(n)')
plt.stem(75, y_3_75, linefmt='r', markerfmt='ro', label=f'y_3(75)={y_3_75}')
plt.xlabel('n')
plt.ylabel('y_3(n)')
plt.legend()
plt.show()

