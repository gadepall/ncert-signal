import matplotlib.pyplot as plt

# Read data from the .dat file
data_file = "data.dat"
with open(data_file, "r") as file:
    lines = file.readlines()

# Extract n and x(n) values from the data
n_values = []
x_n_values = []
for line in lines[1:]:  # Skip the header line
    values = line.strip().split()
    if len(values) >= 2:
        n, x_n = map(float, values[:2])
        n_values.append(n)
        x_n_values.append(x_n)

# Plot the stem plot
plt.stem(n_values, x_n_values, linefmt='b-', markerfmt='bo', basefmt=' ', use_line_collection=True)
plt.axhline(0, color='r', linestyle='--')  # Add mean line at y=0
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

