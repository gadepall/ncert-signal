import matplotlib.pyplot as plt

# Lists to store data
n_values = []
x_values = []

# Read data from the file
with open("output_data.txt", "r") as file:
    next(file)  # skip the header line
    for line in file:
        n, x = map(float, line.split())
        n_values.append(int(n))
        x_values.append(x)

# Plotting
plt.stem(n_values, x_values, markerfmt='o', linefmt='-',basefmt='-')
plt.title('x(n) vs n')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.xticks(range(0, 12))  # Set x-axis ticks for values from 0 to 11
plt.grid(True)
plt.savefig('figure__plot.png')
plt.show()
