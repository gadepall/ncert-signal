import matplotlib.pyplot as plt

# Read data from file
with open('data.txt', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]

# Extract n and x(n) values
n_values, x_values = zip(*data)

# Plot stem plot for x(n)
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r-', label='x(n)')

# Mark x(n) = 3 in green color
plt.axhline(y=3, color='g', linestyle='--', label='x(n) = 3')

plt.title('Stem Plot for x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')

plt.legend()
plt.grid(True)
plt.savefig('i1.png')
plt.show()

