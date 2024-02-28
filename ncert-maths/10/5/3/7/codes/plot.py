import matplotlib.pyplot as plt

with open('theoretical.tex', 'r') as file:
    gp_values = [float(line.strip()) for line in file]

with open('convolution.tex', 'r') as file:
    gp_sum_values = [float(line.strip()) for line in file]

plt.stem(range(len(gp_values)), gp_values, markerfmt='r^', linefmt='-', basefmt='b', label='Stem plot')
plt.scatter(range(len(gp_sum_values)), gp_sum_values, color='black', marker='o',label='y(n) using formulae')

# Highlight the 22nd term
highlight_index = 21
plt.scatter(highlight_index, gp_sum_values[highlight_index], color='red', marker='x', s=100, label='22nd term')

plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.legend()
plt.savefig('plot.png')
plt.show()
