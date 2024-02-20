import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("output.txt", skiprows=1)

# clear all the previous figures
plt.close("all")

# extract the first 20 terms of the data
n = data[:21, 0]
y_n = data[:21, 1]

# plot the graph
highlight_index = [4, 19]
plt.scatter(n[highlight_index], y_n[highlight_index], color='red', marker='x', s=100, label=r'Theory')
plt.stem(n, y_n, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.axhline(y=-25, color='green', linestyle='--',label='y=-25')
# Set labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.xticks(n)
plt.title('Theory v/s Simulation')

# Add legend
plt.legend()
plt.grid(True)
plt.savefig("plot.png")
plt.show()
