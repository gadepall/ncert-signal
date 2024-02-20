import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("output_data.txt", skiprows=1)

# clear all the previous figures
plt.close("all")

# extract the first 20 terms of the data
n = data[:16, 0]
y_n = data[:16, 1]

# plot the graph
plt.stem(n, y_n, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.axhline(y=200, color='green', linestyle='--',label='y=200')
# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.xticks(n)
plt.title('Simulation v/s Analysis')

# Add legend
plt.legend()
plt.grid(True)
plt.savefig("figure_plot.png")
plt.show()
