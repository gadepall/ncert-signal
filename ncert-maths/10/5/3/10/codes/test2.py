import matplotlib.pyplot as plt

# Read data from the file
with open('data.dat', 'r') as file:
    data = [line.split() for line in file.readlines()]

# Extract n_values and x_values2
n_values = [int(row[0]) for row in data]
x_values1 = [int(row[1]) for row in data]
x_values2 = [int(row[2]) for row in data]
y_values1 = [int(row[3]) for row in data]
y_values2 = [int(row[4]) for row in data]


# Plot the graph1
plt.stem(n_values, x_values1, linefmt='b-', markerfmt='bo', basefmt='b')
plt.xlabel('$n$')
plt.ylabel('$x_1(n)$')
# plt.title('Discrete Signal $x_2(n) = (3 + 4n)u(n)$')
plt.grid(True)
plt.show()

# Plot the graph2
plt.stem(n_values, x_values2, linefmt='b-', markerfmt='bo', basefmt='b')
plt.xlabel('$n$')
plt.ylabel('$x_2(n)$')
# plt.title('Discrete Signal $x_2(n) = (9 - 5n)u(n)$')
plt.grid(True)
plt.show()

# Plot the graph1
plt.stem(n_values, y_values1, linefmt='b-', markerfmt='bo', basefmt='b')
plt.xlabel('$n$')
plt.ylabel('$y_1(n)$')
plt.annotate("465", (14, 465), ha="center", va="bottom", xytext=(0, 14), textcoords="offset points")
# plt.title('Discrete Signal $x_2(n) = (3 + 4n)u(n)$')
highlight_color = 'r'
plt.stem(14, y_values1[n_values.index(14)], linefmt=highlight_color, markerfmt=highlight_color + 'o', basefmt=highlight_color)

plt.grid(True)
plt.show()

# Plot the graph2
plt.stem(n_values, y_values2, linefmt='b-', markerfmt='bo', basefmt='b')
plt.xlabel('$n$')
plt.ylabel('$y_2(n)$')
plt.annotate("-390", (14, -450), ha="center", va="bottom", xytext=(0, 14), textcoords="offset points")
highlight_color = 'r'
plt.stem(14, y_values2[n_values.index(14)], linefmt=highlight_color, markerfmt=highlight_color + 'o', basefmt=highlight_color)

# plt.title('Discrete Signal $x_2(n) = (9 - 5n)u(n)$')
plt.grid(True)
plt.show()
