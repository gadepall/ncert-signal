import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

def strip_line(line):
    return line.strip()

vectorized_strip = np.vectorize(strip_line)

with open('output.dat', 'r') as file:
    lines = np.array(file.readlines())

stripped_lines = vectorized_strip(lines)

lines_list = stripped_lines.tolist()

n_values = np.arange(15)

access_element = np.vectorize(lambda n: lines_list[n])

y_values = access_element(n_values)

plt.stem(n_values, y_values, linefmt='r-', markerfmt='rx', basefmt='r-', label=r'$y(n)$')
plt.stem(n_values, y_values, linefmt='g-', markerfmt='go', basefmt='g-', label='Simulation')

plt.setp(plt.gca().lines[0], markersize=8)  
plt.setp(plt.gca().lines[1], markersize=12) 
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.legend()


#plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.savefig('../figs/plot.png')
plt.show()

