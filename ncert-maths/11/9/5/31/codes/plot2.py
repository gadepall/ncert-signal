import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("amount.txt", skiprows=1)

# clear all the previous figures
plt.close("all")

n = data[:10, 0]
y = data[:10, 1]

# plot the graph
highlight_index = 5
plt.scatter(n[highlight_index], y[highlight_index], color='red', marker='x', s=100, label=r'Theory')
plt.stem(n, y, markerfmt='bo', linefmt='b-', basefmt='r-',label=r'Simulation') 
plt.axhline(y=5120, color='green', linestyle='--',label='y=5120')
# Set labels and title
plt.xlabel('n')
plt.ylabel('Amount')
plt.xticks(n)
plt.title('Theory v/s Simulation')

# Add legend
plt.legend()
plt.grid(True)
plt.savefig("plot2.png")
plt.show()
