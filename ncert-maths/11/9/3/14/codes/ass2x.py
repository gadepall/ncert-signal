import numpy as np
import matplotlib.pyplot as plt

try:
    # Load data from datax.dat file
    data = np.loadtxt('datax.dat')

    # Extract n and x(n) values
    n_values = data[:, 0]
    x_values = data[:, 1]

    # Plot x(n)
    plt.stem(n_values, x_values, linefmt='r-', markerfmt='ro', basefmt='b-')

    # Set labels and title
    plt.xlabel('$n$')
    plt.ylabel('$x(n)$')
    plt.title('Plot of $x(n)$')
    plt.grid(True)

    # Show plot
    plt.savefig('plotx.png')
    plt.show()

except FileNotFoundError:
    print("Error: datax.dat file not found.")

