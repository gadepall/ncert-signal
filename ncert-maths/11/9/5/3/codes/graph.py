import matplotlib.pyplot as plt

# Read data points from the file
n_values = []
y_values = []

with open("output.txt", "r") as file:
    next(file)  # Skip header line
    for line in file:
        n, y = map(float, line.strip().split())
        n_values.append(n)
        y_values.append(y)

# Plot all points
plt.stem(n_values, y_values, linefmt='-', markerfmt='o', basefmt=' ', bottom=0)

# Highlight stems at terms 4, 9, and 14
highlight_terms = [4, 9, 14]
highlight_values = [y_values[i] for i in highlight_terms]

plt.stem(highlight_terms, highlight_values, linefmt='r-', markerfmt='ro', basefmt=' ')

# Set x-axis limits and ticks
plt.xlim(-1, 20)
plt.xticks(range(0, 21))

# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.savefig("graph.png")
