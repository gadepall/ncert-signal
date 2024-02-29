import numpy as np
import matplotlib.pyplot as plt

# Define the grid
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x, y)

# Electric field vector (E) in the x-direction
Ex = np.ones_like(X)
Ey = np.zeros_like(Y)

# Magnetic field vector (B) in the y-direction
Bx = np.zeros_like(X)
By = np.ones_like(Y)

# Plotting
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, Ex, Ey, scale=2, color='r', label='Electric Field (E)')
plt.quiver(X, Y, Bx, By, scale=2, color='b', label='Magnetic Field (B)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Electric and Magnetic Fields Perpendicular to Each Other')
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()
