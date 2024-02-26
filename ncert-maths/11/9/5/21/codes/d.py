import matplotlib.pyplot as plt
import numpy as np

# Load data for the first sequence
data_stem1 = np.loadtxt('theory1.dat')
data_scatter1 = np.loadtxt('simuate1.dat')

# Plot stem plot for the first sequence
plt.figure(1)

plt.stem(data_stem1, linefmt='b-', markerfmt='bo', basefmt='r')
plt.scatter(np.arange(len(data_scatter1)), data_scatter1, color='red', s=75)

plt.xlabel('n')
plt.ylabel('$s_1(n)$')
plt.savefig('data_x1.png', dpi=300, bbox_inches='tight')

# Load data for the second sequence
data_stem2 = np.loadtxt('theory2.dat')
data_scatter2 = np.loadtxt('simuate2.dat')

# Plot stem plot for the second sequence
plt.figure(2)

plt.stem(data_stem2, linefmt='b-', markerfmt='bo', basefmt='r')
plt.scatter(np.arange(len(data_scatter2)), data_scatter2, color='red', s=75)

plt.xlabel('n')
plt.ylabel('$s_2(n)$')
plt.savefig('data_x2.png', dpi=300, bbox_inches='tight')
