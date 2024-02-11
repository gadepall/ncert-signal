import numpy as np
import matplotlib.pyplot as plt

# Load the data from 'values.dat'
data = np.loadtxt('values.dat')
n = data[:, 0].astype(int)  # n values as integers
xn = data[:, 1]  # x(n) values as floats

# Plotting
plt.stem(n, xn, basefmt=" ")

# Highlight n = 6
index_6 = np.where(n == 6)[0]  # Find the index where n equals 6
if index_6.size > 0:  # Check if n = 6 exists in the data
    plt.stem([n[index_6[0]]], [xn[index_6[0]]], linefmt='C3-', markerfmt='C3o', basefmt=" ")
    # Adjusted offset for the text position to make it closer to the highlighted point
    text_offset = 0.05 * (max(xn) - min(xn))  # Reduced offset to 5% of the range of xn
    # Label the point with n and x(6), making it closer to the point
    plt.text(n[index_6[0]], xn[index_6[0]] + text_offset, f'({n[index_6[0]]}, {xn[index_6[0]]:.2f})', 
             ha='center', va='bottom')
plt.xlabel('n')
plt.ylabel('$x(n)$')
plt.savefig('plot.png', dpi = 300, bbox_inches = 'tight')
