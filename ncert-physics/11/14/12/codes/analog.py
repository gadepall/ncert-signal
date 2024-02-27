import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def func1(t):
    return -2 * np.sin(3 * t + np.pi / 3)

def func2(t):
    return np.cos(np.pi / 6 - t)

def func3(t):
    return 3 * np.sin(2 * np.pi * t + np.pi / 4)

def func4(t):
    return 2 * np.cos(np.pi * t)

# Define the time range
t = np.linspace(0, 2*np.pi, 1000)

# Plotting Function 1
#plt.figure(figsize=(8, 6))
plt.plot(t, func1(t),label=r'$x = -2 \sin(3t + \frac{\pi}{3})$')
#plt.title('Function 1')
plt.xlabel('t',fontsize=16)
plt.ylabel('x',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid(True)
plt.legend()
plt.savefig('Figure_1.png',dpi=600)
plt.clf()

# Plotting Function 2
#plt.figure(figsize=(8, 6))
plt.plot(t, func2(t),label=r'$x = \cos(\frac{\pi}{6} - t)$')
#plt.title('Function 2')
plt.xlabel('t',fontsize=600)
plt.ylabel('x',fontsize=600)
plt.xticks(fontsize=16)
plt.yticks(fontsize = 16)
plt.grid(True)
plt.legend()
plt.savefig('Figure_2.png',dpi=600)
plt.clf()

# Plotting Function 3
#plt.figure(figsize=(8, 6))
plt.plot(t, func3(t), label=r'$x = 3 \sin(2\pi t + \frac{\pi}{4})$')
#plt.title('Function 3')
plt.xlabel('t',fontsize=16)
plt.ylabel('x',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid(True)
plt.legend()
plt.savefig('Figure_3.png',dpi=600)
plt.clf()

# Plotting Function 4
#plt.figure(figsize=(8, 6))
plt.plot(t, func4(t),label=r'$x = 2 \cos(\pi t)$')
#plt.title('Function 4')
plt.xlabel('t',fontsize=14)
plt.ylabel('x',fontsize=14)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid(True)
plt.legend()
plt.savefig('Figure_4.png',dpi=600)
plt.clf()
