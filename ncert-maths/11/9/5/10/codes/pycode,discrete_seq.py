import matplotlib.pyplot as plt

# Function to read values from file and return as list
def read_values(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        values = [float(line.strip()) for line in lines]
    return values

# Read values from files
values_py1 = read_values('py_1.txt')
values_py2 = read_values('py_2.txt')

# Generate corresponding m and n values
a = len(values_py1) - 1
b = len(values_py2) - 1
m_values = list(range(a + 1))
n_values = list(range(b + 1))

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1)

# Plot the first graph
ax1.stem(m_values, values_py1, label='2^(m+3)')
ax1.set_xlabel('m')
ax1.set_ylabel('x_1(m)')
ax1.legend()
ax1.grid(True)

# Plot the second graph
ax2.stem(n_values, values_py2, label='2^(5-n)')
ax2.set_xlabel('n')
ax2.set_ylabel('x_2(n)')
ax2.legend()
ax2.grid(True)

# Adjust layout
plt.tight_layout()

# Save the plot to a PNG file
plt.savefig('figure.png')

# Display the plot
plt.show()
