import numpy as np
import matplotlib.pyplot as plt

# import the data from the text file
data = np.loadtxt("allterms.dat", skiprows=1)

# clear all the previous figures
plt.close("all")

# extract the first 20 terms of the data
n = data[:20, 0]
conv_n = data[:20, 1]
sum_n = data[:20, 2]

# plot the graph
highlight_index = 9
plt.stem(n, sum_n, label='s(n)') 
plt.scatter(n, conv_n, color='red', marker='x', label='x(n)*u(n)') 
# Set labels and title
plt.xlabel('n')
plt.ylabel('s_n')
plt.title('Verification')

# Add legend
plt.legend()

plt.savefig("plot.png")
