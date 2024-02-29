import numpy as np
import matplotlib.pyplot as plt

# Define the function y(n)
def y(n):
    return np.heaviside(n, 0) * (4*3 ** n - 1)

# Read the sequence values from the file
with open("11.9.1-11.txt", "r") as file:
    sequence_values = [int(line.strip()) for line in file][:6]  # Read only the first six values

# Generate the stem plot
n = np.arange(0, 6)  # Define the range of n
plt.stem(n, y(n), use_line_collection=True, label='Simulation', linefmt='b-', markerfmt='bo')
plt.stem(n, sequence_values, use_line_collection=True, label='Theory', linefmt='r-', markerfmt='rx')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Theory vs simulation')
plt.grid(True)
plt.legend()
plt.savefig('11.9.1-11.png')
plt.show()

