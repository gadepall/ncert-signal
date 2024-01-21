import matplotlib.pyplot as plt
import numpy as np

# Function to create a constant sequence
def constant_sequence(value, length):
    return [value] * length

# Function to create an arithmetic sequence
def arithmetic_sequence(start, step, length):
    return [start + step * i for i in range(length)]
    


# Create sequences
ap1 = arithmetic_sequence(101, 5, 10)
ap2 = arithmetic_sequence(1, 5, 10)
constant_value = 100
constant_seq = constant_sequence(constant_value, 10)

# Plot for the arithmetic sequences
plt.subplot(2, 1, 1)
plt.plot(ap1, label='$x(n)$: 101, 106, ...')
plt.plot(ap2, label='$y(n)$: 1, 6, ...')
plt.stem(ap1, linefmt=':', markerfmt='o', basefmt=' ')
plt.stem(ap2, linefmt=':', markerfmt='s', basefmt=' ')
plt.ylabel('Values')
plt.title('Stem Plot for $x(n)$ and $y(n)$')
plt.legend().set_visible(False)


# Adjust layout for better spacing
plt.tight_layout()

# Save the plot as a PNG
plt.savefig('fig1.png')

# Show the plot
plt.show()

