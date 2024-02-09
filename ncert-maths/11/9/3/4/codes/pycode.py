import matplotlib.pyplot as plt

# Read data from the file
with open("coordinates.txt", "r") as file:
    lines = file.readlines()
    data = [tuple(map(float, line.split())) for line in lines]

# Separate x and y data
x_values, y_values = zip(*data)

# Plotting the stem plot
plt.stem(x_values, y_values, linefmt='b-', markerfmt='bo', basefmt='k-')

# Mark the seventh term with a different color (red)
seventh_term = 7
plt.stem(x_values[seventh_term-1], y_values[seventh_term-1], linefmt='r-', markerfmt='ro', basefmt='k-')

# Customize the plot
plt.title('Stem Plot: Geometric Progression')
plt.xlabel('Term (n)')
plt.ylabel('Value')
plt.grid(True)

# Show the plot
plt.show()

