import matplotlib.pyplot as plt

# Read values from the text file
with open('output.txt', 'r') as file:
    values = [int(line.strip()) for line in file]

# Plot the stem graph
n_values = list(range(len(values)))

plt.stem(n_values, values, basefmt='k-', linefmt='k-', markerfmt='ko', label='x(n) = 4n + 1')

# Highlight points at n=17 and n=24 with different color
plt.scatter([17, 24], [values[17], values[24]], c=['r', 'b'], label='Highlighted points')

# Add labels and legend
plt.xlabel('n')
plt.ylabel('x(n)')
plt.legend()

# Show the plot
plt.show()

plt.savefig('q_plot.png', dpi = 300, bbox_inches = 'tight')

