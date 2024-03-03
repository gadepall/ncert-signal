import numpy as np
import matplotlib.pyplot as plt

try:
    # Load data for x(n)
    data_x = np.loadtxt('datax.dat')
    n_values_x = data_x[:, 0]
    x_values = data_x[:, 1]

    # Load data for y(n)
    data_y = np.loadtxt('data.dat')
    n_values_y = data_y[:, 0]
    y_values = data_y[:, 1]

    # Plot x(n)
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)
    plt.stem(n_values_x, x_values, linefmt='r-', markerfmt='ro', basefmt='b-')
    plt.xlabel('$n$')
    plt.ylabel('$x(n)$')
    plt.title('Plot of $x(n)$')
    plt.grid(True)

    # Plot y(n)
    plt.subplot(2, 1, 2)
    plt.stem(n_values_y, y_values, linefmt='g-', markerfmt='go', basefmt='b-')
    plt.xlabel('$n$')
    plt.ylabel('$y(n)$')
    plt.title('Plot of $y(n)$')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('plot_xy.png')
    plt.show()

except FileNotFoundError:
    print("Error: One or both data files not found.")

