import matplotlib.pyplot as plt

# Read values from the generated file
with open('values.txt', 'r') as file:
    values = [int(line.strip()) for line in file]

# Generate x values (n)
n_values = list(range(len(values)))

# Plotting the stem plot
plt.stem(n_values, values, linefmt='b-', markerfmt='bo', basefmt='b-', label='x(n) = 12 + 4n')
plt.stem(n_values[:60], values[:60], linefmt='r-', markerfmt='ro', basefmt='r-', label='n=0 to n=59')

plt.title('Stem Plot of x(n) = 12 + 4n')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()
plt.grid(True)
plt.savefig("graph1.png")
