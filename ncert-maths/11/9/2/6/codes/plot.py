import matplotlib.pyplot as plt
import numpy as np

def x_n(n):
    return (25 - 3 * n) * (n >= 0)

n_values = np.arange(0, 10, 1)
x_values = x_n(n_values)

plt.stem(n_values, x_values, basefmt="b-", linefmt="b-", markerfmt="bo")
plt.stem(7, x_n(7), linefmt="r-", markerfmt="ro", label="n = 7")
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.title('Stem Plot of $x(n) = (25 - 3n)u(n)$')
plt.legend()
plt.grid(True)

# Save the plot as a PDF file
plt.savefig('stem_plot.pdf', format='pdf')

# Show the plot
plt.show()

