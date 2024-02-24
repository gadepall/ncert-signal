import numpy as np
import matplotlib.pyplot as plt

# Load data from values.dat
data = np.loadtxt('values.dat')
x = data[:, 0]
y = data[:, 1]

# Plot for values.dat and save
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x)')
plt.grid(True)
plt.savefig('f1.png')  # Save the plot
plt.close()  # Close the current figure

# Load data from values1.dat
data = np.loadtxt('values1.dat')
n = data[:, 0].astype(int)
xn = data[:, 1]

# Plot for values1.dat and save
plt.figure(figsize=(8, 6))
plt.stem(n, xn)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem plot of AP series')
plt.grid(True)
plt.savefig('ap.png')  # Save the plot
plt.close()  # Close the current figure

# Load data from values2.dat
data = np.loadtxt('values2.dat')
n = data[:, 0].astype(int)
xn = data[:, 1]

# Plot for values2.dat and save
plt.figure(figsize=(8, 6))
plt.stem(n, xn)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem plot of GP series')
plt.grid(True)
plt.savefig('gp.png')  # Save the plot
plt.close()  # Close the current figure

