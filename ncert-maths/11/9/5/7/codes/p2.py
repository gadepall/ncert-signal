import matplotlib.pyplot as plt

# Read data from the C-generated file
with open('gp_sum_data.txt', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]

# Extract n and sum values
n_values, sum_values = zip(*data)

# Plot stem plot for the sum of the first n terms of the GP
plt.stem(n_values, sum_values, linefmt='b-', markerfmt='bo', basefmt='r-', label='Sum of GP')

plt.title('Stem Plot for Sum of First n Terms of Geometric Progression')
plt.xlabel('n')
plt.ylabel('y(n)')

plt.legend()
plt.grid(True)
plt.savefig('i2.png')
plt.show()

