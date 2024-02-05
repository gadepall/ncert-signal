import matplotlib.pyplot as plt

# Lists to store data
n_values = []
y_values = []

# Read data from the file
with open("output.txt", "r") as file:
    next(file)  # Skip header line
    for line in file:
        n, y = map(float, line.strip().split())
        n_values.append(n)
        y_values.append(y)

# Define color for stems before and after n=14
colors = ['b' if n < 14 else 'r' for n in n_values]

# Plot using stem plot
plt.stem(n_values, y_values, linefmt='-', markerfmt='o{}'.format('r' if n_values[-1] == 14 else 'b'), basefmt=' ', bottom=0, use_line_collection=True)

# Set x-axis limits and ticks
plt.xlim(-5, 14)
plt.xticks(range(-5, 15))

# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Stem Plot of y(n) vs n')

plt.grid(True)
plt.savefig('fig.png')
plt.show()
