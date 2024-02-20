import matplotlib.pyplot as plt

# Function to read values from file and return as list
def read_values(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        values = [float(line.strip()) for line in lines]
    return values

# Function to plot stem graph
def plot_stem_graph(ax, x_values, y_values, expression):
    ax.stem(x_values, y_values, use_line_collection=True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('fig*{}'.format(expression))
    ax.grid(True)

# Read values from files
values_py3 = read_values('ncert-signal/ncert-maths/10/5/4/2/codes/py_3,values.txt')
values_py4 = read_values('ncert-signal/ncert-maths/10/5/4/2/codes/py_4,values.txt')
values_py5 = read_values('ncert-signal/ncert-maths/10/5/4/2/codes/py_5,values.txt')
values_py6 = read_values('ncert-signal/ncert-maths/10/5/4/2/codes/py_6,values.txt')

# Generate corresponding x values
a = len(values_py3) - 1
x_values = list(range(a + 1))

# Create subplots
fig, axs = plt.subplots(2, 2)

# Plot stem graphs for each expression
plot_stem_graph(axs[0, 0], x_values, values_py3, 3)
plot_stem_graph(axs[0, 1], x_values, values_py4, 4)
plot_stem_graph(axs[1, 0], x_values, values_py5, 5)
plot_stem_graph(axs[1, 1], x_values, values_py6, 6)

# Adjust layout
plt.tight_layout()

# Save the plot to a PNG file
plt.savefig('ncert-signal/ncert-maths/10/5/4/2/figs/figure1.png')

# Show the plot
plt.show()
