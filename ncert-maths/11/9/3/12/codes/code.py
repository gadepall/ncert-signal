import matplotlib.pyplot as plt
import numpy as np

# Read data from the '11.dat' file
with open('11.dat', 'r') as file:
    data_str = file.read()

# Split the data into two sequences
sequences = data_str.split('\n')

# Remove the empty string at the end
sequences = [line for line in sequences if line]

# Extract data using NumPy arrays
data_array = np.array([list(map(float, line.split('\t'))) for line in sequences])

# Separate data into arrays
x_values = data_array[:, 0].astype(int)
seq1 = data_array[:, 1]
seq2 = data_array[:, 2]

# Plotting Sequence 1
plt.figure()
plt.stem(x_values, seq1, markerfmt='ro', linefmt='r-', basefmt='k-')
plt.xlabel('n')
plt.ylabel('x(n)')

# Set x-axis ticks to integers
plt.xticks(x_values)

# Save the figure as 'graph1.png'
plt.savefig('graph1.png')
plt.show()

# Plotting Sequence 2
plt.figure()
plt.stem(x_values, seq2, markerfmt='bs', linefmt='b-', basefmt='k-')
plt.xlabel('n')
plt.ylabel('x(n)')

# Set x-axis ticks to integers
plt.xticks(x_values)

# Save the figure as 'graph2.png'
plt.savefig('graph2.png')
plt.show()

