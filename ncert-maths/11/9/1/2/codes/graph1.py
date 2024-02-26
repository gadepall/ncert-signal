import matplotlib.pyplot as plt
import numpy as np

# Read the sequence from the file using numpy
sequence_array = np.loadtxt("sequence.txt")

# Plot the sequence
plt.stem(range(len(sequence_array)), sequence_array, basefmt="k-", use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.xticks(range(len(sequence_array)))

# Save the graph as graph1.png
plt.savefig('graph1.png')

# Show the plot
plt.show()

