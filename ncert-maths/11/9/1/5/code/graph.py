import matplotlib.pyplot as plt

# Read data from the file
with open("values.dat", "r") as file:
    data = [float(line.strip()) for line in file.readlines()]

# Extract x and y values for the stem plot
x = list(range(len(data)))
y = data

# Create stem plot
plt.stem(x, y, use_line_collection=True)

# Add labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('')

# Show plot
plt.show()

