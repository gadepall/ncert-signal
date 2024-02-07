import matplotlib.pyplot as plt

# Read values from the file
with open('values.dat', 'r') as file:
    lines = file.readlines()

n_values, x_values = zip(*[map(int, line.split()) for line in lines])

# Create a stem plot
plt.stem(n_values, x_values, linefmt='-', markerfmt='.', basefmt=' ')

# Highlight points 16 and 23 with different colors
plt.scatter([16, 23], [x_values[16], x_values[23]], c=['red', 'blue'])

# Annotate points 16 and 23
plt.annotate(f'({16},{x_values[16]})', (16, x_values[16]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')
plt.annotate(f'({23},{x_values[23]})', (23, x_values[23]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='blue')

# Color the entire stems corresponding to points 16 and 23
plt.vlines([16, 23], ymin=0, ymax=[x_values[16], x_values[23]], color=['red', 'blue'])

# Show the plot
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of (4n+1)u(n)')
plt.ylim(1, max(x_values) + 1)  # Set y-axis limit to start from 1
plt.yticks([1, 20, 40, 60, 80, 101])  # Label specific values on the y-axis
plt.savefig('a_plot.png', dpi = 300, bbox_inches = 'tight')

