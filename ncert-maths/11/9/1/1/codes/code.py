import matplotlib.pyplot as plt

# Read coordinates from the file
with open("coordinates.txt", "r") as file:
    data = file.readlines()

# Extract x and y values from the data
x_values = [int(line.split()[0]) for line in data]
y_values = [int(line.split()[1]) for line in data]

# Create a stem plot
plt.stem(x_values, y_values, basefmt='r-', linefmt='b-', markerfmt='ro')

# Set plot labels and title
plt.xlabel('n')
plt.ylabel('x(n)')

# Display the plot
plt.grid(True)
plt.show()

