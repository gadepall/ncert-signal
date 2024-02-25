import matplotlib.pyplot as plt

# Read points from the text file
file_path = 'digital2_points.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Extract data from lines
n_values, points = zip(*[map(int, line.strip().split()) for line in lines])

# Highlight the stem where n=19
highlight_n = 19
highlight_index = n_values.index(highlight_n)
highlight_point = points[highlight_index]

# Plot stem graph
plt.stem(n_values, points, basefmt='b-')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('digital2/graphs/digital2_graph.png')
plt.show()
